from password_mail import app
from flask import Response


class TestPasswordMail:
    @staticmethod
    def init():
        return app.test_client()

    def test_password_mail_get(self):
        response: Response = self.init().get('/')
        assert "邮箱".encode() in response.get_data()

    def test_password_mail_post(self):
        response = self.init().post('/', data=dict(message='hi', email='1831353087@qq.com'))
        assert 'something is ok'.encode() == response.get_data()
