from flask import Blueprint,render_template,url_for,request,flash,redirect,url_for
from .models import Patient,PatientMoreDetail
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET','POST'])
def login() :
    if request.method == 'POST' :
        email = request.form.get('email')
        password = request.form.get('password')

        patient = Patient.query.filter_by(email=email).first()
        if patient :
            if check_password_hash(patient.password, password) :
                flash('Logged in successfully!' ,category='success')
                login_user(patient, remember=True)
                return redirect(url_for('views.home'))
            else :
                flash('Incorrect passsword!! Try again.', category='error')

        else :
            flash('Email dosnt exist!', category='error')            
            
            
        
    return render_template('login.html' , patient=current_user)


@auth.route('/logout')
@login_required
def logout() :
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register', methods = ['GET','POST'])
def register() :
    if request.method == 'POST' :
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        patient = Patient.query.filter_by(email=email).first()
        if patient :
            flash('Email already exists!', category='error')

        elif len(email) < 4 :
            flash('Email must be greater than 3 character!', category='error')
        elif len(firstName) < 3 :
            flash('First Name must be greater than 2 character!', category='error')
        elif password1 != password2 :
            flash('Password dosnt Match!', category='error')
        elif len(password1) < 7 :
            flash('password must be greater than 6 character', category='error')
        else :
            new_patient = Patient(email = email, first_name = firstName, password=generate_password_hash(password1,method='sha256'))
            db.session.add(new_patient)
            db.session.commit()
            login_user(new_patient, remember=True)
            flash('Account Created!!', category='success')
            return redirect(url_for('views.home'))
    else :
        pass

    return render_template('sign_up.html' , patient=current_user)   

