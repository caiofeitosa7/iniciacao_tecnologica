let sidebar = document.querySelector(".sidebar");
let btnMenu = document.querySelector("#btnMenu");
let nomeLogo = document.getElementById("logo-name");
let menuLateral = document.getElementsByClassName("nav-list")[0];

menuLateral.style.display = "none";
nomeLogo.style.display = "none";

btnMenu.addEventListener("click", ()=>{
    sidebar.classList.toggle("open");
    menuBtnChange();
});

function menuBtnChange() {
    if(sidebar.classList.contains("open")){
        menuLateral.style.display = "block";
        nomeLogo.style.display = "block";
        sidebar.style.left = "0";
    } else {
        menuLateral.style.display = "none";
        nomeLogo.style.display = "none";
        sidebar.style.left = "-28px";
    }
}