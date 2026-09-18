# Task Manager API

A REST API for task management built with Django and Django REST Framework. It supports full CRUD operations, task priorities, completion status, timestamps, and a dedicated action for completing a task.

## Features

- Create, list, retrieve, update, and delete tasks
- Priorities: low, medium, and high
- Completion status
- Automatic creation and update timestamps
- Custom endpoint to mark a task as completed
- Browsable API provided by Django REST Framework

## Tech stack

- Python 3
- Django 6
- Django REST Framework
- SQLite

## Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/api/tasks/` | List tasks |
| `POST` | `/api/tasks/` | Create a task |
| `GET` | `/api/tasks/{id}/` | Retrieve a task |
| `PUT/PATCH` | `/api/tasks/{id}/` | Update a task |
| `DELETE` | `/api/tasks/{id}/` | Delete a task |
| `POST` | `/api/tasks/{id}/concluir/` | Mark a task as completed |

Example request body:

```json
{
  "title": "Study Django REST Framework",
  "description": "Review serializers and viewsets",
  "priority": "HIGH",
  "is_done": false
}
```

## Run locally

```bash
git clone https://github.com/juniorlummertz/TODOLIST-part2.git
cd TODOLIST-part2
python -m venv .venv
```

Activate the virtual environment on Windows:

```powershell
.venv\Scripts\activate
```

Then install and start the API:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/api/tasks/`.

## Tests

```bash
python manage.py test
```

## Author

Marcio Junior Lummertz — Systems Analysis and Development student.
