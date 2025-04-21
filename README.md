# Secure Message API

> A simple Flask-based API that stores and retrieves messages using PostgreSQL, Docker, and CI/CD pipelines.

![CI](https://github.com/danieljelacik/secure-message-api/actions/workflows/ci.yml/badge.svg)


This is a small learning project where I built a simple message API using:

- Python and Flask (backend)
- PostgreSQL (database)
- Docker and Docker Compose (containerization)
- GitHub Actions (CI)
- pytest (testing)

The goal of this project was to understand how to combine backend development with DevOps tools like Docker and CI pipelines.

---

## What does this app do?

This API has two main endpoints:

- `POST /send` — Sends a message and stores it in the database
- `GET /messages` — Returns all messages as JSON

Messages are saved in a PostgreSQL database.

---

## Why these tools?

- **Flask** is simple and good for learning how APIs work
- **PostgreSQL** is a real SQL database used in production
- **Docker** helps run the app and database in any environment
- **GitHub Actions** runs tests automatically when I push code
- **pytest** helps me check that the message feature actually works

---

## How to run the app with Docker

1. Install Docker and make sure it’s running
2. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd secure-message-api
   ```
---
## How to run the app with Docker

1. Make sure Docker is installed and running on your computer.

2. Clone this repository and go into the project folder:
   ```bash
   git clone <your-repo-url>
   cd secure-message-api
   ```
3. Start the app and the database using Docker Compose:
   ```bash
   docker compose up --build
   ```
4. Once it’s running, the API will be available at:
   ```bash
   http://localhost:5000
   ```

You can now send and receive messages using tools like curl, Postman, or your browser.

---

## How to test the app

You can use `curl` to test the endpoints:

Send a message:

   ```bash
   curl -X POST http://localhost:5000/send \
     -H "Content-Type: application/json" \
     -d '{"content": "Hello from Docker!"}'
   ```
Get all messages:

   ```bash
curl http://localhost:5000/messages
   ```

---

## How CI works

The GitHub Actions workflow runs on every push to the `main` branch. It does the following:

- Starts PostgreSQL in a test container
- Installs Python dependencies
- Runs a Python test with `pytest` that:
  - Sends a test message
  - Makes sure the message is returned correctly

This shows that the system works end-to-end in an automated environment.

---

## What I learned

- How to build a small Flask API with a database
- How to use Docker Compose to run services together
- How to isolate test data using SQLite
- How to write a GitHub Actions CI workflow that installs dependencies, starts services, and runs automated tests

This was my first project combining backend development and DevOps tools, and it helped me understand the full development pipeline from code to deployment and testing.

---


## Next steps

- Add a frontend to display and send messages (easier for non tech users)
- Add user authentication
- Use environment variables for configuration
- Deploy the app to a cloud environment (e.g., Heroku, AWS)
