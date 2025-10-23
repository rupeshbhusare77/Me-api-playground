from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Profile(Base):
    __tablename__ = "profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    bio = Column(Text)
    phone = Column(String)
    location = Column(String)
    resume_link = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    skills = relationship("Skill", back_populates="profile", cascade="all, delete-orphan")
    projects = relationship("Project", back_populates="profile", cascade="all, delete-orphan")
    work = relationship("Work", back_populates="profile", cascade="all, delete-orphan")
    education = relationship("Education", back_populates="profile", cascade="all, delete-orphan")
    links = relationship("Link", back_populates="profile", cascade="all, delete-orphan")

class Skill(Base):
    __tablename__ = "skills"
    
    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey("profiles.id"))
    name = Column(String, nullable=False)
    level = Column(String)
    years_experience = Column(Integer)
    
    profile = relationship("Profile", back_populates="skills")

class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey("profiles.id"))
    title = Column(String, nullable=False)
    description = Column(Text)
    tech_stack = Column(JSON)
    github_link = Column(String)
    live_link = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    
    profile = relationship("Profile", back_populates="projects")

class Work(Base):
    __tablename__ = "work"
    
    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey("profiles.id"))
    company = Column(String, nullable=False)
    position = Column(String)
    description = Column(Text)
    start_date = Column(String)
    end_date = Column(String)
    
    profile = relationship("Profile", back_populates="work")

class Education(Base):
    __tablename__ = "education"
    
    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey("profiles.id"))
    institution = Column(String, nullable=False)
    degree = Column(String)
    field = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    
    profile = relationship("Profile", back_populates="education")

class Link(Base):
    __tablename__ = "links"
    
    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey("profiles.id"))
    platform = Column(String)
    url = Column(String)
    
    profile = relationship("Profile", back_populates="links")
