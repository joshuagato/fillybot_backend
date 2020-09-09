from utilities.flask_configs import Resource, db, request, jsonify, make_response
from models.profile_model import Profile, profile_schema, profiles_schema

class DeleteProfile(Resource):
  def delete(self, id):
    oneprofile = Profile.query.get(id)
    if not oneprofile:
      return make_response(jsonify({'success': False, 'messgae': 'Profile not found'}), 401)

    db.session.delete(oneprofile)
    db.session.commit()

    profile = profile_schema.dump(oneprofile)
    return make_response(jsonify({'success': True, 'profile': profile}), 201)
