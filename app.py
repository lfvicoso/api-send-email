
from flask import Flask
from routes.email_route import email_bp
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.register_blueprint(email_bp)

# Configuração do Swagger UI
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'  # O caminho para o arquivo YAML da especificação Swagger
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "Email Service API"})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True)
