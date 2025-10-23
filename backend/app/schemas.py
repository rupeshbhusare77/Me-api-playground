from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class SkillBase(BaseModel):
    name: str
    level: Optional[str] = None
    years_experience: Optional[int] = None

class SkillCreate(SkillBase):
    pass

class Skill(SkillBase):
    id: int
    profile_id: int
    
    class Config:
        from_attributes = True

class ProjectBase(BaseModel):
    title: str
    description: Optional[str] = None
    tech_stack: Optional[List[str]] = None
    github_link: Optional[str] = None
    live_link: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    profile_id: int
    
    class Config:
        from_attributes = True

class WorkBase(BaseModel):
    company: str
    position: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None

class Work(WorkBase):
    id: int
    profile_id: int
    
    class Config:
        from_attributes = True

class EducationBase(BaseModel):
    institution: str
    degree: Optional[str] = None
    field: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None

class Education(EducationBase):
    id: int
    profile_id: int
    
    class Config:
        from_attributes = True

class LinkBase(BaseModel):
    platform: str
    url: str

class Link(LinkBase):
    id: int
    profile_id: int
    
    class Config:
        from_attributes = True

class ProfileBase(BaseModel):
    name: str
    email: str
    bio: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    resume_link: Optional[str] = None

class ProfileCreate(ProfileBase):
    pass

class ProfileUpdate(ProfileBase):
    pass

class Profile(ProfileBase):
    id: int
    created_at: datetime
    updated_at: datetime
    skills: List[Skill] = []
    projects: List[Project] = []
    work: List[Work] = []
    education: List[Education] = []
    links: List[Link] = []
    
    class Config:
        from_attributes = True
