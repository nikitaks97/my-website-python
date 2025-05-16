# My Website

This project is a simple web application built using Flask. It consists of multiple pages including a homepage, an about page, and a contact page. The application is structured to facilitate continuous integration and deployment (CI/CD) using GitHub Actions.

## Project Structure

```
my-website
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── templates
│   │   ├── index.html
│   │   ├── about.html
│   │   └── contact.html
│   └── static
│       └── style.css
├── tests
│   └── test_routes.py
├── requirements.txt
├── .gitignore
├── Dockerfile
├── .github
│   └── workflows
│       └── ci.yml
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/my-website.git
   cd my-website
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```
   flask run
   ```

5. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000`.

## Pages

- **Homepage:** Displays the main content of the website.
- **About Page:** Provides information about the website or organization.
- **Contact Page:** Contains a contact form or contact information.

## Testing

To run the tests, ensure you have installed the dependencies and then execute:
```
pytest tests/test_routes.py
```

## CI/CD

This project includes a CI/CD pipeline configured with GitHub Actions. The configuration file is located at `.github/workflows/ci.yml`. It automates the process of building, testing, and deploying the application.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.