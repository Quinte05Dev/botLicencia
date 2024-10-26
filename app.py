from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista de licencias válidas
licenses = [
    {"license_key": "EENDJSASSSFSASM", "email": "quinte05dev@gmail.com"}
]

@app.route('/validar_licencia', methods=['POST'])
def validar_licencia():
    data = request.json
    license_key = data.get("license_key")
    email = data.get("email")

    for license in licenses:
        if license["license_key"] == license_key and license["email"] == email:
            return jsonify({"status": "Licencia Válida"}), 200
    
    return jsonify({"status": "Licencia Inválida"}), 404

if __name__ == "__main__":
    app.run(port=5000)
