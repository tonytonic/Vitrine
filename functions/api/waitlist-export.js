// 📋 Export de la liste « Me prévenir » en CSV (pour toi seulement)
// https://vezoria.fr/api/waitlist-export?key=TA_CLE_SECRETE        → fichier CSV
// https://vezoria.fr/api/waitlist-export?key=TA_CLE_SECRETE&n=1    → juste le nombre d'inscrits
// Variable secrète obligatoire : ADMIN_KEY (voir MARCHE-A-SUIVRE.html)

export async function onRequestGet({ request, env }) {
  const u = new URL(request.url), key = u.searchParams.get('key') || '';
  if (!env.ADMIN_KEY || key.length < 16 || key !== env.ADMIN_KEY) return new Response('Accès refusé', { status: 403 });
  if (!env.DB) return new Response('Base D1 non reliée (variable DB)', { status: 500 });
  try { await env.DB.prepare('UPDATE waitlist SET ip_hash = NULL WHERE ip_hash IS NOT NULL AND created_at < ?').bind(Date.now() - 3600e3).run(); } catch (e) {}
  if (u.searchParams.get('n')) {
    const r = await env.DB.prepare('SELECT COUNT(*) AS n, interest FROM waitlist GROUP BY interest').all();
    return new Response(JSON.stringify(r.results), { headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store' } });
  }
  const r = await env.DB.prepare('SELECT email, created_at, interest, source, token FROM waitlist ORDER BY created_at').all();
  const q = v => '"' + String(v == null ? '' : v).replace(/"/g, '""') + '"';
  const base = u.origin + '/api/waitlist?stop=';
  const rows = [['email', 'inscrit_le', 'voyage_plutot', 'page', 'lien_desinscription'].join(';')]
    .concat(r.results.map(x => [q(x.email), q(new Date(x.created_at).toISOString().slice(0, 16).replace('T', ' ')), q(x.interest), q(x.source), q(base + x.token)].join(';')));
  return new Response('﻿' + rows.join('\n'), { headers: { 'content-type': 'text/csv; charset=utf-8', 'content-disposition': 'attachment; filename="vezoria-liste-lancement.csv"', 'cache-control': 'no-store' } });
}
