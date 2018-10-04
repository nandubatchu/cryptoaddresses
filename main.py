from flask import Flask, render_template, jsonify

from src import currencies_mapping

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html', title='CryptoAddresses',
                           currencies=[{
                               "symbol": symbol,
                               "name": currency_dict['name']
                           } for symbol, currency_dict in currencies_mapping.items()])


@app.route('/api/supported-currencies')
def supported_currencies():
    response = {
        "result": [{
            "symbol": symbol,
            "name": currency_dict['name']
        } for symbol, currency_dict in currencies_mapping.items()]
    }
    return jsonify(response)


# Validate if the address is valid or not
@app.route('/api/validate/<currency>/<address>')
def is_address(currency: str, address: str):
    currency = currency.lower()
    currency_mapping = currencies_mapping[currency]
    response = {
        "result": {
            'is_valid': currency_mapping['validation_method'](address=address, **currency_mapping.get('validation_args', {}))
        }
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
