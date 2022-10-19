from flask import Flask, request
import requests
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1503@localhost/python(ass3)'
db = SQLAlchemy(app)
class nft_address(db.Model):
    adress_id = db.Column(db.Integer, primary_key=True)
    adress_itself = db.Column(db.String(100), unique=True)

    def __init__(self, adrdess_itself):
        self.adress_istself = adress_itself
    def __repr__(self):
        return '<nft_address %r>' % self.adress_itself

class nft_info(db.Model):
    adress_id = db.Column(db.Integer, primary_key=True)
    nftinfo_itself = db.Column(db.String(2000), unique=True)

    def __init__(self, nftinfo_itself):
        self.adress_istself = nftinfo_itself
    def __repr__(self):
        return '<nft_info %r>' % self.nftinfo_itself


@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        address=request.form.get('address')
        url = 'https://solana-gateway.moralis.io/nft/mainnet/' + address + '/metadata'
        headers = {
            "accept": "application/json",
            "X-API-Key": "iWXzBLaUXSfgBOJ5y8lmb9h5xAstww6nm2wkDTXOxsL1vLeoANc8njHGpnTrQWcM"
        }
        response = requests.get(url, headers=headers)
        print(response.text)
        return '''
                  <h1>The information about nft: {}</h1>'''.format(response.text)
    return '''
           <form method="POST">
               <div><label>address: <input type="text" name="address"></label></div>
               <input type="submit" value="Get Info">
           </form>'''
if __name__ == '__main__':
    app.run(debug=True, port=5000)