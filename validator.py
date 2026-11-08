
import re

ALLOWED_EXTENSIONS = {"pdf", "doc", "docx"}
MAX_FILE_SIZE = 5 * 1024 * 1024


def validate_application(data, files):
    errors = []

    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    phone = data.get("phone", "").strip()

    if not name:
        errors.append("Full name is required.")

    if not email:
        errors.append("Email address is required.")
    elif not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
        errors.append("Enter a valid email address.")

    if not phone:
        errors.append("Phone number is required.")
    elif not re.fullmatch(r"[0-9]{10}", phone):
        errors.append("Phone number must contain 10 digits.")

    resume = files.get("resume")

    if not resume or not resume.filename:
        errors.append("Resume is required.")
    else:
        extension = resume.filename.rsplit(".", 1)[-1].lower()

        if "." not in resume.filename or extension not in ALLOWED_EXTENSIONS:
            errors.append("Resume must be PDF, DOC or DOCX.")

        if resume.content_length is not None and resume.content_length > MAX_FILE_SIZE:
            errors.append("Resume must be smaller than 5 MB.")

    return errors
