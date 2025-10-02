from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Endpoints de los otros servicios
USUARIOS_URL = "http://usuarios:5000/usuarios"
INVENTARIO_URL = "http://inventario:5002/inventario"

# Datos simulados de pedidos
pedidos = [
    {"id": 101, "usuarioId": 1, "productoId": 2, "cantidad": 2},
    {"id": 102, "usuarioId": 2, "productoId": 1, "cantidad": 1}
]

@app.route("/pedidos", methods=["GET"])
def get_pedidos():
    try:
        usuarios = requests.get(USUARIOS_URL).json()
        inventario = requests.get(INVENTARIO_URL).json()
    except Exception as e:
        return jsonify({"error": f"No se pudieron obtener datos externos: {str(e)}"}), 500

    usuarios_dict = {u["id"]: u for u in usuarios}
    inventario_dict = {p["id"]: p for p in inventario}

    respuesta = []
    for p in pedidos:
        usuario = usuarios_dict.get(p["usuarioId"], {"id": p["usuarioId"], "nombre": "Desconocido"})
        producto = inventario_dict.get(p["productoId"], {"id": p["productoId"], "nombre": "No encontrado", "stock": 0})
        respuesta.append({
            "pedidoId": p["id"],
            "usuario": usuario,
            "producto": producto,
            "cantidad": p["cantidad"],
            "estado": "Confirmado" if producto.get("stock", 0) >= p["cantidad"] else "Pendiente"
        })

    return jsonify(respuesta)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "service": "pedidos"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
