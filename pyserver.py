import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from textgenrnn import textgenrnn

HOST_NAME = '0.0.0.0'
PORT_NUMBER = 9000


class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        paths = {
        }

        if self.path in paths:
            self.respond(paths[self.path])
        else:
            self.respond({'status': 200})

    def handle_http(self, status_code, path):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        t = textgenrnn('textgenrnn_weights.hdf5');
        if len(path) > 1:
             print(len(path))
             generated_texts = t.generate(prefix=path[1:],n=1,temperature=0.5,return_as_list=True); 
        else:
             print(len(path))
             print('< 1')
             generated_texts = t.generate(n=1,temperature=0.5,return_as_list=True);
        content = '''{}'''.format('<br/><br/><br/><br/><center><h1>'+generated_texts[0]+'</h1></center>')
        return bytes(content, 'UTF-8')

    def respond(self, opts):
        response = self.handle_http(opts['status'], self.path)
        self.wfile.write(response)

if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print(time.asctime(), 'Server Starts - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Server Stops - %s:%s' % (HOST_NAME, PORT_NUMBER))

