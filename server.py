from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

# We only need this for local development.
if __name__ == '__main__':
    app.debug = True
    app.run()
