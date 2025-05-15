from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Estudiar es lo mejor que puedes hacer. Haz todas las prácticas y así podrás aprender más."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)