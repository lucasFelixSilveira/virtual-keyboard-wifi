from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import pyautogui
from time import sleep

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    def do_POST(self):
        self._set_headers()
        self.wfile.write('OK'.encode('utf-8'))
        pyautogui.press('enter')

    def do_GET(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        
        if parsed_path.path == '/send':
            typed_param = query_params.get('typed', [''])[0]
            self._set_headers()
            if typed_param:
                for char in typed_param:
                    pyautogui.write(char)
                self.wfile.write(f'Typed parameter received: {typed_param}'.encode('utf-8'))
            else:
                self.wfile.write('No "typed" parameter received'.encode('utf-8'))
        else:
            self._set_headers(status_code=404)
            self.wfile.write('Not Found'.encode('utf-8'))

def run_server():
    server_address = ('', 2919)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print('Server running on port 2919...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
