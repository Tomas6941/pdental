from flask import Flask, render_template, request, redirect

app = Flask(__name__)

content = {
    "titulo": "Clínica Dental Sonrisa Perfecta",
    "subtitulo": "Tecnología avanzada y atención personalizada",
    "tratamientos": [
        "Implantes",
        "Ortodoncia",
        "Blanqueamiento",
        "Endodoncia"
    ]
}

@app.route("/")
def home():
    return render_template("index.html", content=content)

@app.route("/admin", methods=["GET", "POST"])
def admin():
    global content
    if request.method == "POST":
        content["titulo"] = request.form["titulo"]
        content["subtitulo"] = request.form["subtitulo"]
        return redirect("/admin")

    return f'''
    <h2>Panel Admin</h2>
    <form method="POST">
        <input name="titulo" value="{content["titulo"]}">
        <input name="subtitulo" value="{content["subtitulo"]}">
        <button>Guardar</button>
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
