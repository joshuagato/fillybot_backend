from utilities.flask_configs import Resource, db, request, jsonify, make_response
from models.profile_model import Profile, profile_schema, profiles_schema

class UpdateProfile(Resource):
  def put(self, id):
    fetched_profile = Profile.query.get(id)
    if not fetched_profile:
      return make_response(jsonify({'success': False, 'messgae': 'Profile not found'}), 401)

    if request.method == 'PUT':
      if request.is_json:
        fetched_profile.user = request.json['user']
        fetched_profile.profile_name = request.json['profile_name']
        fetched_profile.firstname = request.json['firstname']
        fetched_profile.lastname = request.json['lastname']
        fetched_profile.address = request.json['address']
        fetched_profile.city = request.json['city']
        fetched_profile.state = request.json['state']
        fetched_profile.zipcode = request.json['zipcode']
        fetched_profile.phone = request.json['phone']
        fetched_profile.email = request.json['email']
        db.session.commit()
        profile = profile_schema.dump(fetched_profile)
        return make_response(jsonify({'success': True, 'profile': profile}), 201)
      else:
        return make_response(jsonify({'success': False, 'message': 'Your request data must be jsonified'}))
    else:
      return make_response(jsonify({'success': False, 'message': 'Your request header must be put'}))