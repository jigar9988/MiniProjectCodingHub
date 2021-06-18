let bar = document.querySelector('.bar');
let left = document.querySelector('.left');
let right = document.querySelector('.right');
let head = document.querySelector('#head');
// let bar = document.querySelector('.bar');

bar.addEventListener('click',()=>{
    head.classList.toggle('h-nav');
    right.classList.toggle('visible');
    left.classList.toggle('visible');
})