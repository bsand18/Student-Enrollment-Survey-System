Make sure we have Node.js installed before running
Go to the Node.js official website.  https://nodejs.org/en

Download the LTS (Long Term Support) version, which is suitable for most projects.

During the installation:

Make sure to check Add to PATH, which will automatically add Node.js to the system environment variables.

When runing in new pc 
Check if the virtual environment is complete
Confirm that the virtual environment is created correctly:

Check if the python.exe and pip.exe files exist in the venv\Scripts directory.
If the files are missing, you need to recreate the virtual environment.
Delete and recreate the virtual environment:

Delete the current virtual environment folder venv.
Run the following command in the project directory to recreate the virtual environment:
powershell
Copy code
python -m venv venv
Activate the virtual environment:

Windows:
powershell
Copy code
.\venv\Scripts\activate
If the problem persists, proceed to the next step.
2. Move the project to a space-free path
Spaces in the path may cause command execution to fail. It is recommended to move the project to a space-free directory. For example:

Create a new directory:
powershell
Copy code
mkdir C:\Projects

How to run in local?
Create a Virtual Environment and Install Dependencies: Run the following commands in your terminal:

python -m venv venv
source venv/bin/activate  # For Windows, use venv\Scripts\activate
pip install flask pandas openpyxl
Run the Application: Start the Flask application by running:

python app.py
View the Form Page in Your Browser: Open your browser and navigate to:

http://127.0.0.1:5000
You should now see the form page.

Example ![image](https://github.com/user-attachments/assets/72557727-3a9f-4bdc-b353-5e5ec720db44)

Example ![image](https://github.com/user-attachments/assets/4f2666eb-531c-4a8f-ae36-b08f5c71c8d2)


