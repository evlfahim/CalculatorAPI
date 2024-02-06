import awsgi
from flask import Flask, request, jsonify

app = Flask(__name__)

def your_simple_function(data):

    operand1 = data.get('operand1', 0)
    operand2 = data.get('operand2', 0)
    operator = data.get('operator', '+')

    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2
    else:
        return "Invalid operator"

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    if 'operand1' not in data or 'operand2' not in data or 'operator' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        result = your_simple_function(data)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})
