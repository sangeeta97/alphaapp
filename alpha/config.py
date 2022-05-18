import os


class Config:
    SECRET_KEY = '970c72c08a7ef6e5cc562932'
    
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
