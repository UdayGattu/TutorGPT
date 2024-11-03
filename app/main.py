import os
from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import openai
import uuid

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# Define paths for static files and templates
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(os.path.dirname(BASE_DIR), "frontend")
IMAGE_DIR = os.path.join(BASE_DIR, "generated_images")
os.makedirs(IMAGE_DIR, exist_ok=True)

# Mount the static files directory
app.mount("/static", StaticFiles(directory=os.path.join(FRONTEND_DIR, "static")), name="static")
app.mount("/images", StaticFiles(directory=IMAGE_DIR), name="images")

# Serve the HTML file
@app.get("/", response_class=HTMLResponse)
async def serve_html():
    index_path = os.path.join(FRONTEND_DIR, "templates", "index.html")
    with open(index_path, "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

# In-memory storage for conversation history
conversation_history = {}

# Core Bot Functions - Chat Endpoint
@app.post("/api/chat")
async def chat(message: str = Form(...), session_id: str = Form(None)):
    session_id = session_id or str(uuid.uuid4())
    if session_id not in conversation_history:
        conversation_history[session_id] = []

    # Store the user's message in memory
    conversation_history[session_id].append({"role": "user", "content": message})
    user_input = message.lower()

    # Determine if the user requests an image/visual
    if "visual" in user_input or "diagram" in user_input or "illustration" in user_input:
        prompt = f"Create a physics-related illustration or visual for: {message}"
        
        try:
            # Call DALL-E API for image generation
            image_response = openai.Image.create(
                prompt=prompt,
                n=1,
                size="512x512"  # You can specify the image size
            )
            
            # Save the image URL
            image_url = image_response['data'][0]['url']
            return JSONResponse(content={
                "reply": "Here is the visual you requested:",
                "image_url": image_url
            })

        except Exception as e:
            print(f"Error generating image: {e}")
            return JSONResponse(content={"reply": "Error: Could not generate the visual image."}, status_code=500)

    # Regular chat functionality for non-image requests
    else:
        prompt = (
            "You are TutorBot, a physics expert. Adjust your response based on the user's preferences for detail and complexity. "
            "If the user seems uncertain, ask follow-up questions to reinforce learning and confirm understanding."
        )
        context_messages = conversation_history[session_id][-5:]

        try:
            # Send prompt and user message to OpenAI for response
            response = openai.ChatCompletion.create(
                model="gpt-4-turbo",
                messages=[
                    {"role": "system", "content": prompt},
                    *context_messages
                ]
            )

            bot_reply = response.choices[0].message['content']
            conversation_history[session_id].append({"role": "assistant", "content": bot_reply})

            # Return the bot's response along with the used prompt for documentation
            return JSONResponse(content={
                "reply": bot_reply,
                "prompt_used": prompt,
                "user_input": message,
                "session_id": session_id
            })

        except Exception as e:
            print(f"Error: {e}")
            return JSONResponse(content={"reply": "Error: Could not generate a response from TutorBot."}, status_code=500)
