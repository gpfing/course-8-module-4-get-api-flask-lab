from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Products API!", "resource_endpoint": "/products"}), 200

# TODO: Implement GET /products route that returns all products or filters by category

@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")
    if category:
        filtered_products = [p for p in products if p["category"].lower() == category.lower()]
        return jsonify(filtered_products), 200
    return jsonify(products), 200

# TODO: Implement GET /products/<id> route that returns a specific product by ID or 404

@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    for product in products:
        if product["id"] == id:
            return jsonify(product), 200
    return jsonify({"message": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
