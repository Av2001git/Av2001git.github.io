let menue = document.querySelector('#meniu-bar');
let navbar = document.querySelector('.navbar');

window.addEventListener('scroll',() =>{
    let cont = document.querySelector('.contenyer');
    cont.classList.toggle("sticky",window.scrollY > 0);
});

menue.addEventListener('click',()=>{
    menue.classList.toggle('fa-time');
    navbar.classList.toggle('active')
});


// let img = document.querySelector('#img');
// let btn1 = document.querySelector('#btn1');
// let btn2 = document.querySelector('#btn2');
// let btn3 = document.querySelector('#btn3');

// btn1.addEventListener('click',() =>{
//     img.src="/static/img/jj18.jpg"
// })
// btn2.addEventListener('click',() =>{
//     img.src="/static/img/j21.jpg"
// })
// btn3.addEventListener('click',() =>{
//     img.src="/static/img/jj19.jpg"
// })
