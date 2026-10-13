from flask import Flask, request, render_template, jsonify
from engine.modules.main_class import Main
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__, template_folder="front-end", static_folder="front-end/css", static_url_path="/css")


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/consulta")
def consulta():
    username = request.form.get("username")
    email = request.form.get("email")
    cpf = request.form.get("cpf")
    resultado = Main(username=username, email=email, cpf=cpf).execute()
    return jsonify(resultado)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)