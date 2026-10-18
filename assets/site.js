/* Vezoria · site : met en avant le bon bouton (iPhone ou Android) selon le téléphone. Aucun pistage. */
(function(){ try {
  var ios = /iPhone|iPad|iPod/.test(navigator.userAgent) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
  var and = /Android/.test(navigator.userAgent);
  document.querySelectorAll('.cta').forEach(function(c){ var a = c.querySelector('.btn.and'), i = c.querySelector('.btn.ios'); if(!a || !i) return;
    if(ios){ c.insertBefore(i, a); i.className = 'btn and'; a.className = 'btn ios'; } else if(and){ i.style.display = 'none'; } });
  if(ios) document.querySelectorAll('[data-store]').forEach(function(x){ x.href = 'https://vezoria.pages.dev/'; });
} catch(e){} })();
