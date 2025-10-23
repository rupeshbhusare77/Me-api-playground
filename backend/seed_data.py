from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app import models

models.Base.metadata.create_all(bind=engine)

def seed():
    db = SessionLocal()
    
    # Clear existing
    db.query(models.Link).delete()
    db.query(models.Education).delete()
    db.query(models.Work).delete()
    db.query(models.Project).delete()
    db.query(models.Skill).delete()
    db.query(models.Profile).delete()
    
    # Create profile
    prof = models.Profile(
        name="Allmight",
        email="your.email@example.com",
        bio="Computer Science student passionate about software development, machine learning, and cybersecurity",
        phone="+91-XXXXXXXXXX",
        location="India",
        resume_link="https://your-resume-link.com"
    )
    db.add(prof)
    db.commit()
    db.refresh(prof)
    
    # Skills
    skills_data = [
        {"name": "Python", "level": "Advanced", "years_experience": 3},
        {"name": "Flutter", "level": "Advanced", "years_experience": 2},
        {"name": "Dart", "level": "Advanced", "years_experience": 2},
        {"name": "FastAPI", "level": "Intermediate", "years_experience": 1},
        {"name": "Machine Learning", "level": "Intermediate", "years_experience": 2},
        {"name": "Cryptography", "level": "Intermediate", "years_experience": 1},
        {"name": "Pine Script", "level": "Advanced", "years_experience": 1},
        {"name": "Java", "level": "Intermediate", "years_experience": 2},
        {"name": "C", "level": "Intermediate", "years_experience": 2},
    ]
    
    for s in skills_data:
        skill = models.Skill(profile_id=prof.id, **s)
        db.add(skill)
    
    # Projects
    projects_data = [
        {
            "title": "Flutter Expense Sharing App",
            "description": "Comprehensive expense-sharing application with Google Sign-In, trip management, expense tracking, and payback calculations",
            "tech_stack": ["Flutter", "Dart", "Firebase", "Google Sign-In"],
            "github_link": "https://github.com/yourusername/expense-app",
            "start_date": "2025-08",
            "end_date": "2025-08"
        },
        {
            "title": "OCR Receipt Scanner",
            "description": "Receipt scanning system using Python and Tesseract with preprocessing for bill analysis",
            "tech_stack": ["Python", "Tesseract", "OpenCV", "Azure"],
            "github_link": "https://github.com/yourusername/ocr-scanner",
            "start_date": "2025-08",
            "end_date": "2025-08"
        },
        {
            "title": "Trading Indicators - Pine Script",
            "description": "Advanced TradingView indicators with buy/sell signals, liquidity sweep detection, and stop-loss calculations",
            "tech_stack": ["Pine Script", "TradingView"],
            "github_link": "https://github.com/yourusername/trading-indicators",
            "start_date": "2025-07",
            "end_date": "2025-07"
        },
        {
            "title": "ChipWhisperer Security Analysis",
            "description": "Side-channel analysis project using ChipWhisperer Nano for security research and power analysis",
            "tech_stack": ["Python", "Jupyter", "ChipWhisperer", "C"],
            "github_link": "https://github.com/yourusername/chipwhisperer-analysis",
            "start_date": "2025-09",
            "end_date": "2025-09"
        }
    ]
    
    for p in projects_data:
        proj = models.Project(profile_id=prof.id, **p)
        db.add(proj)
    
    # Education
    edu = models.Education(
        profile_id=prof.id,
        institution="Your University Name",
        degree="Bachelor of Technology",
        field="Computer Science",
        start_date="2022",
        end_date="2026"
    )
    db.add(edu)
    
    # Work
    work = models.Work(
        profile_id=prof.id,
        company="IUDX",
        position="Software Developer (Applied)",
        description="Applied for software development role",
        start_date="2025-09",
        end_date="Present"
    )
    db.add(work)
    
    # Links
    links_data = [
        {"platform": "github", "url": "https://github.com/yourusername"},
        {"platform": "linkedin", "url": "https://linkedin.com/in/yourusername"},
        {"platform": "portfolio", "url": "https://yourportfolio.com"},
    ]
    
    for l in links_data:
        link = models.Link(profile_id=prof.id, **l)
        db.add(link)
    
    db.commit()
    print("✅ Database seeded successfully!")

if __name__ == "__main__":
    seed()
