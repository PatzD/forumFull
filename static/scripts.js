"use strict";

const aboutModal = document.querySelector(".about-mod");
const postModal = document.querySelector(".post-mod");
const body = document.querySelector(".body");
const buttonCloseAboutMod = document.querySelector(".close-about-modal");
const buttonClosePostMod = document.querySelector(".close-post-modal");
const buttonOpenPost = document.querySelector(".open-new-post");
const buttonOpenAbout = document.querySelector(".open-about-section");

const openPostModal = function () {
	postModal.classList.remove("hidden");
	postModal.classList.add("modal");
	body.classList.add("overlay");
};
const openAboutModal = function () {
	aboutModal.classList.remove("hidden");
	aboutModal.classList.add("modal");
	body.classList.add("overlay");
};
const closeModal = function () {
	const toClose = document.querySelector(".modal");
	toClose.classList.remove("modal");
	toClose.classList.add("hidden");
	body.classList.remove("overlay");
};

buttonOpenPost.addEventListener("click", openPostModal);
buttonOpenAbout.addEventListener("click", openAboutModal);
buttonClosePostMod.addEventListener("click", closeModal);
buttonCloseAboutMod.addEventListener("click", closeModal);
body.addEventListener("click", closeModal);
