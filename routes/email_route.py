
from flask import Blueprint
from controllers.email_controller import send_email_controller

email_bp = Blueprint('email', __name__)

email_bp.route('/send-email', methods=['POST'])(send_email_controller)
