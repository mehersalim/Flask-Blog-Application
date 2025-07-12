# Flask Blog Application
## Developer: Meher Salim

![Python](https://img.shields.io/badge/python-3.6%2B-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple blog application with user authentication and CRUD operations for blog posts, built with Flask.

## Features

- User registration and authentication
- Create, read, update, and delete blog posts
- Secure password hashing
- SQLite database storage
- Flask-Login for session management
- Responsive templates (assuming you have template files)

## Requirements

- Python 3.6+
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Werkzeug (for password hashing)

## Installation

1. Clone the repository:

![image](https://github.com/user-attachments/assets/78013fc2-8e76-407f-8fb0-322296a11975)

2. Create a virtual environment (recommended):

![image](https://github.com/user-attachments/assets/71ab1a50-3782-4cd5-94b2-7fe6a9b56e29)

3. Install dependencies:

![image](https://github.com/user-attachments/assets/a3508f5b-8777-42dc-b1bb-48beeee4548b)

*(If requirment.txt doesn't exist, manually install these packages:)*

![image](https://github.com/user-attachments/assets/478f64ad-e03c-410f-b9fa-9e04e8332a96)

4. Initialize the Database:

Run Python interactively to create tables:
![image](https://github.com/user-attachments/assets/4d4916dc-a701-401b-a8c3-c34060b7c9e5)

5. Configure the Environment Variables:

![image](https://github.com/user-attachments/assets/e0b501ea-228e-4d6d-b8a0-e19e1051ab8a)

Create a .env file (optional but recommended for production):

## Running the Application

### Run Command
<img width="778" height="406" alt="image" src="https://github.com/user-attachments/assets/5f0ce122-93e3-4bbd-b72f-f5cc42824a45" />


### Alternative

<img width="494" height="58" alt="image" src="https://github.com/user-attachments/assets/82cd3b21-f9a1-4600-bd0e-bf489d7451b2" />


The application will be available at http://localhost:5000 or http://127.0.0.1:5000

## Project Structure

<img width="1216" height="942" alt="image" src="https://github.com/user-attachments/assets/1f1bcd5b-9e9e-46f1-9124-46058253090e" />

## Configuration

The application can be configured by modifying the following in app.py:
  - SECRET_KEY: Essential for session security (change in production!)
  - SQLALCHEMY_DATABASE_URI: Database connection string
  - SQLALCHEMY_TRACK_MODIFICATIONS: Disabled for performance

## Usage

1. Register a new user account
2. Log in with your credentials
3. Create, edit, or delete your blog posts
4. View all posts on the home page

## Security Notes

- Always use a strong secret key in production
- Consider using environment variables for sensitive configuration
- This is a demo application - for production use, consider additional security measures

## Contributing

Contributions are welcome! Please open an issue or pull request for any improvements.

## License

This project is open source and available under the MIT License.
