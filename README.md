# Job Application Tracker

Beginner-level project using Python, Flask, HTML, CSS, basic Jinja, MySQL and REST API.

## Features
- Add application
- View applications
- Edit application
- Delete application
- Track status
- REST API: GET, POST, PUT, DELETE

## Setup
1. Install Python and MySQL.
2. Run `database.sql` in MySQL.
3. Edit `database.py` and replace `YOUR_MYSQL_PASSWORD`.
4. Run `pip install -r requirements.txt`.
5. Run `python app.py`.
6. Open http://127.0.0.1:5000

## Basic Jinja used
`{{ value }}` displays a value.
`{% for job in jobs %} ... {% endfor %}` repeats HTML for each job.
