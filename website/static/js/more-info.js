// Function to fetch data for a specific university and insert it into the HTML
function fetchUniversityDataAndInsertIntoHTML() {
    // Get the university name from the URL
    const urlParams = new URLSearchParams(window.location.search);
    const universityName = urlParams.get('university');
    console.log('University:', universityName);
  
    // Fetch data for this university
    fetch(`/university/data?university=${encodeURIComponent(universityName)}`)
      .then(response => response.json())
      .then(data => {
        const universityData = data.find(item => item.university_name === universityName);

        // Insert data into the HTML
        document.querySelector('#university-name').textContent = universityData.university_name;
        document.querySelector('#university-description').textContent = universityData.university_description;
        document.querySelector('#website').textContent = universityData.website;
        console.log(universityData.website);
        document.querySelector('#ranking').textContent = universityData.ranking;
        document.querySelector('#requirements').textContent = universityData.requirements;
        console.log(universityData.requirements);
        document.querySelector('#korean-track').textContent = universityData.korean_track;
        console.log(universityData.korean_track);
        document.querySelector('#english-track').textContent = universityData.english_track;
        console.log(universityData.english_track);
        document.querySelector('#fall-intake').textContent = universityData.fall_intake;
        document.querySelector('#spring-intake').textContent = universityData.spring_intake;
        document.querySelector('#application-fee').textContent = universityData.application_fee;
        document.querySelector('#tuition-fee').textContent = universityData.tuition_fee;
        document.querySelector('#application-link').textContent = universityData.application_link;
        console.log(universityData.application_link);
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }
  
  // Wait until the HTML document is fully loaded before fetching the data
  document.addEventListener('DOMContentLoaded', fetchUniversityDataAndInsertIntoHTML);