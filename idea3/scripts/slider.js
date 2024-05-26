
let dots = document.getElementsByClassName("dot");
let dotsArea = document.getElementsByClassName("slider__dots")[0];
let slides = document.getElementsByClassName("slide");
let prevBtn = document.getElementsByClassName("sldier__button_next");
let nextBtn = document.getElementsByClassName("sldier__button_prev");
let slideIndex = 1;

showSlides(slideIndex)

function showSlides (n) {
	
	console.log("click!")
	if (n < 1) {
		slideIndex = slides.length
	} else if ( n > slides.length) {
		slideIndex = 1;
	}

	for (let i = 0; i < slides.length; i++) {
		slides[i].style.display = 'none';
	}
	for (let i = 0; i < dots.length; i++) {
		dots[i].classList.remove('active');
	}

	slides[slideIndex - 1].style.display = 'block';
	dots[slideIndex - 1].classList.add('active');
}

function plusSlides (n) {
	showSlides(slideIndex += n);
}

function currentSlide (n) {
	showSlides(slideIndex = n)
}

prevBtn[0].addEventListener("click", function () {
	plusSlides(-1)
})

nextBtn[0].addEventListener("click", function () {
	plusSlides(1)
})

dotsArea.addEventListener("click", function (e) {
	for (let i = 0; i < dots.length + 1; i++) {
		if (e.target.classList.contains('dot') && e.target == dots[i - 1]) {
			currentSlide(i)
		}
	}
})