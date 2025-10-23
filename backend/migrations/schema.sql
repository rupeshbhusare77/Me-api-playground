-- Database Schema for Me-API Playground

CREATE TABLE profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    bio TEXT,
    phone VARCHAR(20),
    location VARCHAR(100),
    resume_link VARCHAR(255),
    created_at TIMESTAMP DEFAULT (datetime('now')),
    updated_at TIMESTAMP DEFAULT (datetime('now'))
);

CREATE TABLE skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    profile_id INTEGER NOT NULL,
    name VARCHAR(100) NOT NULL,
    level VARCHAR(20) CHECK (level IN ('Beginner', 'Intermediate', 'Advanced', 'Expert')),
    years_experience INTEGER CHECK (years_experience >= 0),
    created_at TIMESTAMP DEFAULT (datetime('now')),
    FOREIGN KEY (profile_id) REFERENCES profiles(id) ON DELETE CASCADE
);

CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    profile_id INTEGER NOT NULL,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    tech_stack TEXT, -- SQLite doesn't have native JSON, using TEXT instead
    github_link VARCHAR(255),
    live_link VARCHAR(255),
    start_date DATE,
    end_date DATE,
    created_at TIMESTAMP DEFAULT (datetime('now')),
    FOREIGN KEY (profile_id) REFERENCES profiles(id) ON DELETE CASCADE,
    CHECK (start_date <= end_date)
);

CREATE TABLE work (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    profile_id INTEGER NOT NULL,
    company VARCHAR(100) NOT NULL,
    position VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE,
    created_at TIMESTAMP DEFAULT (datetime('now')),
    FOREIGN KEY (profile_id) REFERENCES profiles(id) ON DELETE CASCADE,
    CHECK (start_date <= end_date)
);

CREATE TABLE education (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    profile_id INTEGER NOT NULL,
    institution VARCHAR(200) NOT NULL,
    degree VARCHAR(100) NOT NULL,
    field VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    created_at TIMESTAMP DEFAULT (datetime('now')),
    FOREIGN KEY (profile_id) REFERENCES profiles(id) ON DELETE CASCADE,
    CHECK (start_date <= end_date)
);

CREATE TABLE links (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    profile_id INTEGER NOT NULL,
    platform VARCHAR(50) NOT NULL,
    url VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT (datetime('now')),
    FOREIGN KEY (profile_id) REFERENCES profiles(id) ON DELETE CASCADE
);

-- Indexes for better query performance
CREATE INDEX idx_skills_profile ON skills(profile_id);
CREATE INDEX idx_projects_profile ON projects(profile_id);
CREATE INDEX idx_work_profile ON work(profile_id);
CREATE INDEX idx_education_profile ON education(profile_id);
CREATE INDEX idx_links_profile ON links(profile_id);