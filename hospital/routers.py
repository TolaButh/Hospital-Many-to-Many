from pydoc import doc
from turtle import title
from flask import render_template
from hospital import db, app
from hospital.models import Doctor, Patient
from flask import render_template, redirect, request, flash, url_for

@app.route("/")
def home():
    return render_template("index.html", title = "Hospital Management")

@app.route("/doctor")
def doctor():
    doctors = Doctor.query.all()
    
    return render_template('doctor.html', title = "Doctor", doctors = doctors)

@app.route("/add_doctor", methods=["POST", "GET"])
def add_doctor():
    
    if request.method == "POST":
        name = request.form['name']
        specialization = request.form['specialization']
        doctor = Doctor(name=name, specialization=specialization)
        db.session.add(doctor)
        db.session.commit()    
    
        return redirect(url_for('doctor'))



@app.route("/edit_doctor<int:id>", methods=["POST", "GET"])
def edit_doctor(id):
    doc = Doctor.query.get(id)
    doct = Doctor.query.all()
    if request.method == "POST":
        doc.name = request.form["name"]
        doc.specialization = request.form["specialization"]
        
        db.session.commit()
        return redirect(url_for("doctor"))
    
    
    return render_template("doctor.html", doct = doct ,title="Update Doctor",doc = doc)
    
@app.route("/patient")
def patient():
    patients = Patient.query.all()
    
    return render_template("patient.html", title = "Patient Page", patients = patients)

@app.route("/add_patient", methods=["POST", "GET"])
def add_patient():
    if request.method == "POST":
        name = request.form['name']
        insurance_num = request.form['insurance_num']
        sick = request.form["sick"]
        patient = Patient(name=name, insurance_num = insurance_num, sick = sick)
        db.session.add(patient)
        db.session.commit()    
        return redirect(url_for('patient'))
    

@app.route("/edit_patient<int:id>", methods=["POST", "GET"])
def edit_patient(id):
    patient = Patient.query.get(id)
    pat = Patient.query.all()
    if request.method == "POST":
        patient.name = request.form["name"]
        patient.insurance_num = request.form["insurance_num"]
        patient.sick = request.form["sick"]
        db.session.commit()
        return redirect(url_for("patient"))
    return render_template("patient.html", pat = pat ,title="Update Patient",patient = patient)

@app.route("/detail_doctor<int:id>")
def detail_doctor(id):
    d = Doctor.query.filter_by(id=id).first()
    
    return render_template("detail_doctor.html", title = "Detail Doctor" , d = d)


@app.route("/rigistration", methods=["POST", "GET"])
def rigistration():
    doctors = Doctor.query.all()
    patientes = Patient.query.all()
    if request.method == "POST":
        patient_name = request.form["patient_name"]
        doctor_name = request.form["doctor_name"]
        p = Patient.query.filter_by(name=patient_name).first()
        d = Doctor.query.filter_by(name=doctor_name).first()
        print(patient_name)
        print(doctor_name)
        
        d.patients.append(p)
        db.session.add(d)
        db.session.commit()
        
        return redirect(url_for("rigistration"))
    return render_template("rigistration.html", title = "Rigistration Book", doctors = doctors, patientes = patientes)



@app.route("/detail_patient<int:id>")
def detail_patient(id):
    pats = Patient.query.filter_by(id=id).first()
    
    return render_template("detail_patient.html", title = "Detail Patient" ,pats = pats)