# Bitly Clone with QR Code Support

This is a Django-based web application that replicates the functionality of the Bitly URL shortener service. It allows users to create short links, manage them, and generate QR codes for easy sharing. The application includes authentication, tagging, and analytics for tracking link redirects.

---

## Features

- **User Authentication**:
  - Registration, login, and profile management.
- **URL Shortening**:
  - Convert long URLs into short, shareable links.
- **QR Code Generation**:
  - Automatically generate QR codes for shortened URLs.
- **Link Management**:
  - View, tag, and delete created links.
  - Track the number of redirects for each link.
- **Tagging**:
  - Organize links with custom tags for easy filtering and searching.
- **Responsive Design**:
  - Optimized for both desktop and mobile devices.
- **Dark Mode**:
  - Provides a visually appealing dark-themed UI.

---

## Technologies Used

- **Backend**:
  - Python 3.x
  - Django 5.x
  - PostgreSQL for database management
- **Frontend**:
  - HTML5, CSS3, Bootstrap 5
- **QR Code Generation**:
  - Python `qrcode` library
- **Docker**:
  - Containerized application setup using `docker-compose`.

---

## Installation and Setup

### Prerequisites

Before you start, ensure you have the following installed:

- Python 3.8+
- Docker and Docker Compose
- PostgreSQL installed locally or via Docker

### Environment Variables

Create a `.env` file in the root directory with the following content:

```plaintext
DB_NAME="bitly"
DB_USER="postgres"
DB_PASSWORD="postgres"
DB_HOST="db"
DB_PORT="5432"
SECRET_KEY="your-django-secret-key"
DEBUG=True
```

### Steps to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/abl1v1on/shortlink.git
   cd shortlink
   ```

2. **Set up and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## Usage

1. **Create an Account**:
   Register a new account or log in with existing credentials.
2. **Shorten a Link**:
   Navigate to the "Create Link" page, enter the URL, and select optional tags.
3. **Manage Links**:
   View your links, track redirect counts, and delete unwanted links.
4. **Generate QR Codes**:
   Automatically generated QR codes are displayed alongside shortened links.

---

## Project Structure

- **`links/`**:
  Contains the main URL shortener app.
- **`users/`**:
  Handles authentication and user management.
- **`templates/`**:
  HTML templates for the application.
- **`static/`**:
  CSS, JavaScript, and image assets.
- **`media/`**:
  Stores uploaded QR code images.

---

## Future Improvements

- Add social sharing buttons for generated links and QR codes.
- Implement advanced analytics for link performance.
- Support for custom short links (e.g., user-defined slugs).

---
