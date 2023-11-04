const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const btnPopup = document.querySelector('.btnLogin-popup');
const iconClose = document.querySelector('.icon-close');
const hamburguer = document.querySelector('.hamburguer');
const nav = document.querySelector('.navigation');

hamburguer.addEventListener('click', () => nav.classList.toggle('active'));

registerLink.addEventListener('click', () => {
    wrapper.classList.add('active');
});

loginLink.addEventListener('click', () => {
    wrapper.classList.remove('active');
});

btnPopup.addEventListener('click', () => {
    wrapper.classList.add('active-popup');
    wrapper.classList.remove('desativado');

});

iconClose.addEventListener('click', () => {
    wrapper.classList.remove('active-popup');
    wrapper.classList.add('desativado');

});


