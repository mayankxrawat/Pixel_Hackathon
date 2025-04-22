const loginTab = document.getElementById("login-tab");
const signupTab = document.getElementById("signup-tab");
const loginForm = document.getElementById("login-form");
const signupForm = document.getElementById("signup-form");

loginTab.addEventListener("click", () => {
  loginTab.classList.add("active");
  signupTab.classList.remove("active");
  loginForm.classList.add("active");
  signupForm.classList.remove("active");
});

signupTab.addEventListener("click", () => {
  signupTab.classList.add("active");
  loginTab.classList.remove("active");
  signupForm.classList.add("active");
  loginForm.classList.remove("active");
});

// const submitbutton = document.getElementById("submitbtn");

// submitbutton.addEventListener("click", () => {
//     window.location.href="home.html";
// });

function toggleMenu() {
    const nav = document.getElementById("navMenu");
    nav.style.display = nav.style.display === "none" ? "block" : "none";
  }