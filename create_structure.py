import os
from pathlib import Path

# Project root (where script is executed)
BASE_DIR = Path.cwd()

# Folder structure blueprint
STRUCTURE = {
    "app": {
        "__init__.py": "",
        "config.py": "",
        "core": {
            "__init__.py": "",
            "extensions.py": "# Flask-SQLAlchemy, Flask-Migrate etc.",
            "middleware.py": "# Auth middleware, error handlers"
        },
        "auth": {
            "__init__.py": "",
            "routes.py": "# Authentication endpoints",
            "services.py": "# Firebase auth logic",
            "schemas.py": "# Validation schemas (Marshmallow/Pydantic)"
        },
        "loans": {
            "__init__.py": "",
            "routes.py": "# Loan management endpoints",
            "services.py": "# EMI calculation logic",
            "schemas.py": "# Loan request validation"
        },
        "payments": {
            "__init__.py": "",
            "routes.py": "# Payment processing endpoints",
            "services.py": "# Payment gateway integration",
            "schemas.py": "# Payment validation"
        },
        "admin": {
            "__init__.py": "",
            "routes.py": "# Admin dashboard endpoints",
            "services.py": "# Admin-specific logic"
        },
        "models": {
            "__init__.py": "",
            "user.py": "# User model",
            "loan.py": "# Loan model",
            "transaction.py": "# Transaction model"
        },
        "utils": {
            "__init__.py": "",
            "firebase.py": "# Firebase Admin SDK helpers",
            "emi_calculator.py": "# EMI math logic",
            "logger.py": "# Logging configuration"
        },
        "tests": {
            "__init__.py": "",
            "test_auth.py": "",
            "test_loans.py": "",
            "test_payments.py": ""
        }
    },
    "migrations": {},
    "requirements.txt": "# Python dependencies",
    ".env": "# Environment variables",
    "run.py": "# Flask app entry point"
}

def create_structure(root, structure):
    for name, content in structure.items():
        path = root / name
        
        if isinstance(content, dict):  # It's a directory
            path.mkdir(exist_ok=True)
            if name == "migrations":
                (path / "__init__.py").touch(exist_ok=True)
            create_structure(path, content)
        else:  # It's a file
            with open(path, "w") as f:
                if content:
                    f.write(content + "\n")

if __name__ == "__main__":
    create_structure(BASE_DIR, STRUCTURE)
    print("Folder structure created successfully!")