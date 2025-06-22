from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import plaid

load_dotenv()

app = Flask(__name__)
CORS(app)

client = plaid.Client(
    client_id=os.getenv("CLIENT_ID"),
    secret=os.getenv("SECRET"),
    environment='development'  # Use 'sandbox' if you're testing
)

@app.route('/create_link_token', methods=['GET'])
def create_link_token():
    response = client.LinkToken.create({
        'user': {'client_user_id': 'pedro-001'},
        'products': ['transactions'],
        'client_name': 'PedroFinanceGPT',
        'country_codes': ['US'],
        'language': 'en'
    })
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
