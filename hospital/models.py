from hospital import db

rigistrations = db.Table('rigistrations', 
    db.Column('doctor_id', db.Integer(), db.ForeignKey("doctor.id")),
    db.Column('patient_id', db.Integer(), db.ForeignKey("patient.id")))

class Doctor(db.Model):
   
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    specialization = db.Column(db.String(100), nullable=False)
    patients = db.relationship('Patient', secondary = rigistrations ,backref=db.backref('doctor', lazy="dynamic"), lazy='dynamic')
    
    def __repr__(self):
        return f"<Doctor: {self.name}>"
    
class Patient(db.Model):
  
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    insurance_num = db.Column(db.String(30), nullable=False)
    sick = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f"<Patient: {self.name}>"
    
    
        
    
