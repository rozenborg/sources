export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const origin = request.headers.get("Origin") || "";
    const allowed =
      origin.includes("rozenborg.github.io") ||
      origin.startsWith("http://localhost") ||
      origin.startsWith("http://127.0.0.1");

    const cors = {
      "Access-Control-Allow-Origin": allowed ? origin : "",
      "Access-Control-Allow-Methods": "POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type, X-Anthropic-Key",
      "Access-Control-Max-Age": "86400",
    };

    if (request.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: cors });
    }

    if (request.method !== "POST" || url.pathname !== "/summarize") {
      return Response.json({ error: "not found" }, { status: 404, headers: cors });
    }

    const anthropicKey = request.headers.get("X-Anthropic-Key");
    if (!anthropicKey) {
      return Response.json({ error: "X-Anthropic-Key header required" }, { status: 401, headers: cors });
    }

    let body;
    try {
      body = await request.json();
    } catch {
      return Response.json({ error: "invalid JSON body" }, { status: 400, headers: cors });
    }

    const { url: articleUrl, title, source_type } = body;
    if (!articleUrl) {
      return Response.json({ error: "url is required" }, { status: 400, headers: cors });
    }

    // 1. Fetch the article content
    let articleText;
    try {
      const resp = await fetch(articleUrl, {
        headers: { "User-Agent": "Sourcerer/1.0 (summary bot)" },
        redirect: "follow",
      });
      if (!resp.ok) throw new Error("HTTP " + resp.status);
      const html = await resp.text();
      articleText = htmlToText(html);
    } catch (e) {
      return Response.json(
        { error: "Failed to fetch article: " + e.message },
        { status: 502, headers: cors }
      );
    }

    // Truncate to ~30k chars
    articleText = articleText.slice(0, 30000);

    // 2. Build the summary prompt
    let typeHint = "";
    if (source_type === "podcast") {
      typeHint =
        "This is a podcast transcript. Focus on the main arguments and insights from each speaker. Ignore filler, ads, and tangential small talk.\n\n";
    } else if (source_type === "sitemap") {
      typeHint =
        "This is a company blog post. Focus on product announcements, technical capabilities, and strategic implications.\n\n";
    }

    const prompt =
      "You are an expert analyst creating an intelligence briefing.\n\n" +
      "Produce a two-part summary:\n\n" +
      '1. HEADLINE: One or two punchy sentences — the "so what?" of this piece. ' +
      "Make it concrete and specific, not generic. No bullet points, no bold, just a plain paragraph.\n\n" +
      "2. Then a line containing only --- (a horizontal rule).\n\n" +
      "3. DETAILS: 5-8 bullet points covering key facts, strategic implications, and actionable insights. " +
      "Use markdown bullet points (- **Bold label** explanation). Be specific and concise.\n\n" +
      "No introductory phrases, no section headings — just the headline paragraph, then ---, then the bullets.\n\n" +
      typeHint +
      `Title: ${title || "Unknown"}\n\n` +
      `Content:\n${articleText}`;

    // 3. Call Claude API
    try {
      const claudeResp = await fetch("https://api.anthropic.com/v1/messages", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "x-api-key": anthropicKey,
          "anthropic-version": "2023-06-01",
        },
        body: JSON.stringify({
          model: "claude-sonnet-4-20250514",
          max_tokens: 1024,
          messages: [{ role: "user", content: prompt }],
        }),
      });

      if (!claudeResp.ok) {
        const err = await claudeResp.text();
        throw new Error("Claude API error: " + claudeResp.status + " " + err);
      }

      const result = await claudeResp.json();
      const summaryBody = result.content[0].text;

      return Response.json({ body: summaryBody }, { headers: cors });
    } catch (e) {
      return Response.json(
        { error: "Summarization failed: " + e.message },
        { status: 500, headers: cors }
      );
    }
  },
};

/**
 * Extract readable text from HTML. Strips tags, scripts, styles,
 * and collapses whitespace.
 */
function htmlToText(html) {
  // Remove script and style blocks
  let text = html.replace(/<script[^>]*>[\s\S]*?<\/script>/gi, " ");
  text = text.replace(/<style[^>]*>[\s\S]*?<\/style>/gi, " ");
  // Remove nav, header, footer
  text = text.replace(/<(nav|header|footer)[^>]*>[\s\S]*?<\/\1>/gi, " ");
  // Convert block elements to newlines
  text = text.replace(/<\/(p|div|h[1-6]|li|tr|br\s*\/?)>/gi, "\n");
  text = text.replace(/<br\s*\/?>/gi, "\n");
  // Strip remaining tags
  text = text.replace(/<[^>]+>/g, " ");
  // Decode common HTML entities
  text = text.replace(/&amp;/g, "&");
  text = text.replace(/&lt;/g, "<");
  text = text.replace(/&gt;/g, ">");
  text = text.replace(/&quot;/g, '"');
  text = text.replace(/&#39;/g, "'");
  text = text.replace(/&nbsp;/g, " ");
  // Collapse whitespace
  text = text.replace(/[ \t]+/g, " ");
  text = text.replace(/\n{3,}/g, "\n\n");
  return text.trim();
}
