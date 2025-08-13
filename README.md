# Flask Demo App

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-blue.svg)](https://flask.palletsprojects.com/)

This repo is a basic Flask web application.
- **Routes**: Home, About, and API endpoints
- **Templates**: Using Jinja2 HTML templates with a base layout
- **API Endpoints**: JSON responses for GET and POST responses
- **Styling**: External CSS file

## Project Structure

```
demo-flask/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── static/             # Static files
│   └── css/            # CSS stylesheets
│       └── style.css   # Main stylesheet
├── templates/          # HTML templates
│   ├── base.html       # Base template with navigation
│   ├── index.html      # Home page
│   └── about.html      # About page
└── README.md           # Project documentation
```

## Installation

1. **Clone or download** this repository.
2. **Navigate** to the project directory:
   ```bash
   cd demo-flask
   ```
3. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask development server**:
   ```bash
   python app.py
   ```

2. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```


### Key Files Explained

- **`app.py`**: Main application file containing all routes and logic
- **`static/css/style.css`**: External CSS stylesheet
- **`templates/base.html`**: Base template providing common layout and navigation
- **`templates/index.html`**: Home page template
- **`templates/about.html`**: About page template

### Adding New Features

1. **New Routes**: Add route functions in `app.py`
2. **New Templates**: Create HTML files in `templates/` directory
3. **New API Endpoints**: Add JSON-returning functions in `app.py`

## Learning Objectives

This demo covers:
- Flask application structure and setup
- Route handling and view functions
- Template inheritance and Jinja2 syntax
- Building simple API endpoints
- Static file serving
- Basic web development concepts

## Next Steps

Consider extending this demo with:
- Database integration (SQLAlchemy)
- User authentication and sessions
- Form handling and validation
- Static file serving (CSS, JS, images)
- More advanced API features
- Testing with pytest

## Requirements

- Python 3.7+
- Flask 3.0.0
- See `requirements.txt` for complete dependency list

## License

This is a demo project for educational purposes.
