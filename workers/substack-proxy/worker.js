export default {
  async fetch(request) {
    const { searchParams } = new URL(request.url);
    const feedUrl = searchParams.get("url");

    if (!feedUrl || !feedUrl.includes("substack.com")) {
      return new Response("Missing or invalid Substack feed URL", { status: 400 });
    }

    const resp = await fetch(feedUrl, {
      headers: { "User-Agent": "Mozilla/5.0" },
    });

    return new Response(resp.body, {
      status: resp.status,
      headers: { "Content-Type": resp.headers.get("Content-Type") || "application/xml" },
    });
  },
};
