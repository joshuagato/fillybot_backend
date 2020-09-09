from utilities.flask_configs import Resource, request, jsonify, db, bcrypt, make_response
from models.user_model import User, user_schema, users_schema

class Register(Resource):
  def post(self):
    if request.method == 'POST':
      if request.is_json:
        firstname = request.json['firstname']
        lastname = request.json['lastname']
        email = request.json['email']
        password = request.json['password']
        repassword = request.json['repassword']
        hashed_password = bcrypt.generate_password_hash(password)

        matched_user = User.query.filter_by(email=email).first()
        if matched_user:
          return jsonify({'success': False, 'message': 'An account already exists with this email.'})

        new_user = User(firstname, lastname, email, hashed_password)
        db.session.add(new_user)
        db.session.commit()
        data = {'success': True, 'message': 'Successfully Registered', 'user': user_schema.dump(new_user)}
        return make_response(jsonify(data), 201)
