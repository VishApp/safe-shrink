# Flask URL Shortener

A simple URL shortening web app built using Flask, featuring malware URL checking via VirusTotal API.

## 📸 Screenshot

![URL Shortener Screenshot](app/static/screenshot1.png)

![URL Shortener Screenshot](app/static/screenshot2.png)

## 🎯 Features

- **Easy URL Shortening:** Convert long URLs into short, shareable links.
- **SQLite Database:** Efficient storage and retrieval using SQLAlchemy.
- **Simple Web UI:** Minimalist, user-friendly interface.
- **RESTful API:** Programmatically shorten URLs via an API endpoint.
- **VirusTotal Integration:** Checks URLs for malicious content before shortening.
- **Docker Support:** Easily containerized and deployable anywhere.

## 🚀 Tech Stack

- **Flask**
- **SQLite & SQLAlchemy**
- **VirusTotal API**
- **Docker**

## ⚙️ Installation

### Using Docker

```bash
docker-compose up --build
```

Visit [http://localhost:5000](http://localhost:5000)

### Manual Setup

```bash
python -m venv venv

source venv/bin/activate  # On Windows: .\venv\Scripts\activate

pip install -r requirements.txt

export FLASK_APP=app

export FLASK_RUN_HOST=localhost

flask run
```

## 🌐 API Usage

### Shorten URL

Make a POST request to `/api/shorten`:

```json
POST /api/shorten
Content-Type: application/json

{
  "url": "https://example.com"
}
```

### Example Response

```json
{
  "short_url": "http://localhost:5000/abc123",
  "malicious": false
}
```

If a URL is detected as malicious:

```json
{
  "error": "URL detected as malicious",
  "malicious": true
}
```

## 📁 Project Structure

```
flask-url-shortener/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   └── static/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## ⚡ Future Enhancements

- Custom URL aliases
- Analytics and click tracking
- User authentication
- URL expiration dates

## 🤝 Contributions

Feel free to fork this repository, submit pull requests, or suggest improvements!