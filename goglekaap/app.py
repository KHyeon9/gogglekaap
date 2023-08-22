from flask import Flask
app = Flask(__name__)

print("__name__", __name__)
print("DEBUG", app.config["DEBUG"])


@app.route('/')
def index():
    return "Hello, World!"

if __name__ == "__main__":
    print("run")
    app.run(debug=True)