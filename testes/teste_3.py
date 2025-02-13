from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/saudacao', methods=['GET'])
def saudacao():
    nome = request.args.get('nome', 'visitante')
    mensagem = f"Oi, {nome}! Bem-vindo!"
    return jsonify({"mensagem": mensagem})

@app.route('/soma', methods=['POST'])
def soma():
    dados = request.get_json()
    if not dados or 'numero1' not in dados or 'numero2' not in dados:
        return jsonify({"erro": "JSON inválido. Envie dois números válidos."}), 400

    num1 = dados['numero1']
    num2 = dados['numero2']
    resultado = num1 + num2
    return jsonify({"soma": resultado})

if __name__ == '__main__':
    app.run(debug=True)