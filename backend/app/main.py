from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional
from app import models, schemas
from app.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Me-API Playground", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/profile", response_model=schemas.Profile)
def get_profile(db: Session = Depends(get_db)):
    prof = db.query(models.Profile).first()
    if not prof:
        raise HTTPException(status_code=404, detail="Profile not found")
    return prof

@app.put("/profile", response_model=schemas.Profile)
def update_profile(profile: schemas.ProfileUpdate, db: Session = Depends(get_db)):
    prof = db.query(models.Profile).first()
    if not prof:
        raise HTTPException(status_code=404, detail="Profile not found")
    
    for key, value in profile.dict(exclude_unset=True).items():
        setattr(prof, key, value)
    
    db.commit()
    db.refresh(prof)
    return prof

@app.get("/projects", response_model=List[schemas.Project])
def get_projects(
    skill: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(models.Project)
    
    if skill:
        query = query.filter(models.Project.tech_stack.contains(skill))
    
    return query.all()

@app.get("/projects/{project_id}", response_model=schemas.Project)
def get_project(project_id: int, db: Session = Depends(get_db)):
    proj = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not proj:
        raise HTTPException(status_code=404, detail="Project not found")
    return proj

@app.post("/projects", response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    prof = db.query(models.Profile).first()
    if not prof:
        raise HTTPException(status_code=404, detail="Profile not found")
    
    db_project = models.Project(**project.dict(), profile_id=prof.id)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

@app.put("/projects/{project_id}", response_model=schemas.Project)
def update_project(
    project_id: int,
    project: schemas.ProjectUpdate,
    db: Session = Depends(get_db)
):
    db_proj = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not db_proj:
        raise HTTPException(status_code=404, detail="Project not found")
    
    for key, value in project.dict(exclude_unset=True).items():
        setattr(db_proj, key, value)
    
    db.commit()
    db.refresh(db_proj)
    return db_proj

@app.get("/skills", response_model=List[schemas.Skill])
def get_skills(db: Session = Depends(get_db)):
    return db.query(models.Skill).all()

@app.get("/skills/top", response_model=List[schemas.Skill])
def get_top_skills(limit: int = 5, db: Session = Depends(get_db)):
    return db.query(models.Skill).order_by(models.Skill.years_experience.desc()).limit(limit).all()

@app.get("/search")
def search(q: str = Query(...), db: Session = Depends(get_db)):
    projects = db.query(models.Project).filter(
        (models.Project.title.contains(q)) | 
        (models.Project.description.contains(q))
    ).all()
    
    skills = db.query(models.Skill).filter(models.Skill.name.contains(q)).all()
    
    return {
        "query": q,
        "projects": projects,
        "skills": skills
    }

@app.get("/work", response_model=List[schemas.Work])
def get_work(db: Session = Depends(get_db)):
    return db.query(models.Work).all()

@app.get("/education", response_model=List[schemas.Education])
def get_education(db: Session = Depends(get_db)):
    return db.query(models.Education).all()

@app.get("/links", response_model=List[schemas.Link])
def get_links(db: Session = Depends(get_db)):
    return db.query(models.Link).all()
