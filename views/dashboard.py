from flask import render_template
from models.user import User

faculty_details = [
    {
        "username": "Auadhati Datta",
        "personal_upskilling": 0,
        "works_submission": 0,
        "works_taken_up": 0,
        "works_completion": 0,
        "teaching_results": 0,
        "ot_leaves_permitted": 0,
        "invigilation_duties": 0
    },
    {
        "username": "N.Jaya Lalitha",
        "personal_upskilling": 0,
        "works_submission": 0,
        "works_taken_up": 0,
        "works_completion": 0,
        "teaching_results": 0,
        "ot_leaves_permitted": 0,
        "invigilation_duties": 0
    },
    {
        "username": "P.Vijay Bhaskar",
        "personal_upskilling": 0,
        "works_submission": 0,
        "works_taken_up": 0,
        "works_completion": 0,
        "teaching_results": 0,
        "ot_leaves_permitted": 0,
        "invigilation_duties": 0
    },
    {
        "username": "J.Peter Praveen",
        "personal_upskilling": 0,
        "works_submission": 0,
        "works_taken_up": 0,
        "works_completion": 0,
        "teaching_results": 0,
        "ot_leaves_permitted": 0,
        "invigilation_duties": 0
    },
    {
        "username": "A.Venkatesh",
        "personal_upskilling": 0,
        "works_submission": 0,
        "works_taken_up": 0,
        "works_completion": 0,
        "teaching_results": 0,
        "ot_leaves_permitted": 0,
        "invigilation_duties": 0
    },
    {
        "username": "B.Prameela",
        "personal_upskilling": 0,
        "works_submission": 0,
        "works_taken_up": 0,
        "works_completion": 0,
        "teaching_results": 0,
        "ot_leaves_permitted": 0,
        "invigilation_duties": 0
    },
    {
        "username": "K.K.Deepika",
        "personal_upskilling": 0,
        "works_submission": 0,
        "works_taken_up": 0,
        "works_completion": 0,
        "teaching_results": 0,
        "ot_leaves_permitted": 0,
        "invigilation_duties": 0
    },
    {
        "username": "B.Eekshita",
        "personal_upskilling": 0,
        "works_submission": 0,
        "works_taken_up": 0,
        "works_completion": 0,
        "teaching_results": 0,
        "ot_leaves_permitted": 0,
        "invigilation_duties": 0
    },
    {
        "username": "P.Deekshitha",
        "personal_upskilling": 0,
        "works_submission": 0,
        "works_taken_up": 0,
        "works_completion": 0,
        "teaching_results": 0,
        "ot_leaves_permitted": 0,
        "invigilation_duties": 0
    },
    {
        "username": "N.Mani kumari",
        "personal_upskilling": 0,
        "works_submission": 0,
        "works_taken_up": 0,
        "works_completion": 0,
        "teaching_results": 0,
        "ot_leaves_permitted": 0,
        "invigilation_duties": 0
    }
]

def render_dashboard(user):
    if user['role'] == 'HOD':
        return render_hod_dashboard()
    elif user['role'] == 'faculty':
        return render_faculty_dashboard(user)

def render_hod_dashboard():
    return render_template('hod_dashboard.html', faculty_details=faculty_details)

def render_faculty_dashboard(user):
    for faculty in faculty_details:
        if faculty['username'] == user['username']:
            return render_template('faculty_dashboard.html', user=faculty)
    return render_template('faculty_dashboard.html', user=user)

def get_faculty_details():
    return faculty_details

def update_faculty_details(username, data):
    for faculty in faculty_details:
        if faculty['username'] == username:
            faculty.update(data)
            break
        