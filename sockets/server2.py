import socket
from views import index, blog, error404

URLS = {
    '/': index,
    '/blog': blog
}

class Server(socket.socket):
    def __init__(self, url, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((url, port))

    @staticmethod
    def __parse_request(req):
        splited = req.split(' ')
        method = splited[0]
        url = splited[1]
        return (method, url)

    @staticmethod
    def __generate_headers(method, url):
        if not method == 'GET': return ('HTTP/1.1 405 Method not allowed\n\n', 405)
        if not url in URLS: return ('HTTP/1.1 404 Not found\n\n', 404)
        return ('HTTP/1.1 200 OK\n\n', 200)

    @staticmethod
    def __generate_content(url, code):
        if code == 405: return '<h1>405 Method not allowed</h1>'
        if code == 404: return error404()
        return URLS[url]()

    @staticmethod
    def __get_response(req):
        method, url = Server.__parse_request(req)
        print(url)
        headers, code = Server.__generate_headers(method, url)
        content = Server.__generate_content(url, code)
        return (headers + content).encode('utf-8')

    def start(self):
        self.socket.listen()
        while True:
            client_socket, addr = self.socket.accept()
            req = client_socket.recv(1024).decode('utf-8')
            response = Server.__get_response(req)
            client_socket.sendall(response)
            




server = Server('localhost', 9000)
server.start()