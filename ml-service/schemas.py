from pydantic import BaseModel, Field
from typing import Optional


class ExperienceEntry(BaseModel):
    title: str
    company: str
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    description: str


class ProjectEntry(BaseModel):
    name: str
    description: str
    tech_stack: list[str] = Field(default_factory=list)


class EducationEntry(BaseModel):
    institution: str
    degree: str
    year: Optional[str] = None


class ResumeProfile(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    skills: list[str] = Field(default_factory=list)
    experience: list[ExperienceEntry] = Field(default_factory=list)
    projects: list[ProjectEntry] = Field(default_factory=list)
    education: list[EducationEntry] = Field(default_factory=list)