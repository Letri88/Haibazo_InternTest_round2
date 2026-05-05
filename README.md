# Book Review Hub - Haibazo Intern Test Round 2

A modern full-stack web application for discovering and reviewing books.

## 🚀 Architecture
- **Frontend**: React (Deployed on Vercel)
- **Backend**: FastAPI (Deployed on Render)
- **Database**: PostgreSQL (Hosted on Render/Supabase)

## ✨ Features
- **Modern UI**: Sleek dark mode design with glassmorphism and animations.
- **Auto-Seeding**: The database automatically populates with classic books on the first run.
- **Responsive**: Works perfectly on mobile, tablet, and desktop.
- **RESTful API**: Fast and efficient backend powered by FastAPI and SQLAlchemy.

## 🛠️ Tech Stack
- **Frontend**: React.js, CSS3 (Vanilla), Axios.
- **Backend**: Python, FastAPI, SQLAlchemy, Pydantic.
- **Database**: PostgreSQL.
- **DevOps**: GitHub, Vercel, Render.

## 📦 Setup & Installation

### Backend
1. Navigate to the `backend` folder:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the server:
   ```bash
   uvicorn main:app --reload --port 8000
   ```

### Frontend
1. Navigate to the `frontend` folder:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm start
   ```

## 🌐 Deployment Instructions

### Backend (Render)
- Connect your GitHub repo.
- Set Root Directory to `backend`.
- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- Set Environment Variable `DATABASE_URL`.

### Frontend (Vercel)
- Connect your GitHub repo.
- Set Root Directory to `frontend`.
- Set Environment Variable `REACT_APP_API_URL` to your Render service URL.

---
Developed by **Le Tri** for Haibazo Intern Test.
