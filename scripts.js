document.addEventListener('DOMContentLoaded', function () {
	/* Carousel */
	// define the elements
	const carousel = document.getElementById('carousel');
	const prevButton = document.getElementById('prev');
	const nextButton = document.getElementById('next');

	let currentIndex = 0;

	function updateCarousel() {
	  //get the width of the element with offsetWidth
	  const itemWidth = carousel.querySelector('.carousel-item').offsetWidth;
	  // moves the carousel
	  carousel.style.transform = `translateX(${-currentIndex * itemWidth}px)`;
	}

	function prevSlide() {
	  if (window.innerWidth > 1024) {
	  	if (currentIndex > 0) {
			currentIndex--;
	  	} else {
			currentIndex = carousel.children.length - 4;
	  	}
	  	updateCarousel();
	  } else if (window.innerWidth <= 1024 && window.innerWidth > 627) {
		if (currentIndex > 0) {
			currentIndex--;
	  	} else {
			currentIndex = carousel.children.length - 2;
	  	}
	  	updateCarousel();
	  } else {
		if (currentIndex > 0) {
			currentIndex--;
	  	} else {
			currentIndex = carousel.children.length - 1;
	  	}
	  	updateCarousel();
	  }
	}

	function nextSlide() {
	  if (window.innerWidth > 1024) {
	  	if (currentIndex < carousel.children.length - 4) {
			currentIndex++;
	  	} else {
			currentIndex = 0;
	  	}
	  	updateCarousel();
	  } else if (window.innerWidth <= 1024 && window.innerWidth > 627) {
		if (currentIndex < carousel.children.length - 2) {
			currentIndex++;
	  	} else {
			currentIndex = 0;
	  	}
	  	updateCarousel();
	  } else {
		if (currentIndex < carousel.children.length - 1) {
			currentIndex++;
	  	} else {
			currentIndex = 0;
	  	}
	  	updateCarousel();
	  }
	}

	prevButton.addEventListener('click', prevSlide);
	nextButton.addEventListener('click', nextSlide);

	 // Detecting mobile view using media query
	 const isMobileView = window.matchMedia('(max-width: 768px)').matches;

	 if (isMobileView) {
	   // Update carousel behavior for mobile view
	   // Display only one image at a time
	   carousel.style.transform = 'none';

	   // Disable navigation buttons
	   prevButton.classList.add('disabled');
	   nextButton.classList.add('disabled');
	 }

	 window.addEventListener('resize', function () {
	   const newIsMobileView = window.matchMedia('(max-width: 768px)').matches;
	   if (isMobileView !== newIsMobileView) {
		 isMobileView = newIsMobileView;
		 if (isMobileView) {
		   // Update carousel behavior for mobile view
		   // Display only one image at a time
		   carousel.style.transform = 'none';

		   // Disable navigation buttons
		   prevButton.classList.add('disabled');
		   nextButton.classList.add('disabled');
		 } else {
		   // Update carousel behavior for desktop view
		   // Allow navigation buttons
		   prevButton.classList.remove('disabled');
		   nextButton.classList.remove('disabled');
		 }
	   }
	 });

	 // Initial carousel update
	 updateCarousel(); // Appel initial pour mettre à jour la disposition

	window.addEventListener('resize', updateCarousel);
	updateCarousel(); // Appel initial pour mettre à jour la disposition


	/* top button */
	var toTopButton = document.getElementById("to-top-button");

	// When the user scrolls down 200px from the top of the document, show the button
	window.onscroll = function () {
	    if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
	        toTopButton.classList.remove("hidden");
	    } else {
	        toTopButton.classList.add("hidden");
	    }
	}
	// When the user clicks on the button, scroll to the top of the document
	function goToTop() {
	    window.scrollTo({ top: 0, behavior: 'smooth' });
	}
	toTopButton.addEventListener('click', goToTop);

	// anim the avatar
	anime({
	  targets: ".avatar",
	  translateY: [-50, 0],
	  opacity: [0, 1],
	  duration: 2000,
	  easing: "easeOutQuad",
	});
	// Anime "lucie leroty" and "web developpeuse"
	anime({
	  targets: ".name-title",
	  translateY: [50, 0],
	  opacity: [0, 1],
	  duration: 2000,
	  delay: 500, // Délai de 500ms après l'animation de l'avatar
	  easing: "easeOutQuad",
	});

	// Word list to print
    const words = ["Curieuse", "Empathe", "A l'écoute", "Créative", "Consciencieuse", "Autodidacte", "Travail en équipe", "Aime apprendre", "Autonomie", "Respect des deadlines", "Perséverante", "Rigoureuse"];

    // function to create and animate the words
    function createAnimatedWords() {
      const container = document.getElementById("cloud-container");

      words.forEach(word => {
        const span = document.createElement("span");
        span.className = "word";
        span.innerText = word;
        container.appendChild(span);



        anime({
          targets: span,
          translateX: () => anime.random(-250, 220),
          translateY: () => anime.random(-220, 0),
          rotate: () => anime.random(-60, 60),
          duration: () => anime.random(1200, 2000),
          easing: "easeInOutBack",
          loop: true
        });
      });
    }

    // call the function when the page is loaded
    window.onload = createAnimatedWords;


});
