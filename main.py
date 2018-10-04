from flask import Flask, render_template, jsonify

from cryptocurrencies import symbol_to_class_mapping

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html', title='CryptoAddresses', currencies=[s for s in symbol_to_class_mapping])


@app.route('/api/supported-currencies')
def supported_currencies():
    response = {
        "result": [{
            "symbol": s,
            "name": c.name
        } for s, c in symbol_to_class_mapping.items()]
    }
    return jsonify(response)


# Validate if the address is valid or not
@app.route('/api/validate-address/<currency>/<address>')
def is_address(currency: str, address: str):
    currency = currency.lower()
    response = {
        "result": {
            'is_valid': symbol_to_class_mapping[currency].is_address(address=address)
        }
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
