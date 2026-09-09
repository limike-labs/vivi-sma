
// ---------------- MOCK DATA (datos ficticios de demostración) ----------------

const categorias = [
  {icon:'🍝', nombre:'Gastronomía', desc:'Restaurantes, cafés, cervecerías y delivery.'},
  {icon:'🛏️', nombre:'Alojamiento', desc:'Hoteles, cabañas, departamentos y camping.'},
  {icon:'🏔️', nombre:'Turismo', desc:'Excursiones, trekking, pesca y cabalgatas.'},
  {icon:'🛍️', nombre:'Comercios', desc:'Ropa, artesanías y productos regionales.'},
  {icon:'🔧', nombre:'Servicios', desc:'Electricistas, plomeros, mecánicos y más.'},
  {icon:'💆', nombre:'Salud y bienestar', desc:'Farmacias, gimnasios y centros de salud.'},
  {icon:'🚗', nombre:'Transporte', desc:'Remises y alquiler de vehículos.'},
  {icon:'🎉', nombre:'Eventos', desc:'Shows, ferias y actividades locales.'},
];

const negocios = [
  {nombre:'La Casa del Ahumado', cat:'Gastronomía', loc:'Villegas 320', tags:['Trucha','Almuerzo'], destacado:true, img:'assets/images/logo-casa-del-ahumado.jpg'},
  {nombre:'Refugio Quila', cat:'Alojamiento', loc:'Av. Costanera', tags:['Vista al lago','Cabañas'], destacado:false, img:'assets/images/logo-refugio-quila.jpg'},
  {nombre:'Andes Bike Rental', cat:'Turismo', loc:'San Martín 540', tags:['Bicis','Excursiones'], destacado:false, img:'assets/images/logo-andes-bike-rental.jpg'},
  {nombre:'Cervecería del Bosque', cat:'Gastronomía', loc:'Elordi 120', tags:['Cerveza artesanal'], destacado:true, img:'assets/images/logo-cerveceria-del-bosque.jpg'},
  {nombre:'Mercado Regional Patagonia', cat:'Comercios', loc:'Belgrano 88', tags:['Productos regionales'], destacado:false, img:'assets/images/logo-mercado-regional-patagonia.jpg'},
  {nombre:'Estudio Wellness Andes', cat:'Salud y bienestar', loc:'Perito Moreno 210', tags:['Yoga','Spa'], destacado:false, img:'assets/images/logo-estudio-wellness-andes.jpg'},
];

const destacados = [
  {nombre:'La Casa del Ahumado', cat:'Gastronomía', loc:'Villegas 320', tags:['Trucha ahumada','Reservas'], img:'assets/images/logo-casa-del-ahumado.jpg'},
  {nombre:'Cervecería del Bosque', cat:'Gastronomía', loc:'Elordi 120', tags:['Artesanal','Música en vivo'], img:'assets/images/logo-cerveceria-del-bosque.jpg'},
  {nombre:'Cabañas Lago Azul', cat:'Alojamiento', loc:'Ruta 40 km 3', tags:['Pet friendly','Chimenea'], img:'assets/images/logo-cabanas-lago-azul.jpg'},
  {nombre:'Sabores del Cerro', cat:'Gastronomía', loc:'Coronel Díaz 45', tags:['Cocina de autor'], img:'assets/images/logo-sabores-del-cerro.jpg'},
];

const promos = [
  {neg:'Cervecería del Bosque', promo:'2x1 en pintas los martes', vig:'Vence en 4 días', img:'assets/images/logo-cerveceria-del-bosque.jpg'},
  {neg:'Andes Bike Rental', promo:'20% off en alquiler por medio día', vig:'Vence en 9 días', img:'assets/images/logo-andes-bike-rental.jpg'},
  {neg:'Estudio Wellness Andes', promo:'Primera clase de yoga sin cargo', vig:'Todo el mes', img:'assets/images/logo-estudio-wellness-andes.jpg'},
];

const eventos = [
  {dia:'12', mes:'Sep', nombre:'Feria de artesanos del bosque', hora:'11:00 – 20:00', lugar:'Plaza San Martín', cat:'Feria'},
  {dia:'18', mes:'Sep', nombre:'Noche de música en vivo', hora:'21:00', lugar:'Cervecería del Bosque', cat:'Show'},
  {dia:'21', mes:'Sep', nombre:'Trail running Cerro Chapelco', hora:'09:00', lugar:'Base del cerro', cat:'Deporte'},
  {dia:'27', mes:'Sep', nombre:'Mercado de productores locales', hora:'10:00 – 18:00', lugar:'Costanera', cat:'Feria'},
];
