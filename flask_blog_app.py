"""
Developer: Meher Salim
File: flask-blog-app.py
Project Name: Flask Blog Application
Description:
- A complete blog application with user authentication (registration/login/logout)
- Full CRUD (Create, Read, Update, Delete) operations for blog posts
- SQLite database backend with SQLAlchemy ORM
- Flask-Login for session management and authentication
- Secure password hashing with Werkzeug
"""

# Import required modules
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

# Initialize Flask application
app = Flask(__name__)

# ==============
# Configuration
# ==============
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Should be changed in production!
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'  # SQLite database path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disables modification tracking

# ===================
# Extension Setup
# ===================
db = SQLAlchemy(app)  # Initialize SQLAlchemy for database operations

# Configure Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Specify the login view route

# ==============
# Database Models
# ==============

class User(UserMixin, db.Model):
    """
    User model representing registered users with:
    - Authentication capabilities (via Flask-Login's UserMixin)
    - Relationship to blog posts
    - Secure password storage
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)  # Stores hashed passwords
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Account creation timestamp
    posts = db.relationship('Post', backref='author', lazy=True)  # One-to-many relationship with posts

    def set_password(self, password):
        """
        Securely hash and store the user's password using PBKDF2 with SHA256.
        This is more secure than the default scrypt method for this use case.
        """
        self.password_hash = generate_password_hash(
            password,
            method='pbkdf2:sha256',  # Recommended hashing algorithm
            salt_length=8            # Appropriate salt length
        )

    def check_password(self, password):
        """
        Verify a password against the stored hash.
        Returns True if the password matches, False otherwise.
        """
        return check_password_hash(self.password_hash, password)


class Post(db.Model):
    """
    Blog Post model containing:
    - Title and content
    - Timestamps for creation and updates
    - Foreign key relationship to User model
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)  # Post title with length limit
    content = db.Column(db.Text, nullable=False)       # Post content (unlimited length)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Initial creation time
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Auto-updates on changes
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Author reference

# ===================
# Authentication Setup
# ===================

@login_manager.user_loader
def load_user(user_id):
    """
    Required Flask-Login callback function.
    Reloads the user object from the user ID stored in the session.
    """
    return User.query.get(int(user_id))

# =================
# Helper Functions
# =================

def create_tables():
    """Create all database tables within the application context."""
    with app.app_context():
        db.create_all()

# =========
# Routes
# =========

@app.route('/')
def index():
    """
    Homepage route.
    Displays all blog posts in reverse chronological order.
    """
    posts = Post.query.order_by(Post.created_at.desc()).all()  # Get newest posts first
    return render_template('index.html', posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    User registration route.
    Handles both display of registration form and processing of submissions.
    """
    if current_user.is_authenticated:
        return redirect(url_for('index'))  # Prevent logged-in users from registering
        
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Validate required fields
        if not username or not email or not password:
            flash('All fields are required.', 'error')
            return redirect(url_for('register'))
            
        # Check for existing username
        if User.query.filter_by(username=username).first():
            flash('Username already taken.', 'error')
            return redirect(url_for('register'))
            
        # Check for existing email
        if User.query.filter_by(email=email).first():
            flash('Email already registered.', 'error')
            return redirect(url_for('register'))
            
        # Create and save new user
        new_user = User(username=username, email=email)
        new_user.set_password(password)  # Hash password before storage
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
        
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    User login route.
    Handles both login form display and authentication.
    """
    if current_user.is_authenticated:
        return redirect(url_for('index'))  # Redirect if already logged in
        
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        remember = True if request.form.get('remember') else False  # "Remember me" option
        
        user = User.query.filter_by(username=username).first()
        
        # Validate credentials
        if not user or not user.check_password(password):
            flash('Invalid username or password.', 'error')
            return redirect(url_for('login'))
            
        # Log user in and create session
        login_user(user, remember=remember)
        return redirect(url_for('index'))
        
    return render_template('login.html')

@app.route('/logout')
@login_required  # Only accessible to logged-in users
def logout():
    """Log out the current user and clear the session."""
    logout_user()
    return redirect(url_for('index'))

@app.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    """
    Create new blog post route.
    Requires authentication.
    """
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        
        # Validate required fields
        if not title or not content:
            flash('Title and content are required.', 'error')
            return redirect(url_for('create_post'))
            
        # Create and save new post
        new_post = Post(title=title, content=content, author=current_user)
        db.session.add(new_post)
        db.session.commit()
        
        flash('Post created successfully!', 'success')
        return redirect(url_for('index'))
        
    return render_template('create_post.html')

@app.route('/post/<int:post_id>')
def view_post(post_id):
    """
    View single blog post route.
    Accessible to all users (authenticated or not).
    """
    post = Post.query.get_or_404(post_id)  # Returns 404 if post doesn't exist
    return render_template('view_post.html', post=post)

@app.route('/post/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    """
    Edit existing blog post route.
    Only accessible to the post's author.
    """
    post = Post.query.get_or_404(post_id)
    
    # Authorization check
    if post.author != current_user:
        flash('You can only edit your own posts.', 'error')
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        # Update post with new data
        post.title = request.form['title']
        post.content = request.form['content']
        db.session.commit()
        
        flash('Post updated successfully!', 'success')
        return redirect(url_for('view_post', post_id=post.id))
        
    return render_template('edit_post.html', post=post)

@app.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    """
    Delete blog post route.
    Only accessible to the post's author.
    Uses POST method to prevent CSRF attacks.
    """
    post = Post.query.get_or_404(post_id)
    
    # Authorization check
    if post.author != current_user:
        flash('You can only delete your own posts.', 'error')
        return redirect(url_for('index'))
        
    # Delete post
    db.session.delete(post)
    db.session.commit()
    
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('index'))

# ================
# Application Start
# ================
if __name__ == '__main__':
    # Create database if it doesn't exist
    if not os.path.exists('instance/blog.db'):
        create_tables()
        
    # Start development server
    app.run(debug=True)