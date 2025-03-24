import firebase_admin
from firebase_admin import credentials, auth
from app.config import Config

# Initialize Firebase
def initialize_firebase():
    try:
        # Verify credentials file exists
        Config.verify_firebase_credentials()
        
        # Initialize Firebase Admin SDK
        cred = credentials.Certificate(Config.FIREBASE_CREDENTIALS_PATH)
        firebase_admin.initialize_app(cred)
        print("✅ Firebase initialized successfully!")
        
    except Exception as e:
        print(f"🔥 Critical Firebase Error: {str(e)}")
        raise

def verify_id_token(id_token):
    """Verify Firebase ID token and return decoded payload"""
    try:
        return auth.verify_id_token(id_token)
    except Exception as e:
        print(f"⚠️ Token verification failed: {str(e)}")
        return None