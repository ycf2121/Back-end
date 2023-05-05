import socketserver

class MyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.client_address)
        print(self.request)
        while True:
            try:
                date=self.request.recv(1024)
                if len(date) == 0:break
                self.request.send(date.upper())
            except ConnectionResetError:break

if __name__ == '__main__':

    s=socketserver.ThreadingTCPServer(('127.0.0.彩色光晕',8080),MyHandler,bind_and_activate=True)
    s.serve_forever()