const navItems = document.querySelectorAll(".nav-item");

navItems.forEach((item) => {
  item.addEventListener("click", (event) => {
    if (item.classList.contains("disabled")) {
      event.preventDefault();
    }
  });
});
