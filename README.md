# Travel Audio Guide Generator

This project is a web application that generates personalized audio travel guides for various destinations. It leverages **Google Gemini** for generating content and **Murf AI** for high-quality text-to-speech conversion.

## Features

- **Destination Selection**: Users can choose from a list of predefined destinations or search/select their own.
- **Customizable Experience**:
  - **Language**: Supports English, Hindi, Tamil, and Telugu.
  - **Guide Length**: Choose between a "Summary" or a "Detailed" description.
  - **Voice Selection**: Select between Male and Female voices for each language.
- **AI-Powered Content**: Generates rich, culturally relevant descriptions using Google Gemini.
- **Lifelike Audio**: Converts the generated text into natural-sounding speech using Murf AI.

## Tech Stack

- **Frontend**: HTML5, CSS3, Vanilla JavaScript.
- **Backend**: Python, Flask.
- **AI Services**:
  - **Content Generation**: Google Gemini 2.5 Flash.
  - **Text-to-Speech**: Murf AI (Falcon model).

## Prerequisites

- Python 3.8+
- [Murf AI API Key](https://murf.ai/)
- [Google Gemini API Key](https://ai.google.dev/)

## Installation & Setup

### 1. Backend Setup

1.  Navigate to the `Backend` directory:

    ```bash
    cd Backend
    ```

2.  Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  Install dependencies:

    ```bash
    pip install -r ../requirements.txt
    ```

    _(Note: `requirements.txt` is located in the root directory)_

4.  Configure Environment Variables:
    - Create a `.env` file in the `Backend` directory (or root, depending on where you run it from). You can use `.env.example` as a reference.
    - Add your API keys:
      ```ini
      GOOGLE_API_KEY=your_google_api_key
      MURF_API_KEY=your_murf_api_key
      ```

5.  Run the Flask server:
    ```bash
    python app.py
    ```
    The backend will start at `http://127.0.0.1:5000`.

### 2. Frontend Setup

1.  Navigate to the `Frontend` directory.
2.  Open `index.html` in your web browser.
    - You can simply double-click the file, or use a live server extension (like in VS Code) for a better experience.

## Usage

1.  Ensure the backend server is running.
2.  Open the frontend application.
3.  Select a card (Place) or search for one.
4.  Choose your preferred **Language**, **Voice**, and **Guide Length**.
5.  Click **"Generate Audio Guide"**.
6.  Wait for the AI to process (Transcript and Audio will be generated).
7.  Read the description or listen to the audio guide!

## Deployment

### Option 1: Render.com (Recommended)

**Backend Deployment:**

1. Push code to GitHub
2. Create account at [render.com](https://render.com)
3. New Web Service → Connect GitHub repo
4. Configure:
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `gunicorn Backend.app:app`
   - **Environment variables:** Add `GOOGLE_API_KEY` and `MURF_API_KEY`
5. Deploy and note the backend URL (e.g., `https://travel-guide-api.onrender.com`)

**Frontend Deployment:**

1. Create account at [vercel.com](https://vercel.com)
2. Import your GitHub repo
3. Set root directory to `Frontend`
4. Deploy

**After deployment**, update `Frontend/index.js`:

```javascript
const GENERATE_AUDIO_GUIDE_API_URL =
  "https://your-backend-url.onrender.com/generate-audio-guide";
```

### Option 2: Railway

1. Go to [railway.app](https://railway.app)
2. Create new project → Connect GitHub repo
3. Add `GOOGLE_API_KEY` and `MURF_API_KEY` environment variables
4. Auto-deploys when you push

### Option 3: Docker + Any Cloud

```bash
docker build -t travel-guide .
# Push to your cloud provider (AWS, Google Cloud, DigitalOcean, etc.)
```

## Project Structure

```
├── Backend/
│   └── app.py              # Main Flask application
├── Frontend/
│   ├── index.html          # Main user interface
│   └── index.js            # Frontend logic
├── .env.example            # Example environment variables
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```
## End of README