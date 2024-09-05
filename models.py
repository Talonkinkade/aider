from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TEKS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    standard = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teks_id = db.Column(db.Integer, db.ForeignKey('teks.id'), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    question_type = db.Column(db.String(50), nullable=False)
    options = db.Column(db.JSON)
    correct_answer = db.Column(db.Text, nullable=False)
    
    teks = db.relationship('TEKS', backref=db.backref('questions', lazy=True))
