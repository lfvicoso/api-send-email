
from flask import request, jsonify
from services.email_service import send_email

def send_email_controller():
    data = request.get_json()
    to = data.get('to')
    subject = data.get('subject')
    body = data.get('body')

    if not to or not subject or not body:
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        send_email(to, subject, body)
        return jsonify({'message': 'Email sent successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
