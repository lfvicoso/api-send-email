import unittest
from app import app

class EmailTestCase(unittest.TestCase):
    def setUp(self):
        # Configura o cliente de teste da aplicação
        self.app = app.test_client()
        self.app.testing = True

    def test_send_email_success(self):
        # Teste para verificar se o e-mail é enviado com sucesso
        response = self.app.post('/send-email', json={
            'to': 'test@example.com',
            'subject': 'Test Subject',
            'body': 'Test Body'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Email sent successfully', response.data)

    def test_send_email_missing_fields(self):
        # Teste para verificar o comportamento quando campos obrigatórios estão ausentes
        response = self.app.post('/send-email', json={
            'to': 'test@example.com',
            'subject': 'Test Subject'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Missing required fields', response.data)

    def test_send_email_invalid_email(self):
        # Teste para verificar o comportamento com um e-mail inválido
        response = self.app.post('/send-email', json={
            'to': 'invalid-email',
            'subject': 'Test Subject',
            'body': 'Test Body'
        })
        self.assertEqual(response.status_code, 500)
if __name__ == '__main__':
    unittest.main()
