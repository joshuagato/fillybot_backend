from utilities.flask_configs import Resource, request, jsonify, bcrypt
from models.user_model import User, user_schema, users_schema
# import jwt

class Login(Resource):
    def post(self):
        if request.method == 'POST':
            if request.is_json:
                email = request.json['email']
                password = request.json['password']

                matched_user = User.query.filter_by(email=email).first()
                if not matched_user:
                    return jsonify({ 'success': False, 'message': 'Check your username or password' });

                hashed_password = matched_user.password

                if not bcrypt.check_password_hash(hashed_password, password):
                    return jsonify({'success': False, 'message': 'Check your username or password'});

        # token = jwt.encode({'user': user_schema.dump(matched_user)}, 'supersecretivesecret', algorithm='HS256')

        # return jsonify({'success': True, 'user': user_schema.dump(matched_user), 'token': token.decode()})
        return jsonify({'success': True, 'user': user_schema.dump(matched_user)})
