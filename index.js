/* Nav reveal: hidden over the hero, slides in once the dark body starts. */
const scroller = document.querySelector(".parallax-wrapper");
const nav = document.querySelector(".site-nav");
const hero = scroller.querySelector(".parallax-group.hero");
const threshold = hero?.offsetHeight ?? window.innerHeight;

const update = () =>
    nav.classList.toggle("is-visible", scroller.scrollTop > threshold * 0.9);

scroller.addEventListener("scroll", update, { passive: true });
update();
