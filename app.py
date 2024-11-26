from flask import Flask, request, render_template, jsonify
from flask_wtf.csrf import CSRFProtect
from werkzeug.utils import secure_filename
import sqlite3
import os

app = Flask(__name__)


app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', os.urandom(24))


csrf = CSRFProtect(app)


DATABASE = "survey_data.db"

def init_db():
   
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS survey_responses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                email TEXT,
                organization TEXT,
                job_responsibilities TEXT,
                location TEXT,
                coding INTEGER,
                requirements INTEGER,
                testing INTEGER,
                ui_design INTEGER,
                project_management INTEGER,
                experience TEXT
            )
        """)
        conn.commit()

init_db()

@app.route('/')
def survey_form():
   
    skills = ['Coding', 'Requirements', 'Testing', 'UI Design', 'Project Management']
    ranks = range(1, 6)
    return render_template('survey_form.html', skills=skills, ranks=ranks)

@app.route('/submit', methods=['POST'])
def submit_response():
    
    form_data = {
        'first_name': secure_filename(request.form.get('first_name')),
        'last_name': secure_filename(request.form.get('last_name')),
        'email': request.form.get('email'),
        'organization': secure_filename(request.form.get('organization')),
        'job_responsibilities': secure_filename(request.form.get('responsibilities')),
        'location': secure_filename(request.form.get('location')),
        'coding': request.form.get('coding'),
        'requirements': request.form.get('requirements'),
        'testing': request.form.get('testing'),
        'ui_design': request.form.get('ui_design'),
        'project_management': request.form.get('project_management'),
        'experience': secure_filename(request.form.get('experience')),
    }

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO survey_responses (
                first_name, last_name, email, organization,
                job_responsibilities, location, coding, requirements,
                testing, ui_design, project_management, experience
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, tuple(form_data.values()))
        conn.commit()

    return jsonify({'message': 'Your response has been successfully submitted!'})

if __name__ == '__main__':
    app.run(debug=True)
