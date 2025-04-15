from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Sample questions and answers about environmental sustainability
questions = [
    {
        "question": "What is the main cause of climate change?",
        "options": ["Deforestation", "Solar Energy", "Wind Energy"],
        "answer": "Deforestation"
    },
    {
        "question": "Which of these is a renewable resource?",
        "options": ["Coal", "Natural Gas", "Solar Energy"],
        "answer": "Solar Energy"
    },
    {
        "question": "What can you do to reduce waste?",
        "options": ["Recycle", "Burn Trash", "Use Plastic Bags"],
        "answer": "Recycle"
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/question')
def get_question():
    question = random.choice(questions)
    return jsonify(question)

if __name__ == '__main__':
    app.run(debug=True)
