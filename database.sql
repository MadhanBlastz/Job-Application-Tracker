CREATE DATABASE IF NOT EXISTS job_tracker;
USE job_tracker;

CREATE TABLE IF NOT EXISTS applications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    company VARCHAR(100) NOT NULL,
    role VARCHAR(100) NOT NULL,
    location VARCHAR(100),
    salary VARCHAR(50),
    applied_date DATE,
    status VARCHAR(30) DEFAULT 'Applied'
);

INSERT INTO applications
(company, role, location, salary, applied_date, status)
VALUES
('TCS', 'Python Developer', 'Hyderabad', '4 LPA', '2026-09-20', 'Applied'),
('Infosys', 'Software Developer', 'Hyderabad', '4.5 LPA', '2026-09-18', 'Interview');
