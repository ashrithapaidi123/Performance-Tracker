from flask import session
from models.user import User

faculty_members = {
    "Auadhati Datta": "12025",
    "N.Jaya Lalitha": "22025",
    "P.Vijay Bhaskar": "32025",
    "J.Peter Praveen": "42025",
    "A.Venkatesh": "52025",
    "B.Prameela": "62025",
    "K.K.Deepika": "72025",
    "B.Eekshita": "82025",
    "P.Deekshitha": "92025",
    "N.Mani kumari": "102025",
}

def login_user(username, password):
    if username in faculty_members and faculty_members[username] == password:
        user = User(username=username, password=password, role='faculty')
        session['user'] = user.__dict__  
        return True, None
    elif username == "hod" and password == "hod2025":
        user = User(username=username, password=password, role='HOD')
        session['user'] = user.__dict__ 
        return True, None
    return False, "WRONG USERNAME OR PASSWORD"
