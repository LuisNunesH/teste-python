from flask import Flask, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD_HASH = generate_password_hash("senhaMaisSegura#910")

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Dados inválidos"}), 400

    username = data["username"]
    password = data["password"]

    if username == ADMIN_USERNAME and check_password_hash(ADMIN_PASSWORD_HASH, password):
        return jsonify({"message": "Acesso concedido"}), 200

    return jsonify({"error": "Credenciais inválidas"}), 401

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)

# Implementação de senha mais segura
# Dados no formato JSON
# Verificação de usuário e senha
# debug desativado (para evitar a exposição de informações sensíveis)
# Senhas armazenadas como hashes