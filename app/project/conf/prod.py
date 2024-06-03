from .base import *

DEBUG = False
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('DJANGO_EMAIL_HOST', 'localhost')
EMAIL_HOST_PORT = int(os.getenv('DJANGO_EMAIL_PORT', 25))
EMAIL_USE_TLS = is_true(os.getenv('DJANGO_EMAIL_USE_TLS'))
DEFAULT_FROM_EMAIL = os.getenv('DJANGO_DEFAULT_FROM_EMAIL', 'webmaster@localhost')
EMAIL_HOST_USER = os.getenv('DJANGO_EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('DJANGO_EMAIL_HOST_PASSWORD', '')
SERVER_EMAIL = os.getenv('DJANGO_SERVER_EMAIL', 'root@localhost')
