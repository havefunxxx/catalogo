import http.server
import socketserver
import webbrowser
import threading
import os

# Configurações
PORT = 8000
DIRETORIO = os.path.dirname(os.path.abspath(__file__))  # pasta atual

# Define o diretório onde está o index.html
os.chdir(DIRETORIO)

Handler = http.server.SimpleHTTPRequestHandler

# Função para iniciar o servidor
def iniciar_servidor():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Servindo na porta {PORT}")
        httpd.serve_forever()

# Inicia o servidor em uma thread separada
thread = threading.Thread(target=iniciar_servidor)
thread.daemon = True
thread.start()

# Abre o navegador automaticamente
url = f"http://localhost:{PORT}/index.html"
print(f"Abrindo {url} no navegador...")
webbrowser.open(url)

# Mantém o script rodando
input("Pressione ENTER para encerrar o servidor.\n")
