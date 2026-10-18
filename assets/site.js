/* Vezoria · site : bouton « Installer » et boutons d'installation selon le téléphone. Aucun pistage, aucun cookie. */
(function(){ try {
  var PLAY = 'https://play.google.com/store/apps/details?id=fr.vezoria.app', APP = 'https://vezoria.pages.dev/';
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
  function iosSheet(){
    sheet('<h2>Installer Vezoria sur iPhone</h2>' +
      (safari ? '' : '<p class="vz-warn">⚠️ Ouvre d’abord cette page dans <b>Safari</b> : l’installation ne marche pas depuis ' + (inApp ? 'le navigateur de cette appli' : 'ce navigateur') + '.</p>') +
      '<ol class="vz-steps"><li>Touche <b>« Ouvrir Vezoria »</b> ci-dessous.</li><li>Dans Safari, touche le bouton <b>Partager</b> <span class="vz-ic">⬆︎</span> (le carré avec une flèche).</li><li>Choisis <b>« Sur l’écran d’accueil »</b>, puis <b>« Ajouter »</b>.</li></ol>' +
      '<a class="btn and vz-go" href="' + APP + '">🍏 Ouvrir Vezoria</a><p class="vz-small">Ensuite, ouvre toujours Vezoria depuis son icône.</p>');
  }
  function deskSheet(){
    sheet('<h2>Installer Vezoria</h2><p>Vezoria s’installe sur ton téléphone. Ouvre ce site depuis ton téléphone, ou choisis :</p>' +
      '<div class="vz-two"><a class="btn and vz-go" href="' + PLAY + '">🤖 Android · Play Store</a><a class="btn and vz-go" href="#" data-ios>🍏 iPhone · comment faire</a></div>');
    var b = document.querySelector('#vz-sheet [data-ios]'); if(b) b.onclick = function(e){ e.preventDefault(); iosSheet(); };
  }
  function install(e){ if(e) e.preventDefault(); if(and) location.href = PLAY; else if(ios) iosSheet(); else deskSheet(); }

  // bouton « Installer » en haut à droite : décide au moment du toucher
  document.querySelectorAll('[data-store]').forEach(function(x){ x.addEventListener('click', install); });
  // boutons Android / iPhone des pages
  document.querySelectorAll('.cta').forEach(function(c){ var a = c.querySelector('.btn.and'), i = c.querySelector('.btn.ios'); if(!a || !i) return;
    i.addEventListener('click', function(e){ e.preventDefault(); iosSheet(); });
    if(ios){ c.insertBefore(i, a); i.className = 'btn and'; a.className = 'btn ios'; a.style.display = 'none'; }
    else if(and){ i.style.display = 'none'; } });
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
