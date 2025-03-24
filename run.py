from flask import Flask, jsonify, request
from app import create_app
from app.utils.firebase import verify_id_token

# Create the Flask app
app = create_app()

# Test endpoint for Firebase token verification
@app.route('/test-token', methods=['POST'])
def test_token():
    # Get token from request
    token = request.json.get('token')
    
    if not token:
        return jsonify({'error': 'Token is required'}), 400
    
    # Verify token
    decoded_token = verify_id_token(token)
    
    if decoded_token:
        return jsonify({
            'success': True,
            'uid': decoded_token.get('uid'),
            'email': decoded_token.get('email')
        }), 200
    else:
        return jsonify({'error': 'Invalid or expired token'}), 401

if __name__ == '__main__':
    # Verify Firebase initialization
    try:
        from app.utils.firebase import auth
        print("✅ Firebase initialized successfully!")
        print("🔑 Test endpoint: POST http://localhost:5000/test-token")
    except Exception as e:
        print("❌ Firebase initialization failed:", str(e))
    
    # Check database connection
    try:
        from app.core.extensions import db
        with app.app_context():
            db.engine.connect()
            print("✅ Database connection successful!")
    except Exception as e:
        print("❌ Database connection failed:", str(e))
    
    app.run(debug=True, port=5000)