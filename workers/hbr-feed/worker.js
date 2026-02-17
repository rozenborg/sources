/**
 * Cloudflare Worker that scrapes HBR topic pages and serves RSS.
 * HBR blocks direct access from CI/cloud IPs but Workers edge
 * requests typically pass through. Modeled on the RSSHub HBR route.
 *
 * Usage: GET /?topic=technology  (default: technology)
 *
 * HBR topic pages contain <stream-content> elements whose children
 * (.stream-item) carry structured data-* attributes we can extract.
 */

const DEFAULT_TOPIC = "technology";
const HBR = "https://hbr.org";

function extractAttr(tag, name) {
  const m = tag.match(new RegExp(`\\b${name}="([^"]*)"`, "i"));
  return m ? decodeEntities(m[1]) : "";
}

function decodeEntities(s) {
  return s
    .replace(/&amp;/g, "&")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'");
}

function escapeXml(s) {
  return s
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

export default {
  async fetch(request) {
    const { searchParams } = new URL(request.url);
    const topic = searchParams.get("topic") || DEFAULT_TOPIC;
    const topicUrl = `${HBR}/topic/${topic}`;

    const resp = await fetch(topicUrl, {
      headers: {
        "User-Agent":
          "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        Accept:
          "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
      },
    });

    if (!resp.ok) {
      return new Response(
        `Upstream ${resp.status}: could not fetch ${topicUrl}`,
        { status: 502 }
      );
    }

    const html = await resp.text();

    // Extract articles from elements carrying data-title + data-url
    const items = [];
    const tagRe = /<[^>]+\bdata-title="[^"]*"[^>]*\bdata-url="[^"]*"[^>]*>/gi;
    let match;
    while ((match = tagRe.exec(html)) !== null) {
      const tag = match[0];
      const title = extractAttr(tag, "data-title");
      const url = extractAttr(tag, "data-url");
      if (!title || !url) continue;
      items.push({
        title,
        link: url.startsWith("http") ? url : `${HBR}${url}`,
        author: extractAttr(tag, "data-authors"),
        category: extractAttr(tag, "data-topic"),
      });
    }

    const rssItems = items
      .map(
        (it) => `    <item>
      <title>${escapeXml(it.title)}</title>
      <link>${escapeXml(it.link)}</link>
      ${it.author ? `<dc:creator>${escapeXml(it.author)}</dc:creator>` : ""}
      ${it.category ? `<category>${escapeXml(it.category)}</category>` : ""}
    </item>`
      )
      .join("\n");

    const rss = `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:dc="http://purl.org/dc/elements/1.1/">
  <channel>
    <title>Harvard Business Review – ${escapeXml(topic)}</title>
    <link>${escapeXml(topicUrl)}</link>
    <description>HBR articles on ${escapeXml(topic)}</description>
${rssItems}
  </channel>
</rss>`;

    return new Response(rss, {
      headers: {
        "Content-Type": "application/rss+xml; charset=utf-8",
        "Cache-Control": "public, max-age=3600",
      },
    });
  },
};
