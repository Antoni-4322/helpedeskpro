# # type: ignore
# # flake8: noqa

# # Comando:
# # python -c "import string as s;from secrets import SystemRandom as SR;print(''.join(SR().choices(s.ascii_letters + s.digits + s.punctuation, k=64)));"
# SECRET_KEY = 'JHbR871M7DadA!YN(s]sYSz$?XaH2d.R2?0@]u~U5?D;T$oF?U;W$TtZhoH*s}CU'

# # DEBUG DEVE SER False em produção
# DEBUG = False

# # Seu domínio ou IP devem vir aqui
# ALLOWED_HOSTS = [
#     '*'
# ]  # Troque * para seu domínio ou IP

# # Config para postgresql
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'helpdesk',
#         'USER': 'antonio',
#         'PASSWORD': 'Antoni-4322',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }