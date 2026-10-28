/* Vezoria · site : bandeau cookies des liens partenaires + Drive (Travelpayouts).
   Ne fait rien tant que AFFIL = False dans outils/generer.py, sauf en mode test (?drive=test).
   Rien n'est chargé depuis Travelpayouts tant que le visiteur n'a pas touché « Accepter ». */
(function(){ try {
  var me = document.currentScript, TP = me && me.getAttribute('data-tp');
  if(!TP || !/^\d+$/.test(TP)) return;
  // Mode test (avant le 1er novembre) : seulement sur l'appareil passé par ?drive=test ; ?drive=off pour arrêter.
  var on = me.getAttribute('data-on') === '1', test = false;
  try {
    var q = /[?&]drive=(test|off)/.exec(location.search);
    if(q && q[1] === 'test') localStorage.setItem('vz_drive_test', '1');
    if(q && q[1] === 'off'){ localStorage.removeItem('vz_drive_test'); localStorage.removeItem('vz_ck'); }
    test = !on && localStorage.getItem('vz_drive_test') === '1';
  } catch(e){}
  if(!on && !test) return;
  var K = 'vz_ck', DAY = 864e5, loaded = false;
  // choix gardé 13 mois si oui, 6 mois si non (recommandations CNIL), puis on redemande
  function get(){ try { var v = JSON.parse(localStorage.getItem(K) || 'null'); if(v && v.t && Date.now() - v.t < (v.ok ? 395 : 182) * DAY) return v; } catch(e){} return null; }
  function set(ok){ try { localStorage.setItem(K, JSON.stringify({ok: !!ok, t: Date.now()})); } catch(e){} }
  function load(){
    if(loaded) return; loaded = true;
    var s = document.createElement('script'); s.async = true; s.setAttribute('data-cmp-ab', '2');
    s.src = 'https://emrldtp.cc/' + btoa(TP).replace(/=+$/, '') + '.js?t=' + TP;   // = le code donné par Travelpayouts
    document.head.appendChild(s);
  }
  function banner(){
    var old = document.getElementById('vz-ck'); if(old) old.remove();
    var d = document.createElement('div'); d.id = 'vz-ck'; d.setAttribute('role', 'dialog'); d.setAttribute('aria-label', 'Cookies des liens partenaires');
    d.innerHTML = '<p>' + (test ? '<i style="color:#e2337f;font-style:normal;font-weight:700">MODE TEST · visible par toi seul</i>' : '') + '<b>🍪 Liens partenaires</b>Certains liens de réservation sont des liens partenaires : si tu réserves après en avoir touché un, Vezoria peut toucher une petite commission, sans surcoût pour toi. Pour ça, notre partenaire Travelpayouts dépose des cookies. C’est toi qui choisis. <a href="confidentialite#cookies">En savoir plus</a></p>' +
      '<div class="ck-b"><button type="button" class="ck-no">Refuser</button><button type="button" class="ck-ok">Accepter</button></div>';
    document.body.appendChild(d);
    d.querySelector('.ck-ok').onclick = function(){ set(true); d.remove(); load(); };
    d.querySelector('.ck-no').onclick = function(){ var was = loaded; set(false); d.remove(); if(was) location.reload(); };
  }
  var c = get();
  if(c && c.ok) load(); else if(!c) banner();
  // lien « Cookies » en bas de page : redonne le choix
  document.addEventListener('click', function(e){ var a = e.target.closest && e.target.closest('[data-ck]'); if(a){ e.preventDefault(); banner(); } });
} catch(err){} })();
