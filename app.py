import fundamentus

from flask import Flask, request, jsonify
from flask_cors import CORS
# from fundamentus import get_data

app = Flask(__name__)
CORS(app)
def get_company_data(ticker):
    try:
        data = fundamentus.get_papel(ticker)
        return data.to_dict(orient='records')[0]
    except Exception as e:
        return {'erro': str(e)}

@app.route('/get_company', methods=['GET'])
def get_company():
    ticker = request.args.get('ticker')
    company_data = get_company_data(ticker)
    return jsonify(company_data)

if __name__ == '__main__':
    app.run(debug=True)