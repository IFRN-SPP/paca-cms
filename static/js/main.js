"use strict";

if (document.body.classList.contains("index")) {
  document.addEventListener("scroll", () => {
    if(window.scrollY > 50) {
      document.body.classList.remove("index"); 
    } else {
      document.body.classList.add("index"); 
    }
  });
}
