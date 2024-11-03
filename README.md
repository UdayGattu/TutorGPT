# TutorBot: AI-Powered Physics Tutor

TutorBot is an AI-powered interactive chatbot designed to assist users in learning physics concepts. It provides step-by-step problem solving, real-world connections, exam preparation, and can generate visual aids using OpenAI's DALL-E API. The bot is configured to simulate a personalized tutoring experience, engaging users through thoughtful responses and prompts.

## Project Structure

TutorBot/ ├── app/ │ └── main.py # FastAPI backend server with core bot functions ├── frontend/ │ ├── static/ │ │ ├── style.css # Styling for chat interface │ │ └── script.js # Frontend JavaScript for chat interactions │ └── templates/ │ └── index.html # Main HTML file for chatbot interface ├── generated_images/ # Folder to store generated images from DALL-E ├── .env # Environment file for API keys ├── .gitignore # Specifies files and directories to ignore in Git └── README.md # Project README file


## Features

TutorBot includes the following core functionalities:

1. **Subject Q&A Module**: Provides progressively deeper explanations on physics questions.
2. **Step-by-Step Problem Solving**: Guides users through complex problems with hints.
3. **Real-World Connections**: Relates physics concepts to real-life situations.
4. **Critical Thinking Prompts**: Engages users with reflective questions.
5. **Exam Preparation and Review**: Offers quizzes and immediate feedback.
6. **Basic Visual Aids Creation**: Generates simple physics visuals using DALL-E.

## Getting Started

### Prerequisites

- Python 3.7+
- [OpenAI API Key](https://platform.openai.com/account/api-keys)
- Install the required Python libraries by running:

    ```bash
    pip install -r requirements.txt
    ```

### Setting Up

1. Clone the repository and navigate to the project directory:

    ```bash
    git clone <repository_url>
    cd TutorBot
    ```

2. Set up a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your OpenAI API key:

    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    ```

5. Start the FastAPI server:

    ```bash
    uvicorn app.main:app --reload
    ```

6. Open a browser and go to `http://127.0.0.1:8000` to access the chatbot.

## Usage

- **Ask Questions**: Type in questions related to physics, and TutorBot will respond with layered explanations.
- **Problem Solving**: Request step-by-step guidance on solving physics problems.
- **Visual Aids**: Ask TutorBot to generate visuals (e.g., “Create a diagram of Newton’s Third Law”) to receive images generated through DALL-E.
- **Exam Preparation**: Use TutorBot to practice with quizzes and get immediate feedback.

## Core Bot Functions

TutorBot's core functionalities are implemented using prompt engineering and include:

- **Q&A Module**: Provides multi-layered explanations on physics topics.
- **Problem Solving**: Offers step-by-step guidance with hints.
- **Real-World Connections**: Explains physics concepts in real-life contexts.
- **Critical Thinking Prompts**: Engages users in reflective questioning.
- **Exam Preparation and Review**: Delivers quizzes and feedback for assessment preparation.
- **Visual Aids Creation**: Uses DALL-E to generate simple educational visuals.

## Files

- **app/main.py**: Contains the FastAPI server and API endpoints for chat and image generation.
- **frontend/templates/index.html**: The HTML file for the chatbot interface.
- **frontend/static/style.css**: Contains the CSS for styling the chat interface.
- **frontend/static/script.js**: Contains JavaScript for handling chat interactions and displaying responses.

## Future Improvements

Potential enhancements include:

- **Enhanced Memory**: Add long-term memory to allow the bot to remember user interactions.
- **Advanced Visualizations**: Enable more complex diagrams and graphs.
- **Support for Additional Subjects**: Expand TutorBot to support other educational fields.

## License

This project is licensed under the MIT License.

## Acknowledgments

- This project uses the OpenAI GPT-4-turbo model for conversational responses and DALL-E for image generation.
