from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app import models

models.Base.metadata.create_all(bind=engine)

def seed():
    db = SessionLocal()
    db.query(models.Link).delete()
    db.query(models.Education).delete()
    db.query(models.Work).delete()
    db.query(models.Project).delete()
    db.query(models.Skill).delete()
    db.query(models.Profile).delete()

    prof = models.Profile(
        name="Rupesh Bhusare",
        email="bhusare.hemant.22031@iitgoa.ac.in",
        bio="CSE undergrad at IIT Goa. Passionate about coding, creating visuals, and solving real-world problems. Enjoys exploring tech and expressing ideas through digital creativity.",
        phone="+91 9579624640",
        location="Kolhapur, Maharashtra, India",
        resume_link="https://drive.google.com/file/d/1Y7Sif3T51jAxJWQONthkYbiYhgblvOr_/view?usp=drive_link"
    )
    db.add(prof)
    db.commit()
    db.refresh(prof)

    skills_list = [
        "HTML5", "CSS3", "JavaScript", "React", "Tailwind", "Figma",
        "Node.js", "MongoDB", "Express", "MySQL", "Firebase",
        "C", "C++", "Python", "VHDL",
        "Git", "Postman", "AWS", "Linux", "VS Code",
        "Bash", "PowerShell", "AutoCAD", "Matlab", "LaTeX", "Wireshark", "Illustrator", "Photoshop"
    ]
    for sk in skills_list:
        db.add(models.Skill(profile_id=prof.id, name=sk))

    projects_data = [
        {
            "title": "Receipt Scanner",
            "description": "Developed a Python tool using Azure AI Document Intelligence to automatically extract and structure data from receipt images, exporting results to JSON and CSV. Includes parallel processing, network retries, and mathematical result validation.",
            "tech_stack": ["Python", "Azure AI", "OCR"],
            "github_link": "https://github.com/rupeshbhusare77/receipt-scanner",
            "live_link": ""
        },
        {
            "title": "GV Coding Scheme Extractor",
            "description": "Generator for coding schemes satisfying the Gilbert–Varshamov bound. Randomized matrix generation and theoretical research with responsive frontend.",
            "tech_stack": ["Cryptography", "Python", "HTML", "CSS", "JS"],
            "github_link": "https://github.com/rupeshbhusare77/gv-coding-scheme-extractor",
            "live_link": "https://gvcodingschemeextractor.pythonanywhere.com/"
        },
        {
            "title": "Multi Level Feedback Queue Simulator (MLFQ)",
            "description": "Visual simulator to demonstrate MLFQ CPU scheduling with dynamic queue management.",
            "tech_stack": ["Operating system", "Web", "Python"],
            "github_link": "https://github.com/vaibhavgupta856/Multi-Level-Feedback-Queue-Simulator",
            "live_link": "https://vaibhavgupta856.github.io/Multi-Level-Feedback-Queue-Simulator/"
        },
        {
            "title": "TCP Congestion Control",
            "description": "Simulation and analysis of TCP congestion control mechanisms using graphs and metrics.",
            "tech_stack": ["Computer Networks", "Python"],
            "github_link": "https://github.com/rupeshbhusare77/TCP-Congestion-control",
            "live_link": ""
        },
        {
            "title": "Portfolio Site",
            "description": "My personal portfolio, built with modern CSS & JS.",
            "tech_stack": ["Web Development", "HTML5", "CSS3", "JS"],
            "github_link": "https://github.com/rupeshbhusare77/portfolio",
            "live_link": "https://rupeshbhusare77.github.io/portfolio/"
        },
        {
            "title": "QuickClick App",
            "description": "Simple android game to test your reaction.",
            "tech_stack": ["Android Development", "Kotlin", "XML"],
            "github_link": "https://github.com/rupeshbhusare77/QuickClick_app",
            "live_link": ""
        }
    ]
    for p in projects_data:
        db.add(models.Project(profile_id=prof.id, **p))

    db.add(models.Education(
        profile_id=prof.id,
        institution="Indian Institute of Technology Goa",
        degree="BTech",
        field="Computer Science and Engineering",
        start_date="2022",
        end_date="Present"
    ))
    db.add(models.Education(
        profile_id=prof.id,
        institution="Shree Parashram Balaji Patil Highschool, Mudal",
        degree="Class 12, HSC board (Maharashtra)",
        field="Science",
        start_date="2020",
        end_date="2022"
    ))

    db.add(models.Work(
        profile_id=prof.id,
        company="IIT Goa",
        position="Graphic Designer Head (Newsletter), Core Member (Design Club)",
        description="Led campus design initiatives for the IIT Goa newsletter and core member organizing and leading hands-on design workshops.",
        start_date="2023",
        end_date="2024"
    ))

    db.add(models.Link(profile_id=prof.id, platform="github", url="https://github.com/rupeshbhusare77"))
    db.add(models.Link(profile_id=prof.id, platform="linkedin", url="https://www.linkedin.com/in/rupesh-bhusare-7ba246256/"))
    db.add(models.Link(profile_id=prof.id, platform="portfolio", url="https://rupeshbhusare77.github.io/portfolio/"))

    db.commit()
    print("✅ Database seeded with real portfolio data!")

if __name__ == "__main__":
    seed()
