# Email Service API

Este é um microserviço simples para envio de e-mails utilizando uma API RESTful. O serviço foi desenvolvido em Python utilizando Flask e permite enviar e-mails através de uma rota HTTP POST.

## Estrutura do Projeto

email_service/
├── app.py
├── config.py
├── controllers/
│   └── email_controller.py
├── services/
│   └── email_service.py
├── routes/
│   └── email_route.py
├── tests/
│   └── test_email.py
├── requirements.txt
└── swagger.yaml

## Requisitos

- Python 3.12 ou superior
- Pip (gerenciador de pacotes do Python)

## Instalação

1. **Clone o repositório:**

   git clone https://github.com/seu-usuario/email-service.git
   cd email-service

2. **Instale as dependências:**

   pip install --break-system-packages -r requirements.txt

3. **Configuração:**

   Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

   EMAIL_HOST=smtp.example.com
   EMAIL_PORT=587
   EMAIL_HOST_USER=your_email@example.com
   EMAIL_HOST_PASSWORD=your_password

   **Observação:** Use senhas específicas de aplicativo para contas com verificação em duas etapas ativada, caso vá usar GMAIL.

## Uso

1. **Inicie o servidor:**

   python3 app.py

2. **Envio de E-mail:**

   Faça uma requisição POST para a rota `/send-email` com o seguinte formato JSON:

   {
     "to": "destinatario@example.com",
     "subject": "Assunto do E-mail",
     "body": "Conteúdo do E-mail"
   }


## Testes

Para rodar os testes, execute:

python3 -m unittest discover -s tests


## Documentação da API

A documentação da API pode ser acessada em [http://localhost:5000/swagger.yaml](http://localhost:5000/swagger.yaml).

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).