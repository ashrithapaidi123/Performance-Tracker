from flask import Flask, render_template, redirect, request, url_for, session, flash
from auth.login import login_user
from views.dashboard import render_dashboard, get_faculty_details, update_faculty_details

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        success, error_message = login_user(username, password)
        if success:
            return redirect(url_for('dashboard'))
        return render_template('login.html', error_message=error_message)
    return render_template('login.html')



@app.route('/dashboard')
def dashboard():
    user = session.get('user')
    if user and user['role'] == 'HOD':
        faculty_details = get_faculty_details()
        return render_template('hod_dashboard.html', faculty_details=faculty_details)
    elif user and user['role'] == 'faculty':
        return render_template('faculty_dashboard.html', user=user)
    return redirect(url_for('login'))

@app.route('/update_details', methods=['POST'])
def update_details():
    user = session.get('user')
    if user and user['role'] == 'faculty':
        data = request.form.to_dict()
        update_faculty_details(user['username'], data)
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
