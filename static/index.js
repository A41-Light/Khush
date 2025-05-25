// Open the modal
function openModal() {
  document.getElementById("modal").style.display = "block";
}

// Close the modal
function closeModal() {
  document.getElementById("modal").style.display = "none";
}

// Email validation using regex
function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

// Close modal when clicking outside it
window.onclick = function(event) {
  let modal = document.getElementById("modal");
  if (event.target === modal) {
    modal.style.display = "none";
  }
};

// Form submission
document.getElementById("contact-form").addEventListener("submit", function(e) {
  e.preventDefault();

  let name = document.getElementById("name").value.trim();
  let email = document.getElementById("email").value.trim();
  let message = document.getElementById("message").value.trim();
  let status = document.getElementById("form-status");

  // Clear previous messages
  status.style.color = "red";
  status.textContent = "";

  // Frontend validation
  if (!name || !email) {
    status.textContent = "Please fill out all fields.";
    return;
  }

  if (!isValidEmail(email)) {
    status.textContent = "Please enter a valid email address.";
    return;
  }

  // Show submission in progress
  status.style.color = "green";
  status.textContent = "Submitting...";

  // Example: submit to backend (change URL if needed)
   fetch("/submit", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ name, email, message })
  })
  .then(response => response.json())
  .then(data => {
    status.style.color = "green";
    status.textContent = data.message;
    document.getElementById("contact-form").reset();
  })
  .catch(err => {
    status.style.color = "red";
    status.textContent = "Server error. Try again later.";
    console.error("Error:", err);
  });
});
