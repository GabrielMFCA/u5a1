from flask import Flask, request, render_template_string

app = Flask(__name__)

# Plantilla HTML para el formulario
html_form = """
<!doctype html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulario acceso al usuario</title>
</head>
<body>
    <h1>Bienvenida</h1>
    <form action="/" method="POST">
        <label for="nombre">Ingrese su nombre:</label>
        <input type="text" id="nombre" name="nombre" required>
        <button type="submit">Enviar</button>
    </form>
    {% if nombre %}
        <h2>¡Bienvenido, {{ nombre }}!</h2>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def formulario():
    nombre = None
    if request.method == "POST":
        nombre = request.form.get("nombre")
    return render_template_string(html_form, nombre=nombre)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
