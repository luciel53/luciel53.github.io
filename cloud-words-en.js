document.addEventListener('DOMContentLoaded', function () {
  // Word list to print
  const words = ["Curious", "Empathetic", "Good listener", "Creative", "Conscientious", "Self-taught", "Team player", "Likes to learn", "Autonomous", "Meets deadlines", "Persevering", "Thorough"];

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

