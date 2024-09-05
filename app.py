
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, TEKS, Question
from question_generator import QuestionFactory
import csv
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teks_questions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_question', methods=['POST'])
def generate_question():
    teks_id = request.form.get('teks_id')
    question_type = request.form.get('question_type')
    
    teks = TEKS.query.get(teks_id)
    if not teks:
        return jsonify({'error': 'TEKS not found'}), 404
    
    openai_api_key = os.environ.get('OPENAI_API_KEY')
    if not openai_api_key:
        return jsonify({'error': 'OpenAI API key not set'}), 500
    
    question_factory = QuestionFactory()
    question = question_factory.create_question(question_type, teks.description, openai_api_key)
    generated_question = question.generate()
    
    new_question = Question(
        teks_id=teks_id,
        question_text=generated_question,
        question_type=question_type,
        options=None,  # You may want to parse options from the generated question
        correct_answer=None  # You may want to determine the correct answer
    )
    db.session.add(new_question)
    db.session.commit()
    
    return jsonify({'question': generated_question})

@app.route('/load_teks', methods=['POST'])
def load_teks():
    file = request.files['file']
    if file and file.filename.endswith('.csv'):
        csv_content = file.read().decode('utf-8').splitlines()
        csv_reader = csv.DictReader(csv_content)
        for row in csv_reader:
            teks = TEKS(standard=row['standard'], description=row['description'])
            db.session.add(teks)
        db.session.commit()
        return jsonify({'message': 'TEKS data loaded successfully'})
    return jsonify({'error': 'Invalid file format'}), 400

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
