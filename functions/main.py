from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def respond():
    print(request.json);
    print('i am gay')
    return Response(status=200)