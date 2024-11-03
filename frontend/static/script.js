const chatBox = document.getElementById('chat-box');
const chatForm = document.getElementById('chat-form');
const messageInput = document.getElementById('message-input');

// Function to display messages in the chat box
function displayMessage(text, sender = 'bot') {
  const messageElement = document.createElement('div');
  messageElement.classList.add('message', sender);
  messageElement.innerText = text;
  chatBox.appendChild(messageElement);
  chatBox.scrollTop = chatBox.scrollHeight;
}

// Function to display images in the chat box
function displayImage(url, sender = 'bot') {
  const imageElement = document.createElement('img');
  imageElement.classList.add('message', sender);
  imageElement.src = url;
  imageElement.alt = "Generated visual";
  imageElement.style.maxWidth = "100%";
  chatBox.appendChild(imageElement);
  chatBox.scrollTop = chatBox.scrollHeight;
}

// Function to show a loading spinner
function showLoading() {
  const loadingElement = document.createElement('div');
  loadingElement.classList.add('loading', 'message', 'bot');
  loadingElement.id = 'loading-spinner';
  chatBox.appendChild(loadingElement);
  chatBox.scrollTop = chatBox.scrollHeight;
}

// Function to hide the loading spinner
function hideLoading() {
  const loadingElement = document.getElementById('loading-spinner');
  if (loadingElement) {
    chatBox.removeChild(loadingElement);
  }
}

// Display initial greeting when the chat loads
function displayGreeting() {
  displayMessage("Hello! I'm TutorBot, your AI-powered physics tutor. Ask me anything related to physics, and I'll do my best to assist!", 'bot');
}

// Handle form submission for text input
chatForm.addEventListener('submit', async (event) => {
  event.preventDefault();

  const message = messageInput.value.trim();
  if (message) {
    displayMessage(message, 'user');
    messageInput.value = '';

    // Show the loading spinner
    showLoading();

    try {
      const response = await fetch("http://127.0.0.1:8000/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams({ message: message })
      });

      const data = await response.json();

      // Hide the loading spinner
      hideLoading();

      if (data.image_url) {
        // Display image if an image URL is returned
        displayMessage(data.reply, 'bot');
        displayImage(data.image_url);
      } else {
        // Display text response
        displayMessage(data.reply, 'bot');
      }

    } catch (error) {
      hideLoading();
      displayMessage("Error: Unable to connect to TutorBot server.", 'bot');
    }
  }
});

// Initialize the chat with a greeting message
displayGreeting();
