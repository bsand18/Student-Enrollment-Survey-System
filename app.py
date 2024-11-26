from flask import Flask, request, render_template, jsonify
import pandas as pd
import os
from werkzeug.utils import secure_filename
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', os.urandom(24))  
csrf = CSRFProtect(app)

data_file = './data/survey_data.xlsx'


if not os.path.exists('./data'):
    os.makedirs('./data')

if not os.path.exists(data_file):
    df = pd.DataFrame(columns=[
        'First Name', 'Last Name', 'Email', 'Organization',
        'Job Responsibilities', 'Location', 'Coding', 'Requirements',
        'Testing', 'UI Design', 'Project Management', 'Experience'
    ])
    df.to_excel(data_file, index=False)

@app.route('/')
def survey_form():
    skills = ['Coding', 'Requirements', 'Testing', 'UI Design', 'Project Management']
    ranks = range(1, 6)
    return render_template('survey_form.html', skills=skills, ranks=ranks)


@app.route('/submit', methods=['POST'])
def submit_response():
    form_data = {
        'First Name': secure_filename(request.form.get('first_name')),
        'Last Name': secure_filename(request.form.get('last_name')),
        'Email': request.form.get('email'),
        'Organization': secure_filename(request.form.get('organization')),
        'Job Responsibilities': secure_filename(request.form.get('responsibilities')),
        'Location': secure_filename(request.form.get('location')),
        'Coding': request.form.get('coding'),
        'Requirements': request.form.get('requirements'),
        'Testing': request.form.get('testing'),
        'UI Design': request.form.get('ui_design'),
        'Project Management': request.form.get('project_management'),
        'Experience': secure_filename(request.form.get('experience')),
    }

    df = pd.read_excel(data_file)
    df = pd.concat([df, pd.DataFrame([form_data])], ignore_index=True)
    df.to_excel(data_file, index=False)

    return jsonify({'message': 'Your response has been successfully submitted!'})

if __name__ == '__main__':
    app.run(debug=True)


