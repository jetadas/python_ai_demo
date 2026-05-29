from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_flask():
    return "<h1>Hello from Flask!</h1><p>This is a simple Flask application.</p>"

if __name__ == '__main__':
    app.run(debug=True)
