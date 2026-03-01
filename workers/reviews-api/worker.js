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
      "Access-Control-Allow-Methods": "GET, POST, DELETE, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type, X-Auth-Token",
      "Access-Control-Max-Age": "86400",
    };

    if (request.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: cors });
    }

    // Auth check
    const token = request.headers.get("X-Auth-Token");
    if (!token || token !== env.AUTH_TOKEN) {
      return Response.json({ error: "unauthorized" }, { status: 401, headers: cors });
    }

    const path = url.pathname;

    // GET /reviews — return all reviews
    if (request.method === "GET" && path === "/reviews") {
      const data = await env.REVIEWS.get("reviews", "json");
      return Response.json(data || { reviews: {} }, { headers: cors });
    }

    // POST /review — save a review {path, status}
    if (request.method === "POST" && path === "/review") {
      const body = await request.json();
      if (!body.path) {
        return Response.json({ error: "path is required" }, { status: 400, headers: cors });
      }
      if (!["pass", "save", "star", null].includes(body.status)) {
        return Response.json({ error: "status must be pass, save, star, or null" }, { status: 400, headers: cors });
      }

      const data = (await env.REVIEWS.get("reviews", "json")) || { reviews: {} };

      if (body.status === null) {
        delete data.reviews[body.path];
      } else {
        data.reviews[body.path] = {
          status: body.status,
          reviewed_at: new Date().toISOString(),
        };
      }

      await env.REVIEWS.put("reviews", JSON.stringify(data));
      return Response.json({ ok: true, path: body.path, status: body.status }, { headers: cors });
    }

    // DELETE /review?path=... — remove a review
    if (request.method === "DELETE" && path === "/review") {
      const articlePath = url.searchParams.get("path");
      if (!articlePath) {
        return Response.json({ error: "path param is required" }, { status: 400, headers: cors });
      }

      const data = (await env.REVIEWS.get("reviews", "json")) || { reviews: {} };
      delete data.reviews[articlePath];
      await env.REVIEWS.put("reviews", JSON.stringify(data));
      return Response.json({ ok: true, path: articlePath }, { headers: cors });
    }

    return Response.json({ error: "not found" }, { status: 404, headers: cors });
  },
};
