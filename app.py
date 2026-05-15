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
    return render_template('index.html', tasks=roadmap_items)

# --- NEW: OWASP ZAP VULNERABILITY REMEDIATION ---
@app.after_request
def add_security_headers(response):
    # Fix 1: Content Security Policy (CSP) Header Not Set
    response.headers['Content-Security-Policy'] = "default-src 'self'; style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net;"
    
    # Fix 2: Missing Anti-clickjacking Header
    response.headers['X-Frame-Options'] = 'DENY'
    
    # Fix 3: X-Content-Type-Options Header Missing
    response.headers['X-Content-Type-Options'] = 'nosniff'
    
    # Fix 4: Hide Server Version Information
    response.headers['Server'] = 'Secure Server'
    
    return response
# ------------------------------------------------

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)