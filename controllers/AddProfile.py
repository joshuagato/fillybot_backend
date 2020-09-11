from utilities.flask_configs import Resource, db, request, jsonify, make_response
from models.profile_model import Profile, profile_schema, profiles_schema

class AddProfile(Resource):
  def post(self):
    if request.method == 'POST':
      if request.is_json:
        user = request.json['user']
        profile_name = request.json['profile_name']
        firstname = request.json['firstname']
        lastname = request.json['lastname']
        address_1 = request.json['address_1']
        address_2 = request.json['address_2']
        city = request.json['city']
        state = request.json['state']
        zipcode = request.json['zipcode']
        phone = request.json['phone']
        email = request.json['email']
        card_number = request.json['card_number']
        card_name = request.json['card_name']
        card_expiry = request.json['card_expiry']
        card_cvv = request.json['card_cvv']

        new_profile = Profile(user, profile_name, firstname, lastname, address_1, address_2, city, state, zipcode, phone, email, card_number, card_name, card_expiry, card_cvv)
        db.session.add(new_profile)
        db.session.commit()
        data = {'success': True, 'schema': profile_schema.dump(new_profile)}
        return make_response(jsonify(data), 201)
      else:
        return make_response(jsonify({'success': False, 'message': 'Your request data must be jsonified'}))
    else:
      return make_response(jsonify({'success': False, 'message': 'Your request header must be put'}))