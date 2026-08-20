# Task Management API

## A REST API for managing tasks with FastAPI and SQLite

This repository contains a compact task-management backend built with FastAPI and SQLAlchemy. It provides create, read, update, and delete operations for tasks stored in a local SQLite database.

## Features

### Core Capabilities

- **Create Tasks**: Add tasks through a REST endpoint
- **Read Tasks**: List all tasks or retrieve a task by its identifier
- **Update Tasks**: Modify an existing task
- **Delete Tasks**: Remove a task by its identifier
- **SQLite Persistence**: Stores task data locally through SQLAlchemy
- **Interactive API Docs**: FastAPI exposes OpenAPI documentation when the server is running

## Technology Stack

- **Backend**: Python, FastAPI
- **Database Layer**: SQLAlchemy
- **Database**: SQLite
- **Server**: Uvicorn

## Installation

### Requirements

- Python 3.9 or later recommended
- pip

### Setup

```bash
git clone https://github.com/Shiv-0707/task-management-api-fastapi.git
cd task-management-api-fastapi
python -m venv .venv
```

Activate the environment and install the runtime packages used by the application:

```bash
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install fastapi uvicorn sqlalchemy
```

## Running the Application

```bash
uvicorn main:app --reload
```

After startup, open the interactive API documentation at:

```
http://127.0.0.1:8000/docs
```

## API Operations

The application implements task CRUD operations:

- Create a task
- List tasks
- Retrieve a task by ID
- Update a task
- Delete a task

Use the generated OpenAPI page at `/docs` to inspect the current routes and request models.

## Project Structure

```
task-management-api-fastapi/
├── main.py              # FastAPI application, models, and CRUD routes
├── README.md            # Project documentation
└── tasks.db             # Created locally when the application runs
```

## Development Notes

This is a small backend project intended to demonstrate FastAPI routing and SQLite persistence. It currently keeps the implementation in a single module and has no committed dependency manifest or automated test suite.

## Future Improvements

- Add a pinned `requirements.txt` or `pyproject.toml`
- Add request validation and test coverage
- Add authentication and user ownership for tasks
- Split database, schema, and route code into separate modules
- Add Docker and deployment configuration

## Contact

Shiv Pratap Singh — [GitHub](https://github.com/Shiv-0707) · shivpratap0709@gmail.com
