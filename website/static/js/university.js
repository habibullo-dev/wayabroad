let currentIndex = 0;
let isLoadMoreEventAttached = false;

// Function to create a card
function createCard(card) {
  let imagePath = `./static/img/university/${card.university_name}.png`;
  let logoPath = `./static/img/university/${card.university_name}_logo.png`;
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
              <p class="card-text brief-info">${card.university_description}</p>
          </div>
          <div class="card-footer">
          <button type="button" class="btn btn-primary mb-3 loadUnibtn" data-university="${
            card.university_name
          }" data-mdb-modal-init data-mdb-target="#modal-${card.university_name.replace(
    /\s+/g,
    ""
  )}">Learn More</button>
          </div>
      </div>
  </div>

  <!-- Modal -->
<div class="modal top fade uniModal" id="modal-${card.university_name.replace(
    /\s+/g,
    ""
  )}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true" data-mdb-backdrop="true" data-mdb-keyboard="true">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">       
            <ul class="nav nav-tabs">
            <li class="nav-item">
                <a class="nav-link active" data-mdb-toggle="tab" href="#overview-${card.university_name.replace(
                  /\s+/g,
                  ""
                )}">Overview</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" data-mdb-toggle="tab" href="#korean-${card.university_name.replace(
                  /\s+/g,
                  ""
                )}">Korean Programs</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" data-mdb-toggle="tab" href="#english-${card.university_name.replace(
                  /\s+/g,
                  ""
                )}">English Programs</a>
            </li>
        </ul>
                <button type="button" class="btn-close" data-mdb-dismiss="modal" aria-label="Close"></button>
            </div>
                
            </div>
            <div class="modal-body">
    <div class="tab-content">
        <div class="tab-pane active" id="overview-${card.university_name.replace(
          /\s+/g,
          ""
        )}">
            <img src="${logoPath}" onerror="this.onerror=null; this.src='${fallbackImagePath}';" class="logo-img fixed-height" alt="Logo of ${
    card.university_name
  }">
            <h5 class="university-name">${card.university_name}</h5>
            <p class="university-description">${card.university_description}</p>
            <h5 class"university-ranking">QS Ranking: ${card.ranking}</h5>
            <br>
            <h5 class="requirements">Requirements:</h5>
            
            <ul class="university-requirements">
                ${
                  Array.isArray(card.requirements)
                    ? card.requirements
                        .map((requirement) => `<li>${requirement.trim()}</li>`)
                        .join("")
                    : card.requirements
                        .split(/\r?\n/)
                        .map((requirement) => `<li>${requirement.trim()}</li>`)
                        .join("")
                }
            </ul>

            <h5 class="university-website">Website:</h5>
            <p class="website"><a href="${card.website}" target="_blank">${
    card.website
  }</a></p>

            <h5 class="application-period">Application Period:</h5>
            <ul class="intake-period">
                <li><strong>Fall Intake:</strong></li>
                ${card.fall_intake
                  .split(";")
                  .map((intake) => `<li>${intake.trim()}</li>`)
                  .join("")}
                <li><strong>Spring Intake:</strong></li>
                ${card.spring_intake
                  .split(";")
                  .map((intake) => `<li>${intake.trim()}</li>`)
                  .join("")}
            </ul>

            <h5 class="tuition-fees">Tuition Fees:</h5>
            <p class="fees">${card.tuition_fee}</p>

            <h5 class="application-link">Application Link:</h5>
            <p class="link"><a href="${
              card.application_link
            }" target="_blank">${card.application_link}</a></p>

            <h5 class="application-fees">Application Fees:</h5>
            <p class="fees">${card.application_fee}</p>
        </div>
        <div class="tab-pane" id="korean-${card.university_name.replace(
          /\s+/g,
          ""
        )}">
            <div class="korean-programs">
              <!-- Korean programs will be populated here -->
            </div>
        </div>
        <div class="tab-pane" id="english-${card.university_name.replace(
          /\s+/g,
          ""
        )}">
            <div class="english-programs">
              <!-- English programs will be populated here -->
            </div>
        </div>
    </div>
</div>
            </div>
        </div>
  </div>
  <!-- ... -->
`;
}

// Function to fetch data for a specific university and insert it into the HTML
function fetchUniversityDataAndInsertIntoHTML(universityName) {
  console.log(`Fetching data for university: ${universityName}`);

  // Fetch data for this university
  fetch(`/university/data?university=${encodeURIComponent(universityName)}`)
    .then((response) => response.json())
    .then((data) => {
      console.log(`Fetched university data:`, data);

      const universityData = data.find(
        (item) => item.university_name === universityName
      );

      // Get the modal for this university
      const modal = document.querySelector(
        `#modal-${universityName.replace(/\s+/g, "")}`
      );

      // Insert data into the HTML
      modal.querySelector(".university-name").textContent =
        universityData.university_name;
      modal.querySelector(".university-description").textContent =
        universityData.university_description;

      // Fetch and insert Korean and English programs
      fetch(`/majors/data?university=${encodeURIComponent(universityName)}`)
        .then((response) => response.json())
        .then((programData) => {
          programData = programData[0][universityName];
          console.log(`Fetched program data:`, programData);

          const koreanPrograms = modal.querySelector(".korean-programs");
          const englishPrograms = modal.querySelector(".english-programs");

          // Clear existing data
          koreanPrograms.innerHTML = "";
          englishPrograms.innerHTML = "";

          Object.entries(programData).forEach(([trackName, trackData]) => {
            if (trackName.toLowerCase().includes("korean")) {
              Object.entries(trackData).forEach(([collegeName, majors]) => {
                let content = `<h3>${collegeName}</h3>`;
                majors.forEach((major) => {
                  content += `<p>${major}</p>`;
                });
                koreanPrograms.innerHTML += content;
              });
            } else if (trackName.toLowerCase().includes("english")) {
              Object.entries(trackData).forEach(([collegeName, majors]) => {
                let content = `<h3>${collegeName}</h3>`;
                majors.forEach((major) => {
                  content += `<p>${major}</p>`;
                });
                englishPrograms.innerHTML += content;
              });
            }
          });

          console.log(
            `Updated modal content for university: ${universityName}`
          );
        })
        .catch((error) => {
          console.error("Error fetching programs:", error);
        });
    })
    .catch((error) => {
      console.error("Error:", error);
    });
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

  // Initialize modals
  const modals = row.querySelectorAll(".modal");
  modals.forEach((modal) => {
    new mdb.Modal(modal);
  });

  // Attach event listeners to buttons
  const buttons = row.querySelectorAll(".btn");
  buttons.forEach((button) => {
    button.addEventListener("click", () => {
      const universityName = button.getAttribute("data-university");
      if (universityName) {
        const modal = new mdb.Modal(
          document.getElementById(`modal-${universityName.replace(/\s+/g, "")}`)
        );
        modal.show();
      }
    });
  });

  // Attach event listeners to new buttons
  const newButtons = row.querySelectorAll(".loadUnibtn");
  newButtons.forEach((button) => {
    const universityName = button.dataset.university;
    button.addEventListener("click", () => {
      fetchUniversityDataAndInsertIntoHTML(universityName);
    });
  });
}

// Function to fetch data and load cards
function fetchDataAndLoadCards() {
  // Disable "Load More" button
  const loadMoreButton = document.querySelector(".load-more-btn");
  loadMoreButton.disabled = true;

  fetch("/university/data")
    .then((response) => response.json())
    .then((data) => {
      console.log(`Fetched cards data:`, data);

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
