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
                address = request.json['address']
                city = request.json['city']
                state = request.json['state']
                zipcode = request.json['zipcode']
                phone = request.json['phone']
                email = request.json['email']

        new_profile = Profile(user, profile_name, firstname, lastname, address, city, state, zipcode, phone, email)
        db.session.add(new_profile)
        db.session.commit()
        data = {'success': True, 'schema': profile_schema.dump(new_profile)}
        return make_response(jsonify(data), 201)
