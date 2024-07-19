import os
import ssl

# Defina o caminho para o certificado, se necessário
os.environ['SSL_CERT_FILE'] = 'Users/Paula/Desktop/mba_impacta/certificado/certificate.pem'

# Ou configure o SSL diretamente
ssl_context = ssl.create_default_context(cafile=os.environ['SSL_CERT_FILE'])
