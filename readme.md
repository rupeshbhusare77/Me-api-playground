# Me-API Playground

A full-stack personal profile API and web app that lets you showcase your resume, skills, and projects with a FastAPI backend and a modern HTML/CSS/JS frontend.

***

## Demo

- **Frontend:** [Link](https://me-api-playground-flame.vercel.app/)
- **Backend API Docs:** [Link](https://me-api-playground-production-0cb4.up.railway.app/docs)


***

## Features

- RESTful API for candidate profile, skills, projects, education, contacts
- Real data seeded from your resume and portfolio
- Filter and search endpoints for projects and skills
- Minimal, clean, mobile-friendly frontend (HTML/CSS/JS)
- Deployed free with [Railway](https://railway.app) (backend) and [Vercel](https://vercel.com) (frontend)

***

## Directory Structure
```
repo-root/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   └── (other backend Python files)
│   ├── migrations/
│   │   ├── schema.sql
│   │   └── me_api.db
│   ├── requirements.txt
│   ├── seed_data.py
│   └── runtime.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── readme.md
```
***

## Quickstart

### 1. Backend (FastAPI)

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python seed_data.py
uvicorn app.main:app --reload        # Local dev
# Or deploy to Railway for production
```
- By default, API serves on http://localhost:8000 (`/docs` for Swagger UI).

### 2. Frontend (HTML/CSS/JS)

Just open `frontend/index.html` in your browser for local preview.
- For live usage, deploy `frontend/` with Vercel or Netlify.

***

## API Reference

Automatic interactive docs:
- `/docs` for Swagger (OpenAPI)
- `/profile`, `/skills`, `/projects`, `/search`, etc.

***

## Deployment

- **Backend:** Deploy `/backend` on Railway. Make sure to set Root Directory = `backend` and Custom Start Command = `uvicorn app.main:app --host 0.0.0.0 --port $PORT`. Use `runtime.txt` to pin Python 3.11.
- **Frontend:** Deploy `/frontend` on Vercel or Netlify.
- Update `API_BASE` in `script.js` with your deployed backend URL.

***

## Data Model

- **Profile:** name, email, bio, phone, location, resume, links
- **Skills:** just skill names (no levels/years)
- **Projects:** title, description, tech_stack (array), links
- **Education, Work:** standard fields

***

## Seeding Real Data

Your profile, skills, and projects are seeded with your real resume information via `seed_data.py`.

***

## Limitations

- Database is SQLite (best for demo/small scale, not for production).
- No authentication—API is open for demo.
- No pagination, rate-limiting, or advanced error handling.
- For personal use/demo only!

***

## Credits

- Built by [Rupesh Bhusare](https://rupeshbhusare77.github.io/portfolio/)



