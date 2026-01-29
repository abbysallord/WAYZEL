import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add Backend to path
sys.path.insert(0, os.path.dirname(__file__))

from Backend.app import app

if __name__ == "__main__":
    app.run()
