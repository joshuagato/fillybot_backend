import jwt

def verify_token(token):
    try:
        matched = jwt.decode(token, 'supersecretivesecret', algorithms=['HS256'])
        matched.update({ 'success': True })
        return matched
    except Exception as e:
        return { 'success': False, 'message': e }
