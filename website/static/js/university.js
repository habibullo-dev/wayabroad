let currentIndex = 0;
let isLoadMoreEventAttached = false;

// Function to create a card
// Function to create a card
function createCard(card) {
  let imagePath = `./static/img/university/${card.university_name}.png`;
  let fallbackImagePath = `./static/img/university/default.png`; // Fallback image

  return `
      <div class="col">
          <div class="card h-100 university-card">
          <img src="${imagePath}" onerror="this.onerror=null; this.src='${fallbackImagePath}';" class="card-img-top fixed-height" alt="Image of ${
    card.university_name
  }">
          <div class="card-body">
                  <h5 class="card-title university-name"><i class="fas fa-university"></i> ${
                    card.university_name
                  }</h5>
                  <p class="card-text brief-info">${
                    card.university_description
                  }</p>
              </div>
              <div class="card-footer">
              <a href="more-info?university=${encodeURIComponent(
                card.university_name
              )}" class="btn btn-primary mb-3">Learn More</a>
              </div>
          </div>
      </div>
  `;
}

// Function to load cards
function loadCards(data) {
  let cardsHTML = "";
  data.forEach((card) => {
    cardsHTML += createCard(card);
  });
  const row = document.querySelector(".row-cols-1");
  row.innerHTML += cardsHTML;

  // Add 'loaded' class to cards after a short delay
  setTimeout(() => {
    const cards = row.querySelectorAll(".university-card");
    cards.forEach((card) => {
      card.classList.add("loaded");
    });
  }, 100);
}

// Function to fetch data and load cards
function fetchDataAndLoadCards() {
  // Disable "Load More" button
  const loadMoreButton = document.querySelector(".load-more-btn");
  loadMoreButton.disabled = true;

  fetch("/university/data")
    .then((response) => response.json())
    .then((data) => {
      // Check if there is more data to load
      if (currentIndex >= data.length) {
        loadMoreButton.disabled = true;
        loadMoreButton.innerHTML = "No more data to load";
        return;
      }

      loadCards(data.slice(currentIndex, currentIndex + 6)); // Load next 6 cards
      currentIndex += 6;

      // Enable "Load More" button if there is more data to load
      if (currentIndex < data.length) {
        loadMoreButton.disabled = false;
      }
    })
    .catch((error) => {
      console.error("Error:", error);

      // Enable "Load More" button
      loadMoreButton.disabled = false;
    });
}

// Wait until the HTML document is fully loaded before attaching the event listener
document.addEventListener("DOMContentLoaded", (event) => {
  // Load initial cards
  fetchDataAndLoadCards();

  // Load more cards when "Load More" button is clicked
  document
    .querySelector(".load-more-btn")
    .addEventListener("click", fetchDataAndLoadCards);
});


