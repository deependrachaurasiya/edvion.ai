import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

def run_server(port=8000):
    # Get the current directory
    current_dir = Path.cwd()
    
    # Check if required files exist
    required_files = ['index.html', 'styles.css', 'script.js']
    missing_files = [f for f in required_files if not (current_dir / f).exists()]
    
    if missing_files:
        print(f"Error: Missing required files: {', '.join(missing_files)}")
        return
    
    # Create handler
    handler = http.server.SimpleHTTPRequestHandler
    
    try:
        # Create server
        with socketserver.TCPServer(("", port), handler) as httpd:
            print(f"Serving at http://localhost:{port}")
            print("Press Ctrl+C to stop the server")
            # Open browser automatically
            webbrowser.open(f'http://localhost:{port}')
            # Start serving
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped by user")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    run_server() 