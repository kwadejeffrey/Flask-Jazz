
# Flask API Setup Guide

## Project Description
This is a simple Flask API designed to perform task management operations. The API exposes endpoints to manage tasks such as adding, updating, and deleting tasks.

---

## Prerequisites

To run this Flask API, ensure you have the following installed on your machine:

1. **Python 3.7+** – [Download Python](https://www.python.org/downloads/)
2. **pip** – Python package manager (usually installed with Python)
3. **Virtual Environment** (optional, but recommended) – for isolating project dependencies

---

## Installation Instructions

### 1. Clone the Repository

```bash
git clone git@github.com:kwadejeffrey/Flask-Jazz.git
cd Flask-Jazz
```

### 2. Set Up a Virtual Environment (Optional but Recommended)

To create and activate a virtual environment:

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file at the root of your project directory to store environment variables such as the Flask app name and the environment type:

```bash
# .env file
FLASK_APP=api.py
FLASK_ENV=development
```

### 5. Database Setup (Optional)

If your Flask API uses a database, make sure you have the database set up and configured correctly. Update the database configuration in your `config.py` file or `.env` file.

```bash
# Example for SQLite or MySQL
SQLALCHEMY_DATABASE_URI = 'sqlite:///tasks.db'
# or
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/db_name'
```

### 6. Running Migrations (Optional)

If you're using **SQLAlchemy** or **Flask-Migrate**, you may need to apply migrations:

```bash
flask db init
flask db migrate
flask db upgrade
```

### 7. Run the Flask Application

To start the Flask API, run the following command:

```bash
flask run --port 5001
```

By default, the app will run on [http://127.0.0.1:5001/](http://127.0.0.1:5001/).

You can also use the following command to run the app:

```bash
python api.py
```

---

## Testing the API

Once the server is running, you can test the API using `curl`, Postman, or any other HTTP client.

For example, you can test the root endpoint:

```bash
curl http://127.0.0.1:5001/
```

### Sample Endpoint

- **POST /api/tasks**: Create a new task

```bash
curl -X POST http://127.0.0.1:5001/api/tasks -d '{"task_name":"New Task", "task_description":"Description here", "is_done":false}' -H "Content-Type: application/json"
```

---

## Troubleshooting

### Common Issues:
- **Port Already in Use**: If you get an error like `Port 5001 is already in use`, make sure that no other application is using the same port or change the port number.
- **Missing Dependencies**: If you encounter errors related to missing dependencies, run `pip install -r requirements.txt` again.
  


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
