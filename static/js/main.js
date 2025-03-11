"use strict";

document.addEventListener("scroll", () => {
  const navbar = document.querySelector("#site-nav");
  if(window.scrollY > 50) {
    navbar.classList.add("navbar-solid"); 
  } else {
    navbar.classList.remove("navbar-solid"); 
  }
});
