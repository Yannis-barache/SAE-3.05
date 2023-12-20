document.addEventListener('DOMContentLoaded', function() {

    const bouton_agrandir = document.getElementById("btn-agrandir");
    const div_img_agrandir = document.getElementById("div-image-agrandir");
    const bouton_fermeture = document.getElementById("bouton-fermeture");
    const html = document.querySelector("html");
    const header = document.querySelector("header");

    bouton_agrandir.addEventListener('click', () => {
        div_img_agrandir.style.display = "block";
        html.classList.add("active");
        header.style.zIndex = "0";
    });

    bouton_fermeture.addEventListener('click', () => {
        div_img_agrandir.style.display = "none";
        html.classList.remove("active");
        header.style.zIndex = "1";
        });
});