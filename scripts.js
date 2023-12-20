document.addEventListener('DOMContentLoaded', function () {
	const carousel = document.querySelector('[data-carousel="static"]');
	const prevButton = document.querySelector('[data-carousel-prev]');
	const nextButton = document.querySelector('[data-carousel-next]');
	const items = document.querySelectorAll('[data-carousel-item]');
	let currentIndex = 0;

	// Function to print next element in the carousel
	function showNextItem() {
		items[currentIndex].classList.remove('duration-700', 'ease-in-out', 'hidden');
		currentIndex = (currentIndex + 1) % items.length;
		items[currentIndex].classList.add('duration-700', 'ease-in-out');
		items[currentIndex].classList.remove('hidden');
	}

	// Function to print previous element in the carousel
    function showPrevItem() {
        // Update currentIndex before showing the previous item
        currentIndex--;
        if (currentIndex < 0) {
            currentIndex += items.length;
        }

        items[currentIndex].classList.remove('duration-700', 'ease-in-out', 'hidden');
        items[currentIndex].classList.add('duration-700', 'ease-in-out');
        items[currentIndex].classList.remove('hidden');
    }

	// Écouteurs d'événements pour les boutons de contrôle
	prevButton.addEventListener('click', showPrevItem);
	nextButton.addEventListener('click', showNextItem);
});
