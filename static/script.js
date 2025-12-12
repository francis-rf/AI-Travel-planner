// State management
const state = {
  interests: [],
  isGenerating: false,
};

// DOM Elements
const form = document.getElementById("itinerary-form");
const cityInput = document.getElementById("city");
const interestsInput = document.getElementById("interests-input");
const interestsTags = document.getElementById("interests-tags");
const generateBtn = document.getElementById("generate-btn");
const resultsSection = document.getElementById("results-section");
const errorSection = document.getElementById("error-section");
const inputSection = document.querySelector(".input-section");
const resultCity = document.getElementById("result-city");
const resultInterests = document.getElementById("result-interests");
const itineraryContent = document.getElementById("itinerary-content");
const errorMessage = document.getElementById("error-message");
const newPlanBtn = document.getElementById("new-plan-btn");
const retryBtn = document.getElementById("retry-btn");

// Initialize
document.addEventListener("DOMContentLoaded", () => {
  setupEventListeners();
});

function setupEventListeners() {
  // Form submission
  form.addEventListener("submit", handleFormSubmit);

  // Interests input
  interestsInput.addEventListener("keydown", handleInterestInput);

  // New plan button
  newPlanBtn.addEventListener("click", resetForm);

  // Retry button
  retryBtn.addEventListener("click", hideError);
}

// Handle interest tag input
function handleInterestInput(e) {
  if (e.key === "Enter") {
    e.preventDefault();
    const interest = interestsInput.value.trim();

    if (interest && !state.interests.includes(interest.toLowerCase())) {
      addInterest(interest);
      interestsInput.value = "";
    }
  }
}

// Add interest tag
function addInterest(interest) {
  state.interests.push(interest.toLowerCase());
  renderInterests();
}

// Remove interest tag
function removeInterest(interest) {
  state.interests = state.interests.filter((i) => i !== interest);
  renderInterests();
}

// Render interest tags
function renderInterests() {
  interestsTags.innerHTML = "";

  state.interests.forEach((interest) => {
    const tag = document.createElement("div");
    tag.className = "interest-tag";
    tag.innerHTML = `
            <span>${interest}</span>
            <button type="button" class="tag-remove" onclick="removeInterestTag('${interest}')">×</button>
        `;
    interestsTags.appendChild(tag);
  });
}

// Global function for removing tags (called from HTML)
window.removeInterestTag = function (interest) {
  removeInterest(interest);
};

// Handle form submission
async function handleFormSubmit(e) {
  e.preventDefault();

  const city = cityInput.value.trim();

  // Validation
  if (!city) {
    showError("Please enter a city name");
    return;
  }

  if (state.interests.length === 0) {
    showError("Please add at least one interest");
    return;
  }

  // Generate itinerary
  await generateItinerary(city, state.interests);
}

// Generate itinerary via API
async function generateItinerary(city, interests) {
  if (state.isGenerating) return;

  state.isGenerating = true;
  setLoadingState(true);
  hideError();

  try {
    const response = await fetch("/api/generate-itinerary", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        city: city,
        interests: interests,
      }),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail || "Failed to generate itinerary");
    }

    const data = await response.json();
    displayResults(data);
  } catch (error) {
    console.error("Error:", error);
    showError(
      error.message || "Failed to generate itinerary. Please try again."
    );
  } finally {
    state.isGenerating = false;
    setLoadingState(false);
  }
}

// Set loading state
function setLoadingState(isLoading) {
  if (isLoading) {
    generateBtn.classList.add("loading");
    generateBtn.disabled = true;
  } else {
    generateBtn.classList.remove("loading");
    generateBtn.disabled = false;
  }
}

// Display results
function displayResults(data) {
  // Hide input section and error
  inputSection.style.display = "none";
  errorSection.style.display = "none";

  // Populate results
  resultCity.textContent = data.city;
  resultInterests.textContent = data.interests.join(", ");

  // Convert markdown-style formatting to HTML
  const formattedItinerary = formatItinerary(data.itinerary);
  itineraryContent.innerHTML = formattedItinerary;

  // Show results
  resultsSection.style.display = "block";

  // Scroll to results
  resultsSection.scrollIntoView({ behavior: "smooth", block: "start" });
}

// Format itinerary text (simple markdown to HTML)
function formatItinerary(text) {
  let html = text;

  // Headers (### to h3)
  html = html.replace(/###\s+(.+)/g, "<h3>$1</h3>");

  // Bold (**text** to <strong>)
  html = html.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");

  // Italic (*text* to <em>)
  html = html.replace(/\*(.+?)\*/g, "<em>$1</em>");

  // Line breaks
  html = html.replace(/\n\n/g, "</p><p>");
  html = html.replace(/\n/g, "<br>");

  // Wrap in paragraphs
  html = "<p>" + html + "</p>";

  // Clean up empty paragraphs
  html = html.replace(/<p><\/p>/g, "");
  html = html.replace(/<p><br><\/p>/g, "");

  return html;
}

// Show error
function showError(message) {
  errorMessage.textContent = message;
  errorSection.style.display = "block";
  inputSection.style.display = "block";
  resultsSection.style.display = "none";

  // Scroll to error
  errorSection.scrollIntoView({ behavior: "smooth", block: "center" });
}

// Hide error
function hideError() {
  errorSection.style.display = "none";
}

// Reset form
function resetForm() {
  // Clear form
  cityInput.value = "";
  interestsInput.value = "";
  state.interests = [];
  renderInterests();

  // Show input section
  inputSection.style.display = "block";
  resultsSection.style.display = "none";
  errorSection.style.display = "none";

  // Scroll to top
  window.scrollTo({ top: 0, behavior: "smooth" });

  // Focus on city input
  setTimeout(() => cityInput.focus(), 300);
}

// Add some visual feedback on input focus
cityInput.addEventListener("focus", () => {
  cityInput.parentElement.style.transform = "scale(1.01)";
});

cityInput.addEventListener("blur", () => {
  cityInput.parentElement.style.transform = "scale(1)";
});

interestsInput.addEventListener("focus", () => {
  interestsInput.parentElement.parentElement.style.transform = "scale(1.01)";
});

interestsInput.addEventListener("blur", () => {
  interestsInput.parentElement.parentElement.style.transform = "scale(1)";
});
