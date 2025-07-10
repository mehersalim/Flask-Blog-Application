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

![image](https://github.com/user-attachments/assets/fc1f0e55-1a69-4fae-9b9e-85b346eb4007)

2. Create a virtual environment (recommended):

![image](https://github.com/user-attachments/assets/a71a5db5-d37a-44bd-b97a-29ee07436ed8)

3. Install dependencies:

![image](https://github.com/user-attachments/assets/a3508f5b-8777-42dc-b1bb-48beeee4548b)

4. Set up the database:

![image](https://github.com/user-attachments/assets/5569c4b9-3dff-4da1-98b9-71002e708ee1)

5. Configure the secret key:
      Replace 'your-secret-key-here' in app.config['SECRET_KEY'] with a strong secret key
   
## Running the Application

bash
python app.py

The application will be available at http://localhost:5000

## Project Structure

![image](https://github.com/user-attachments/assets/153e831d-6431-40c9-b459-bed8e073268e)

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
