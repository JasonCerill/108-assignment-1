import json 
from flask import Flask 
from autobio import me
from mock_data import catalog



app = Flask('whoknows')

@app.route("/", methods=['GET'])
def home():
    return "WhoKnows?"

@app.route("/about")
def about():
   
    
    return me["first"] + " " + me["last"]


@app.route("/myaddress")
def address():
    return f'Address:  {me["address"]["street"]} {me["address"]["number"]} '



################ API ENDPOINTS ############

#  Postman --> test endpoints of REST API's


@app.route("/api/catalog", methods=["Get"])
def get_catalog():
    return json.dumps(catalog)

@app.route("/api/catalog/inventory", methods=["Get"])
def get_inventory():

        inventory = len(catalog)

        return json.dumps(inventory)


@app.route("/api/product/<id>", methods=["Get"])
def get_product(id):
    return json.dumps(id)


app.run(debug=True)