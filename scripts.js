document.addEventListener('DOMContentLoaded', function () {
	/* Carousel */
	const carousel = document.getElementById('carousel');
	const prevButton = document.getElementById('prev');
	const nextButton = document.getElementById('next');

	let currentIndex = 0;

	function updateCarousel() {
	  const itemWidth = carousel.querySelector('.carousel-item').offsetWidth;
	  carousel.style.transform = `translateX(${-currentIndex * itemWidth}px)`;
	}

	function prevSlide() {
	  if (currentIndex > 0) {
		currentIndex--;
	  } else {
		currentIndex = carousel.children.length - 4;
	  }
	  updateCarousel();
	}

	function nextSlide() {
	  if (currentIndex < carousel.children.length - 4) {
		currentIndex++;
	  } else {
		currentIndex = 0;
	  }
	  updateCarousel();
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



});
