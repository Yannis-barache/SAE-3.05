document.addEventListener('DOMContentLoaded', function() {

    const bouton_agrandir2 = document.getElementById("btn-agrandir2");
    const div_img_agrandir2 = document.getElementById("div-image-agrandir2");
    const bouton_fermeture2 = document.getElementById("bouton-fermeture2");
    const html = document.querySelector("html");
    const header = document.querySelector("header");

    bouton_agrandir2.addEventListener('click', () => {
        div_img_agrandir2.style.display = "flex";
        html.classList.add("active");
        header.style.zIndex = "0";
    });

    bouton_fermeture2.addEventListener('click', () => {
        div_img_agrandir2.style.display = "none";
        html.classList.remove("active");
        header.style.zIndex = "1";
        });
});