
// script.js
let isBottleRotated = false;

function rotateBottle() {
    const bottle = document.querySelector('.bottle');
    const liquid = document.querySelector('.liquid');
    const fundo = document.querySelector('body')

    if (!isBottleRotated) {
        bottle.style.transform = 'rotate(-90deg)';
        liquid.style.visibility = 'visible';
        fundo.style.visibility = '100%'
    } else {
        bottle.style.transform = 'rotate(0deg)';
        liquid.style.height = '0';
        fundo.style.backgoundColor = 'white';
    }

    isBottleRotated = !isBottleRotated;
}

// parallax

window.addEventListener('scroll', e => {
    document.body.style.cssText = `--scrollTop: ${this.scrollY}px`
})

// folha


