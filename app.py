from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    print("Yeeee")
    return 'Hello, Docker! Hoe gaat het. Deze code werkt op port 80'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)



