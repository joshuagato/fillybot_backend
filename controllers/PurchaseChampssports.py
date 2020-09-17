from utilities.flask_configs import Resource, db, request, jsonify, make_response
from models.profile_model import Profile, profile_schema, profiles_schema
from sitecontrollers.Champssports import Champssports
champssports = Champssports()

class PurchaseChampssports(Resource):
  def post(self):
    if request.method == 'POST':
      if request.is_json:
        product_details = {
          'product_name': request.json['prod_name'], 'product_number': request.json['prod_number'],
          'product_size': request.json['prod_size'], 'product_quantity': request.json['prod_qty']
        }

        user_details = {
          'first_name': request.json['firstname'], 'last_name': request.json['lastname'],
          'address_1': request.json['address_1'], 'address_2': request.json['address_2'], 'city': request.json['city'],
          'state': request.json['state'] , 'zipcode': request.json['zipcode'],
          'phone': request.json['phone'], 'email': request.json['email'],
          'card_number': request.json['card_number'], 'card_holder': request.json['card_name'],
          'card_expiry': request.json['card_expiry'], 'card_cvv': request.json['card_cvv'],
        }

        taskId = request.json['taskId']

        response = champssports.generate_url(product_details, user_details, taskId)
        return make_response(jsonify(response), 200)
