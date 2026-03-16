document.addEventListener("DOMContentLoaded", () => {
	const header = document.querySelector(".header");
	const footer = document.querySelector(".pie");

	header.innerHTML = createHeader();
	footer.innerHTML = createFooter();
});

function createHeader() {
	return `
	<nav class="navbar">
		<div class="navbar-brand">
			<a href="/index.html"><img class="logo" src="../img/logo_2.png" alt="Logo Patitas Felices"></a>
			<span class="brand_logo">Patitas Felices</span>
		</div>
		<input type="checkbox" id="menu-toggle" class="menu-toggle" />
		<label for="menu-toggle" class="menu-icon">
			<i class="bx bx-menu"></i>
			<i class="bx bx-x"></i>
		</label>
		<div class="navbar-links">
			<a href="/pages/cards.html">Mascotas</a>
			<a href="/pages/nosotros.html">Nosotros</a>
			<a href="/pages/organizaciones.html">Organizaciones</a>
			<a href="/pages/contacto.html">Contacto</a>
			<a href="/pages/dashboard.html">Dashboard</a>
			<a href="/pages/login.html" class="navbar-login-btn"><i class="bx bxs-user"></i> Iniciar sesión</a>
		</div>
	</nav>
	`;
}

function createFooter() {
	let footerCode = "";

	footerCode = `<div class="contenerdorPie">
		<div class="img_foot"> <img src="../img/logo_2.png" alt="Logo Patitas Felices" style="width: 60px; height: 60px;"/></div>
	<div class="list">
		<a href="/pages/construccion.html" class="item-Txt">Soy una organización.</a>
		<a href="/pages/nosotros.html" class="item-Txt">Trabaja con nosotros!</a>
		<a href="/pages/construccion.html" class="item-Txt">Términos y condiciones.</a>
	</div>

	<div class="redesSociales">
		<a href="#" class="social-link"><i class="bx bxl-instagram"></i></a>
		<a href="#" class="social-link"><i class="bx bxl-twitter"></i></a>
		<a href="#" class="social-link"><i class="bx bxl-whatsapp"></i></a>
		<a href="#" class="social-link"><i class="bx bxl-facebook"></i></a>
	</div>

	<div class="contacto">
		<h3 class="contact_foot">Contactanos!</h3>
		<form action="" class="formContacto"
			><input
				class="inputContact"
				type="text"
				placeholder="Ingresa tu Mail!" />
			<button class="enviar" type="submit"
				><i class="bx bx-send" id="enviar"></i></button
		></form>
	</div>
</div>
<div class="copyright">&copy;Patitas Felices 2023. Todos los derechos reservados</div>`;

	return footerCode;
}
