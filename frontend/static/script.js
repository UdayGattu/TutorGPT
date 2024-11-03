// Reference to chat box and input field
const chatBox = document.getElementById('chat-box');
const messageInput = document.getElementById('message-input');
const fileUpload = document.getElementById('file-upload');

// Function to display messages
function displayMessage(text, sender = 'bot') {
  const messageElement = document.createElement('div');
  messageElement.classList.add('message', sender);
  messageElement.innerText = text;
  chatBox.appendChild(messageElement);
  chatBox.scrollTop = chatBox.scrollHeight;
}

// Send Message Function
function sendMessage() {
  const message = messageInput.value.trim();
  if (message) {
    displayMessage(message, 'user');
    messageInput.value = '';

    // Simulate a response from TutorBot
    setTimeout(() => {
      displayMessage(`TutorBot received your message: "${message}"`, 'bot');
    }, 1000);
  }
}

// Handle file upload
fileUpload.addEventListener('change', (event) => {
  const file = event.target.files[0];
  if (file) {
    displayMessage(`File uploaded: ${file.name}`, 'user');

    // Simulate a TutorBot response after file upload
    setTimeout(() => {
      displayMessage(`TutorBot is processing the file "${file.name}"`, 'bot');
    }, 1000);
  }
});
