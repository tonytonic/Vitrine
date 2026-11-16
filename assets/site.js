/* Vezoria · site : bouton « Installer » et boutons d'installation selon le téléphone. Aucun pistage, aucun cookie. */
(function(){ try {
  var PLAY = 'https://play.google.com/store/apps/details?id=fr.vezoria.app', APP = 'https://vezoria.pages.dev/';
  var PLAY_LIVE = true;   // true le jour où Google Play publie l’appli (et dans outils/generer.py) ; d’ici là, Android installe l’appli web depuis Chrome   // le jour du lancement, si l’appli passe sur app.vezoria.fr : changer APP ici et dans outils/generer.py
  var ua = navigator.userAgent || '';
  var ios = /iPhone|iPad|iPod/.test(ua) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
  var and = /Android/i.test(ua);
  var inApp = /Instagram|FBAN|FBAV|FB_IAB|Line\/|Snapchat|TikTok|Twitter|LinkedInApp/i.test(ua);   // navigateur intégré d'une appli
  var safari = ios && /Safari/.test(ua) && !/CriOS|FxiOS|EdgiOS|OPiOS/.test(ua) && !inApp;

  function sheet(html){
    var old = document.getElementById('vz-sheet'); if(old) old.remove();
    var d = document.createElement('div'); d.id = 'vz-sheet';
    d.innerHTML = '<div class="vz-bg"></div><div class="vz-card" role="dialog" aria-modal="true"><button type="button" class="vz-x" aria-label="Fermer">✕</button>' + html + '</div>';
    document.body.appendChild(d); document.body.style.overflow = 'hidden';
    var close = function(){ d.remove(); document.body.style.overflow = ''; };
    d.querySelector('.vz-bg').onclick = close; d.querySelector('.vz-x').onclick = close;
  }

  // 🌐 Traduction automatique (Google Traduction, seulement si on la demande : rien n’est chargé avant le clic)
  var LANGS = [['en','🇬🇧','English'],['es','🇪🇸','Español'],['de','🇩🇪','Deutsch'],['it','🇮🇹','Italiano'],['pt','🇵🇹','Português'],['nl','🇳🇱','Nederlands'],['pl','🇵🇱','Polski'],['ru','🇷🇺','Русский'],['uk','🇺🇦','Українська'],['tr','🇹🇷','Türkçe'],['ar','🇸🇦','العربية'],['zh-CN','🇨🇳','中文'],['ja','🇯🇵','日本語'],['ko','🇰🇷','한국어']];
  var onTr = /\.translate\.goog$/.test(location.hostname);
  var curTr = (location.search.match(/[?&]_x_tr_tl=([^&]+)/) || [])[1] || '';
  function origUrl(){ var h = onTr ? location.hostname.replace(/\.translate\.goog$/, '').replace(/--/g, '\u0000').replace(/-/g, '.').replace(/\u0000/g, '-') : location.hostname;
    var q = location.search.replace(/[?&]_x_tr_[a-z]+=[^&]*/g, '').replace(/^&/, '?'); return 'https://' + h + location.pathname + q + location.hash; }
  function trUrl(lg){ var o = new URL(origUrl()); var h = o.hostname.replace(/-/g, '--').replace(/\./g, '-') + '.translate.goog';
    var q = o.search ? o.search + '&' : '?'; return 'https://' + h + o.pathname + q + '_x_tr_sl=fr&_x_tr_tl=' + lg + '&_x_tr_hl=' + lg + '&_x_tr_pto=wapp' + o.hash; }
  function langSheet(){
    sheet('<h2>🌐 Langue · Language</h2><p class="vz-small">Traduction automatique de Google · Automatic translation by Google</p><div class="vz-langs">' +
      LANGS.map(function(l){ return '<a href="' + trUrl(l[0]) + '" lang="' + l[0] + '"' + (curTr === l[0] ? ' class="on"' : '') + '><span>' + l[1] + '</span>' + l[2] + '</a>'; }).join('') +
      '</div>' + (onTr ? '<a class="vz-orig" href="' + origUrl() + '">🇫🇷 Version originale en français</a>' : ''));
  }
  // le bouton 🌐 est ajouté ici (pas besoin de toucher les 266 pages)
  (function(){ var nav = document.querySelector('header.top nav'); if(!nav || nav.querySelector('[data-lang]')) return;
    var b = document.createElement('button'); b.type = 'button'; b.className = 'lang-mini'; b.setAttribute('data-lang', ''); b.setAttribute('aria-label', 'Langue · Language · Idioma'); b.textContent = '🌐';
    var last = nav.lastElementChild; if(last && /cta-mini/.test(last.className)) nav.insertBefore(b, last); else nav.appendChild(b); })();
  document.querySelectorAll('[data-lang]').forEach(function(b){ b.addEventListener('click', langSheet); });
  // visiteur dont le téléphone n’est pas en français : on propose une fois sa langue
  (function(){ if(onTr) return; var nl = (navigator.language || 'fr').toLowerCase(); if(/^fr/.test(nl)) return;
    // pas de stockage (promis dans la page confidentialité) : on ne le propose qu’en arrivant sur le site
    try { if(document.referrer && new URL(document.referrer).hostname === location.hostname) return; } catch(e){}
    var code = nl.indexOf('zh') === 0 ? 'zh-CN' : nl.slice(0, 2); var L = LANGS.filter(function(l){ return l[0] === code; })[0] || LANGS[0];
    var b = document.querySelector('[data-lang]'); if(b) b.classList.add('pulse');
    var t = document.createElement('div'); t.id = 'vz-lgtip'; t.setAttribute('lang', L[0]);
    t.innerHTML = '<span>' + L[1] + '</span><span style="flex:1">' + L[2] + ' ?</span><a href="' + trUrl(L[0]) + '">🌐 ' + L[2] + '</a><button type="button" aria-label="✕">✕</button>';
    document.body.appendChild(t);
    var done = function(){ t.remove(); };
    t.querySelector('button').onclick = done; t.querySelector('a').addEventListener('click', done);
  })();
  function iosSheet(){
    sheet('<h2>Installer Vezoria sur iPhone</h2>' +
      (safari ? '' : '<p class="vz-warn">⚠️ Ouvre d’abord cette page dans <b>Safari</b> : l’installation ne marche pas depuis ' + (inApp ? 'le navigateur de cette appli' : 'ce navigateur') + '.</p>') +
      '<ol class="vz-steps"><li>Touche <b>« Ouvrir Vezoria »</b> ci-dessous.</li><li>Dans Safari, touche le bouton <b>Partager</b> <span class="vz-ic">⬆︎</span> (le carré avec une flèche).</li><li>Choisis <b>« Sur l’écran d’accueil »</b>, puis <b>« Ajouter »</b>.</li></ol>' +
      '<a class="btn and vz-go" href="' + APP + '">🍏 Ouvrir Vezoria</a><p class="vz-small">Ensuite, ouvre toujours Vezoria depuis son icône.</p>');
  }
  function andSheet(){
    var chrome = /Chrome\//.test(ua) && !/SamsungBrowser|EdgA|OPR\/|Firefox/.test(ua) && !inApp;
    sheet('<h2>Installer Vezoria sur Android</h2>' +
      (chrome ? '' : '<p class="vz-warn">⚠️ Ouvre d’abord cette page dans <b>Chrome</b> : l’installation marche le mieux depuis Chrome' + (inApp ? ', pas depuis le navigateur de cette appli' : '') + '.</p>') +
      '<ol class="vz-steps"><li>Touche <b>« Ouvrir Vezoria »</b> ci-dessous.</li><li>Dans Chrome, touche le menu <b>⋮</b> (en haut à droite).</li><li>Choisis <b>« Installer l’application »</b> (ou « Ajouter à l’écran d’accueil »), puis <b>« Installer »</b>.</li></ol>' +
      '<a class="btn and vz-go" href="' + APP + '">🤖 Ouvrir Vezoria</a><p class="vz-small">Ensuite, ouvre toujours Vezoria depuis son icône.</p>');
  }
  function pcSheet(){
    var mac = /Macintosh/.test(ua), edge = /Edg\//.test(ua), chrome = /Chrome\//.test(ua) && !edge && !/OPR\//.test(ua), fx = /Firefox\//.test(ua), saf = !chrome && !edge && !fx && /Safari\//.test(ua);
    sheet('<h2>Installer Vezoria sur ordinateur</h2>' +
      (fx ? '<p class="vz-warn">⚠️ Firefox ne sait pas installer les applis web : ouvre plutôt cette page dans <b>Chrome</b> ou <b>Edge</b>' + (mac ? ' (ou Safari)' : '') + '.</p>' : '') +
      (saf ? '<ol class="vz-steps"><li>Clique sur <b>« Ouvrir Vezoria »</b> ci-dessous.</li><li>Menu <b>Fichier</b> → <b>« Ajouter au Dock »</b>.</li></ol>'
           : '<ol class="vz-steps"><li>Clique sur <b>« Ouvrir Vezoria »</b> ci-dessous.</li><li>Clique sur l’icône <b>« Installer »</b> au bout de la barre d’adresse, ou menu <b>⋮</b> → <b>« Installer Vezoria »</b>.</li><li>Vezoria s’ouvre dans sa propre fenêtre, comme un logiciel.</li></ol>') +
      '<a class="btn and vz-go" href="' + APP + '">💻 Ouvrir Vezoria</a><p class="vz-small">Pour garder le même carnet que sur ton téléphone : ☁️ Cloud → « Tu as déjà un code ? ». <a href="installer-vezoria-pc">Le guide complet</a></p>');
  }
  function deskSheet(){
    sheet('<h2>Installer Vezoria</h2><p>Vezoria marche sur ordinateur, sur Android et sur iPhone. Choisis :</p>' +
      '<div class="vz-two"><a class="btn and vz-go" href="#" data-pc>💻 Sur cet ordinateur</a>' + (PLAY_LIVE ? '<a class="btn and vz-go" href="' + PLAY + '">🤖 Android · Play Store</a>' : '<a class="btn and vz-go" href="#" data-and>🤖 Android · comment faire</a>') + '<a class="btn and vz-go" href="#" data-ios>🍏 iPhone · comment faire</a></div>');
    var b = document.querySelector('#vz-sheet [data-ios]'); if(b) b.onclick = function(e){ e.preventDefault(); iosSheet(); };
    var a = document.querySelector('#vz-sheet [data-and]'); if(a) a.onclick = function(e){ e.preventDefault(); andSheet(); };
    var c = document.querySelector('#vz-sheet [data-pc]'); if(c) c.onclick = function(e){ e.preventDefault(); pcSheet(); };
  }
  function install(e){ if(e) e.preventDefault(); if(and){ if(PLAY_LIVE) location.href = PLAY; else andSheet(); } else if(ios) iosSheet(); else deskSheet(); }

  // bouton « Installer » en haut à droite : décide au moment du toucher
  document.querySelectorAll('[data-store]').forEach(function(x){ x.addEventListener('click', install); });
  // boutons Android / iPhone des pages
  // boutons Android / iPhone / ordinateur des pages : sur un téléphone, seulement le sien ; sur ordinateur, « PC · Mac » en premier
  document.querySelectorAll('.cta').forEach(function(c){ var a = c.querySelector('.btn.and'), i = c.querySelector('.btn.ios'), p = c.querySelector('.btn.pc'); if(!a || !i) return;
    i.addEventListener('click', function(e){ e.preventDefault(); iosSheet(); });
    if(p) p.addEventListener('click', function(e){ e.preventDefault(); pcSheet(); });
    if(!PLAY_LIVE) a.addEventListener('click', function(e){ e.preventDefault(); andSheet(); });
    if(ios){ c.insertBefore(i, a); i.className = 'btn and'; a.className = 'btn ios'; a.style.display = 'none'; if(p) p.style.display = 'none'; }
    else if(and){ i.style.display = 'none'; if(p) p.style.display = 'none'; }
    else if(p){ c.insertBefore(p, a); p.className = 'btn and pc'; a.className = 'btn ios'; } });
} catch(err){} })();

/* Navigation flottante : ← Retour · Menu · ↑ Haut de page */
(function(){ try {
  var home = /\/(index(\.html)?)?$/.test(location.pathname);
  var n = document.createElement('nav'); n.className = 'vz-fnav'; n.setAttribute('aria-label', 'Navigation');
  n.innerHTML = (home ? '' : '<button type="button" class="vz-f" data-a="back" aria-label="Page précédente">←<span>Retour</span></button><a class="vz-f" href="./" aria-label="Retour au menu">☰<span>Menu</span></a>')
    + '<button type="button" class="vz-f vz-up" data-a="top" aria-label="Remonter en haut de la page">↑<span>Haut</span></button>';
  document.body.appendChild(n);
  var back = n.querySelector('[data-a=back]');
  if(back) back.onclick = function(){
    var same = false; try { same = document.referrer && new URL(document.referrer).origin === location.origin; } catch(e){}
    if(same && history.length > 1) history.back(); else location.href = './';
  };
  var up = n.querySelector('[data-a=top]');
  up.onclick = function(){ window.scrollTo({top:0, behavior:'smooth'}); };
  var tick = function(){ var y = window.scrollY || document.documentElement.scrollTop;
    up.classList.toggle('on', y > 500); n.classList.toggle('on', y > 200 || !home); };
  window.addEventListener('scroll', tick, {passive:true}); tick();
  // les rubriques dépliantes : une ancre (#rubrique) ouvre la bonne
  var openHash = function(){ var id = decodeURIComponent((location.hash || '').slice(1)); if(!id) return; var d = document.getElementById(id); if(d && d.tagName === 'DETAILS'){ d.open = true; d.scrollIntoView({block:'start'}); } };
  window.addEventListener('hashchange', openHash); openHash();
} catch(err){} })();

/* ✉️ « Me prévenir du lancement » : envoi sans recharger la page (sans script, le formulaire marche quand même) */
(function(){ try {
  var MSG = {ok:'🎉 C’est noté ! Tu recevras un seul e-mail, le jour du lancement.', deja:'👍 Tu es déjà sur la liste : à très vite !', email:'⚠️ Cette adresse e-mail ne semble pas valide.', consent:'⚠️ Coche la case pour accepter de recevoir l’e-mail du lancement.', trop:'⏳ Trop d’essais : réessaie dans un moment.', erreur:'⚠️ Petit souci, réessaie dans un instant.', stop:'✅ Tu es désinscrit·e : ton adresse a été effacée.'};
  document.querySelectorAll('form[data-wl]').forEach(function(f){
    var src = f.querySelector('[name=source]'); if(src) src.value = (location.pathname.replace(/^\//, '') || 'accueil').slice(0, 80);
    f.addEventListener('submit', function(e){
      e.preventDefault(); var m = f.querySelector('.wl-msg'), b = f.querySelector('button[type=submit]');
      var data = {}; new FormData(f).forEach(function(v, k){ data[k] = v; });
      if(b) b.disabled = true; if(m){ m.textContent = '…'; m.className = 'wl-msg'; }
      fetch('/api/waitlist', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify(data)})
        .then(function(r){ return r.json().catch(function(){ return {code:'erreur'}; }); })
        .then(function(j){ var c = (j && j.code) || 'erreur'; if(m){ m.textContent = MSG[c] || MSG.erreur; m.className = 'wl-msg ' + (c === 'ok' || c === 'deja' ? 'ok' : 'ko'); }
          if(c === 'ok' || c === 'deja'){ f.classList.add('done'); } else if(b) b.disabled = false; })
        .catch(function(){ if(m){ m.textContent = MSG.erreur; m.className = 'wl-msg ko'; } if(b) b.disabled = false; });
    });
  });
  // page « merci » : le bon message selon le résultat
  var r = /[?&]r=([a-z]+)/.exec(location.search), t = document.getElementById('mr-t'), p = document.getElementById('mr-p');
  if(r && t && p && r[1] !== 'ok'){ t.textContent = r[1] === 'deja' || r[1] === 'stop' ? (r[1] === 'stop' ? 'C’est fait' : 'Déjà inscrit·e !') : 'Oups'; p.textContent = MSG[r[1]] || MSG.erreur; }
} catch(err){} })();
