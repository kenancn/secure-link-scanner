# Secure Link App Tool

Secure Link App Tool is a Flask application designed to extract URLs from web pages and analyze them for security using the VirusTotal API. It ensures that the URLs you check are safe and displays the results in a user-friendly interface.

## Features

- **Unique URL Scanning**: Avoids duplicate URL scans by ensuring only unique URLs are analyzed.
- **Multithreaded Scanning**: Scans multiple URLs simultaneously, improving efficiency and speed.
- **VirusTotal API Integration**: Utilizes VirusTotal API for comprehensive security checks on URLs.
- **User-Friendly Interface**: Provides a simple and clear interface for easy navigation.
- **Environment Variables**: API keys and configuration settings are securely managed via environment variables.

## Getting Started

This tool can be easily run using Docker. You can also set it up locally for development purposes.

### Prerequisites

- Docker (Docker Compose recommended)
- Python 3.11 (for local development)
- VirusTotal API key

### Running with Docker

1. **Clone the Repository**

   Clone the repository to your local machine:

   ```bash
   git clone https://github.com/kenancn/secure-link-scanner.git
   cd secure-link-scanner
   ```
### Set Up Environment Variables

Create a `.env` file in the root directory and add the following details:

```
API_URL=https://www.virustotal.com/api/v3
VIRUSTOTAL_API_KEY=your_virustotal_api_key
```

### Build the Docker Image

Build the Docker image using the following command:

```bash
docker build -t secure_link_scanner .
```

### Run the Docker Container

Start the container with the following command:

```bash
docker run --name secure_link_scanner -p 5002:5002 --env-file .env secure_link_scanner
```

Alternatively, you can use Docker Compose:

```bash
docker-compose up
```

### Local Development

#### Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

#### Run the Flask Application

Set the environment variables and start the Flask development server:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Ensure the environment variables (`API_URL` and `VIRUSTOTAL_API_KEY`) are correctly configured.

### How to Use

- **Access the Application**: Open your browser and go to `http://localhost:5002`.
- **Scan a URL**: Enter the URL of the web page you want to scan and submit. The results will be displayed on the same page.
- **View Results**: The scan results will show the status of the URL and its security assessment.
