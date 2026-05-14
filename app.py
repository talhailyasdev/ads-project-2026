from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # This represents your Week 1 Roadmap items
    roadmap_items = [
        {"step": "1", "task": "Project Initiation & ADS Documentation", "status": "Completed"},
        {"step": "2", "task": "Set up GitHub Repository & Branching Strategy", "status": "In Progress"},
        {"step": "3", "task": "Dockerize Python/Django Application", "status": "Pending"},
        {"step": "4", "task": "Configure Basic GitHub Actions Pipeline", "status": "Pending"},
        {"step": "5", "task": "Initial SAST Tool Integration (Bandit/SonarQube)", "status": "Pending"}
    ]
    # FAKE_AWS_KEY = "AKIAIOSFODNN7EXAMPLE"
    return render_template('index.html', tasks=roadmap_items)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)