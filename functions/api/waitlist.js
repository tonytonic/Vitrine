// ✉️ Liste « Me prévenir du lancement » de Vezoria (Cloudflare Pages Function)
// POST /api/waitlist        → inscription (formulaire classique ou JSON)
// GET  /api/waitlist?stop=… → désinscription (lien mis dans l'e-mail de lancement)
// Liaison D1 obligatoire : nom de variable  DB  (voir MARCHE-A-SUIVRE.html)
// Variable facultative : SALT (texte au hasard, sert à brouiller les adresses IP)

const EMAIL = /^[^\s@<>"']{1,64}@[^\s@<>"']{1,190}\.[a-z]{2,24}$/i;
const INTERETS = ['', 'amis', 'famille', 'couple', 'solo', 'groupe'];

function json(data, status) {
  return new Response(JSON.stringify(data), { status: status || 200, headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store' } });
}
async function sha(txt) {
  const b = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(txt));
  return [...new Uint8Array(b)].map(x => x.toString(16).padStart(2, '0')).join('');
}

export async function onRequestPost({ request, env }) {
  const ct = request.headers.get('content-type') || '';
  const isJson = ct.includes('application/json');
  const reply = code => {
    const good = code === 'ok' || code === 'deja';
    if (isJson) return json({ ok: good, code }, good ? 200 : (code === 'erreur' ? 500 : 400));
    return Response.redirect(new URL('/merci?r=' + code, request.url).toString(), 303);
  };
  let d = {};
  try { d = isJson ? await request.json() : Object.fromEntries(await request.formData()); } catch (e) { return reply('erreur'); }
  if (d.site) return reply('ok');                                   // piège à robots : on fait semblant
  const email = String(d.email || '').trim().toLowerCase();
  if (!EMAIL.test(email) || email.length > 254) return reply('email');
  if (!d.consent) return reply('consent');
  if (!env.DB) return reply('erreur');
  const now = Date.now();
  const ipHash = await sha((request.headers.get('cf-connecting-ip') || '') + (env.SALT || 'vezoria'));
  try {
    await env.DB.prepare('UPDATE waitlist SET ip_hash = NULL WHERE ip_hash IS NOT NULL AND created_at < ?').bind(now - 3600e3).run();   // l'empreinte IP ne sert qu'une heure
    const r = await env.DB.prepare('SELECT COUNT(*) AS n FROM waitlist WHERE ip_hash = ?').bind(ipHash).first();
    if (r && r.n >= 5) return reply('trop');                          // 5 inscriptions par heure et par connexion, pas plus
    const interest = INTERETS.includes(String(d.interest || '')) ? String(d.interest || '') : '';
    await env.DB.prepare('INSERT INTO waitlist (email, created_at, source, interest, token, ip_hash) VALUES (?, ?, ?, ?, ?, ?)')
      .bind(email, now, String(d.source || '').slice(0, 80), interest, crypto.randomUUID(), ipHash).run();
  } catch (e) {
    if (/UNIQUE/i.test(String(e && e.message || e))) return reply('deja');
    return reply('erreur');
  }
  return reply('ok');
}

export async function onRequestGet({ request, env }) {
  const t = new URL(request.url).searchParams.get('stop');
  if (t && env.DB) { try { await env.DB.prepare('DELETE FROM waitlist WHERE token = ?').bind(t.slice(0, 64)).run(); } catch (e) {} return Response.redirect(new URL('/merci?r=stop', request.url).toString(), 303); }
  return json({ ok: true });
}
