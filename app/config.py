import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv()

class Config:
    # PostgreSQL Configuration
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:Qwer%40123@localhost/loan_app_db"  # @ -> %40
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Firebase Configuration
    FIREBASE_CREDENTIALS_PATH = os.getenv(
        "FIREBASE_CREDENTIALS_PATH",
        str(Path.cwd() / "firebase-adminsdk.json")  # Look in project root
    )

    @classmethod
    def verify_firebase_credentials(cls):
        """Check if Firebase credentials file exists"""
        if not Path(cls.FIREBASE_CREDENTIALS_PATH).exists():
            raise FileNotFoundError(
                f"Firebase credentials not found at: {cls.FIREBASE_CREDENTIALS_PATH}\n"
                "1. Download service account key from Firebase Console\n"
                "2. Rename to 'firebase-adminsdk.json'\n"
                "3. Place in project root folder"
            )