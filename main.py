from flask import Flask, request, jsonify

app = Flask(__name__)
# my app
@app.route('/')


def hello():
    return 'Hello from test2!'

@app.route('/add', methods=['GET'])

def add_numbers():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        return jsonify({"result": a + b})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5000)
