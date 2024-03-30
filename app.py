import http.server
import socketserver
import os

PORT = int(input("Enter The Server Port: "))  # You can change this to any available port

# Specify the directory you want to serve files from
# Example: custom_folder = '/path/to/your/folder'
custom_folder = input("Enter the path to the folder you want to serve files from: ")

print("\n\n\n")

# Change the current directory to the custom folder
os.chdir(custom_folder)

Handler = http.server.SimpleHTTPRequestHandler

class ThreadedHTTPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

with ThreadedHTTPServer(("", PORT), Handler) as httpd:
    print("HTTP server started on port", PORT)
    print("Access the server by visiting http://localhost:" + str(PORT))
    print("Press Ctrl+C to stop the server.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
