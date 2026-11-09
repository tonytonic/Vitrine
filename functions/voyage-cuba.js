// Page Cuba retirée (demande de Stripe, 2026-11-09) : /voyage-cuba renvoie toujours « page introuvable » (404),
// même s'il reste une ancienne copie de voyage-cuba.html dans le dépôt ou dans un cache.
export async function onRequest({ request, env }) {
  let body = '<!doctype html><meta charset="utf-8"><title>Page introuvable · Vezoria</title><p>Page introuvable.</p><p><a href="/">Vezoria</a></p>';
  try { const r = await env.ASSETS.fetch(new URL('/404', request.url)); if (r.ok) body = await r.text(); } catch (e) {}
  return new Response(body, { status: 404, headers: { 'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'no-store', 'X-Robots-Tag': 'noindex' } });
}
