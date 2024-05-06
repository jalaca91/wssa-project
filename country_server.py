# This file creates the server 
# Is the component that manages incoming HTTP requests and directs them to the appropriate view functions for processing

from flask import Flask, request, jsonify, abort, send_file
from countryDAO import CountriesDAO

app = Flask(__name__, static_url_path="", static_folder="static")

@app.route("/")
def index():
    return send_file("countryViewer.html")

# Create operation
# curl -X POST -H "Content-Type: application/json" -d "{\"country\":\"TestCountry\", \"capital\":\"TestCapital\", \"continent\":\"TestContinent\", \"currency\":\"TestCurrency\"}" http://127.0.0.1:5000/countries

@app.route("/countries", methods=["POST"])
def create_country():
    jsonstring = request.json
    if not all(key in jsonstring for key in ["country", "capital", "continent", "currency"]):
        abort(400) # If any of these fields are missing, the function aborts the request and returns a 400 error
    new_id = CountriesDAO().create(jsonstring)
    print(f"Country created, ID assigned: {new_id}")
    return jsonify({"id": new_id}), 201

# getall (Read operation)
# curl http://127.0.0.1:5000/countries

@app.route("/countries", methods=["GET"])
def get_all_countries():
    countries = CountriesDAO().getAll()
    print("GET request done, returning all countries")
    return jsonify(countries)

# Update operation
# curl -X PUT -H "Content-Type: application/json" -d "{"country":"UpdatedCountry", "capital":"UpdatedCapital", "continent":"UpdatedContinent", "currency":"UpdatedCurrency"}" http://127.0.0.1:5000/countries/1

@app.route("/countries/<int:id>", methods=["PUT"])
def update_country(id):
    jsonstring = request.json
    if not jsonstring:
        return jsonify({"error": "No data provided"}), 400

     # Included ID in the dictionary 
    jsonstring['ID'] = id  

    # Call update with a single dictionary that includes all the necessary attributes
    updated_country = CountriesDAO().update(jsonstring)
    if updated_country:
        print(f"Country updated: {id}")
        return jsonify(updated_country), 200
    else:
        return jsonify({"error": "Update failed"}), 500

# Delete operation
# curl -X DELETE http://127.0.0.1:5000/countries/1

@app.route("/countries/<int:id>", methods=["DELETE"])
def delete_country(id):
    return jsonify(CountriesDAO().delete(id))
 
# Find operation
# curl http://127.0.0.1:5000/countries/1

@app.route("/countries/<int:id>", methods=["GET"])
def find_country_by_id(id):
    country = CountriesDAO().findById(id)
    if country:
        return jsonify(country)
    else:
        abort(404)

# Running the server
if __name__ == "__main__":
    app.run(debug=True)



