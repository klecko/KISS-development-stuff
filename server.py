import http.server
import zlib

def encode(content):
    gzip_compress = zlib.compressobj(9, zlib.DEFLATED, zlib.MAX_WBITS | 16)
    data = gzip_compress.compress(content) + gzip_compress.flush()
    return data

class Handler(http.server.BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'
    
    ans = [b"HOLA MUNDO\n", b"ADIOS MUNDO\n"]
    ans_encoded = [encode(a) for a in ans]
    #analizar paquetes con wireshark
    def send_head(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Transfer-Encoding", "chunked")
        self.send_header("Content-Encoding", "gzip")
        #self.send_header("Content-Length", max(len(self.ans) + len(self.ans2), len(self.ans_encoded) + len(self.ans2_encoded)))
        self.end_headers()
        
        chunk_length = sum([len(a_encoded) for a_encoded in self.ans_encoded])
        chunked_heading = hex(chunk_length)[2:].encode() + b"\r\n"
        content = b"".join([a_encoded for a_encoded in self.ans_encoded])#encode(self.ans) + encode(self.ans2) + b"\r\n"
        chunked_finish = b"\r\n0\r\n\r\n"
        
        final_ans = chunked_heading + content + chunked_finish
        print(final_ans, chunk_length, len(final_ans), len(content))
        self.wfile.write(final_ans)
        return
        
    def do_GET(self):
        self.send_head()
    
    def do_HEAD(self):
        self.send_head()
    
    
        

def main():
    server = http.server.ThreadingHTTPServer(("localhost", 8080), Handler)
    
    print("Started server")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Finishing...")
    
    
if __name__ == "__main__":
    main()
