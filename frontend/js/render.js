// ---------------- RENDER ----------------
document.getElementById('descubri-row').innerHTML = negocios.map(n => `
  <article class="card reveal">
    <div class="card-img-wrap">
      <img src="${n.img}" alt="${n.nombre}" loading="lazy">
      ${n.destacado ? '<span class="badge">DESTACADO</span>' : ''}
    </div>
    <div class="card-body">
      <div class="cat">${n.cat}</div>
      <h3>${n.nombre}</h3>
      <div class="loc">📍 ${n.loc}</div>
      <div class="tags">${n.tags.map(t=>`<span class="tag">${t}</span>`).join('')}</div>
    </div>
  </article>
`).join('');

document.getElementById('cat-grid').innerHTML = categorias.map(c => `
  <a href="#descubri" class="cat-card reveal">
    <div class="cat-icon">${c.icon}</div>
    <div class="cat-card-text">
      <h3>${c.nombre}</h3>
      <p>${c.desc}</p>
    </div>
  </a>
`).join('');

document.getElementById('destacados-grid').innerHTML = destacados.map(n => `
  <article class="card reveal">
    <div class="card-img-wrap">
      <img src="${n.img}" alt="${n.nombre}" loading="lazy">
      <span class="badge">DESTACADO</span>
    </div>
    <div class="card-body">
      <div class="cat">${n.cat}</div>
      <h3>${n.nombre}</h3>
      <div class="loc">📍 ${n.loc}</div>
      <div class="tags">${n.tags.map(t=>`<span class="tag">${t}</span>`).join('')}</div>
    </div>
  </article>
`).join('');

document.getElementById('promos-grid').innerHTML = promos.map(p => `
  <article class="promo-card reveal">
    <div class="promo-img"><img src="${p.img}" alt="${p.promo}" loading="lazy"></div>
    <div class="promo-body">
      <span class="promo-vig">${p.vig}</span>
      <h3>${p.promo}</h3>
      <p class="promo-neg">${p.neg}</p>
      <span class="promo-link">Descubrir</span>
    </div>
  </article>
`).join('');

document.getElementById('eventos-grid').innerHTML = eventos.map(e => `
  <article class="evento-card reveal">
    <div class="evento-date"><span class="d">${e.dia}</span><span class="m">${e.mes}</span></div>
    <div class="evento-body">
      <span class="evento-cat">${e.cat}</span>
      <h3>${e.nombre}</h3>
      <div class="evento-meta">
        <span>🕒 ${e.hora}</span>
        <span>📍 ${e.lugar}</span>
      </div>
    </div>
  </article>
`).join('');
