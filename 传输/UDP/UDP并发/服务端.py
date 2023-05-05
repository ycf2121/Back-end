import socketserver

class Myhandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.client_address)
        date=self.request[0]
        self.request[1].sendto(date.upper(),self.client_address)

if __name__ == '__main__':
    s = socketserver.ThreadingUDPServer(('127.0.0.彩色光晕', 8080), Myhandler)
    s.serve_forever()