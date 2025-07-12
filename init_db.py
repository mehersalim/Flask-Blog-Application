"""
Developer: Meher Salim
File: init_db.py
Description: Database initialization script that:
1. Resets the entire database
2. Creates all tables
3. Adds a test user with hashed password
4. Creates a sample blog post
5. Commits changes to the database
"""

# Import necessary components from the Flask application
from flask_blog_app import app, db, User, Post

# Create an application context to work with the database
with app.app_context():
    # Database reset section
    # ----------------------
    # Drop all existing tables to start fresh
    # WARNING: This will permanently delete all existing data
    db.drop_all()
    
    # Create all database tables based on defined models
    # This establishes the schema structure
    db.create_all()
    
    # Test user creation
    # ------------------
    # Create a test user with admin privileges
    # Note: In production, you would want stronger credentials
    test_user = User(
        username='admin',          # Default admin username
        email='admin@example.com'  # Default admin email
    )
    # Securely set the password (will be hashed before storage)
    test_user.set_password('password')  # Temporary password for development
    
    # Add the user to the database session (staged for commit)
    db.session.add(test_user)
    
    # Test post creation
    # ------------------
    # Create a sample blog post associated with the test user
    test_post = Post(
        title='First Post',        # Post title
        content='Welcome!',        # Post content
        author=test_user           # Associate post with our test user
    )
    # Add the post to the database session
    db.session.add(test_post)
    
    # Commit all changes to the database
    # This permanently saves our test data
    db.session.commit()
    
    # Success message
    print("Database initialized with test data")