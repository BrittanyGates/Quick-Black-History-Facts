function updateWindow() {
  fetch("/chosen-fact")
    .then(response => response.json()) // Parse the JSON response
    .then(data => {
      // Update the page with the data from the server
      document.querySelector(".fact").textContent = data.value;
    })
    .catch(error => {
      console.error("Error fetching data:", error);
    });
};

setInterval(updateWindow, 10000);