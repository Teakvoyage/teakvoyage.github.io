
const body = document.body;
const barNav = document.getElementById('barNav');
const navBar = document.getElementById('navBar');
const navMax = screen.height * 0.1;
const barMax = screen.height * 0.1;
const content = document.getElementById('content');
const diagonal = document.getElementById('diagonal');
const rotate = document.getElementsByClassName('rotate');

function scroll() {
    var scrollPos = body.scrollTop;
    if (scrollPos < navMax) {
        navBar.style = `background-color: rgba(0, 0, 0, ${scrollPos/navMax}); height: ${9 - (scrollPos/navMax)}vh;`;
        barNav.style = `width: ${scrollPos/(barMax)*100}%; top: ${9 - (scrollPos/navMax)}vh; opacity: 1;`
        content.style.marginTop = '50px';
        diagonal.style.transform = 'rotate(-2deg)';
    } else {
        navBar.style = `background-color: rgba(0, 0, 0, ${scrollPos}); height: ${6}vh;`;
        barNav.style = `top: 6vh; width: 100%;`;
    }

    if (scrollPos*1.2 > barMax) {
        barNav.style.opacity = `0`;
        diagonal.style.transform = 'rotate(0deg)';
    }

    if (scrollPos/barMax > 0.75) {
        content.style.marginTop = `-70vh`;
    }
    for (let i = 0; i < rotate.length; i++) {
        rotate[i].style.transform = `rotate(${scrollPos/7}deg)`;
        if (scrollPos > 600) {
            rotate[i].style.height = `1200px`;
            rotate[i].style.width = `1200px`;
            rotate[i].style.transition = '5s';
            rotate[i].style.opacity = '0';
        } else {
            rotate[i].style.height = `100px`;
            rotate[i].style.width = `100px`;
            rotate[i].style.opacity = '1';
            rotate[i].style.transition = '0.1s';
        }
    }

}

