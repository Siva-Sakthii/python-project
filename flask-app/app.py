from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', message="Welcome to my EC2 Hosted Flask App!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
