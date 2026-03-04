from flask import Flask, render_template, request
from database import init_db, guardar_grup, carregar_grup

# Creem l'aplicacio Flask
app = Flask(__name__)

# Inicialitzem la base de dades si encara no existeix
init_db()

# Ruta principal de la web. Accepta GET i POST
@app.route("/", methods=["GET", "POST"])
def index():
    # Si s'envia el formulari, rebem les dades
    if request.method == "POST":
        noms_text = request.form.get("noms")
        if noms_text:
            # Separem els noms escrits per comes
            grup = [nom.strip() for nom in noms_text.split(",")]
            # Guardem la llista a la base de dades
            guardar_grup(grup)

    # Carreguem els noms guardats per mostrar-los a la vista
    grup = carregar_grup()
    return render_template("index.html", grup=grup)


if __name__ == "__main__":
    # Executem el servidor Flask al port 8000
    app.run(host="0.0.0.0", port=8000, debug=False)
