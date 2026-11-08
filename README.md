# FormSure — Application Submission Validator

**Validate before you submit.**

FormSure is a lightweight web application designed to help students catch common mistakes before submitting internship, scholarship, and university applications.

A missing field, incorrectly formatted phone number, or unsupported resume file can make an application incomplete. FormSure aims to identify these issues early through simple, automated validation.

## Problem Statement

Students frequently submit applications with missing information, invalid contact details, or incorrectly formatted documents. These small mistakes can lead to incomplete submissions and unnecessary delays.

FormSure addresses this problem by providing a simple validation interface that checks application details before submission.

## Key Features

- **Required Field Validation:** Checks whether essential application details are provided.
- **Email Validation:** Identifies incorrectly formatted email addresses.
- **Phone Number Validation:** Checks whether the phone number contains exactly 10 digits.
- **Resume Upload Validation:** Checks the resume file extension.
- **File Size Validation:** Enforces an upload size limit.
- **Clear Error Messages:** Displays issues that need to be corrected before submission.

## Technology Stack

| Technology | Purpose |
|---|---|
| HTML5 | Application form structure |
| CSS3 | User interface and styling |
| Python | Validation logic |
| Flask | Backend web framework |
| SQLite | Planned database integration |
| Selenium | Planned browser automation testing |
| Java & TestNG | Planned automated test framework |
| Playwright | Planned cross-browser and end-to-end testing |
| Pytest | Planned Python test framework |
| Git & GitHub | Version control |

## Project Structure

```text
FormSure/
│
├── app/
│   ├── app.py
│   ├── validator.py
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   └── static/
│       └── style.css
│
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/FormSure.git
```

### 2. Navigate to the application directory

```bash
cd FormSure/app
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

From the project root directory, run:

```bash
pip install -r requirements.txt
```

### 5. Start the application

Navigate into the `app` directory and run:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## Validation Rules

| Field | Validation |
|---|---|
| Full Name | Cannot be empty |
| Email | Must follow a valid email format |
| Phone | Must contain exactly 10 digits |
| Resume | PDF, DOC, or DOCX formats |
| Resume Size | Maximum 5 MB |

## Testing Strategy

FormSure is being developed with an emphasis on software quality and test automation.

The planned testing approach includes:

- **Selenium with Java:** Browser automation for form interactions and validation scenarios.
- **Playwright with Python:** End-to-end testing and browser compatibility checks.
- **Pytest:** Organizing and executing automated Python tests.
- **Negative Testing:** Checking how the application handles missing fields, invalid inputs, and unsupported files.

Both Selenium and Playwright will be used to test the same application through different automation approaches.

## Current Development Status

- [x] Initial Flask application structure
- [x] Application form interface
- [x] Basic input validation logic
- [x] Requirements file
- [ ] Run and verify the application locally
- [ ] Improve file-size validation and error handling
- [ ] Add database integration using SQLite
- [ ] Implement automated tests using Selenium
- [ ] Implement automated tests using Playwright
- [ ] Add test documentation and results

## Project Goal

The goal of FormSure is to build a practical application that demonstrates backend development, input validation, software testing fundamentals, and browser automation.

It is being developed as a hands-on learning project with a focus on building reliable software and understanding how quality assurance fits into the development lifecycle.

---

**Built with Python, Flask, and a focus on software quality.**
