from flask import Flask, render_template, request, jsonify
from cipher import encrypt_message, decrypt_message

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    try:
        key = int(data.get('key'))
        message = data.get('message')
        encrypted, h_values = encrypt_message(key, message)
        return jsonify({
            'success': True,
            'encrypted': encrypted,
            'h_values': h_values
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    try:
        key = int(data.get('key'))
        encrypted_text = data.get('encrypted_text')
        h_values = data.get('h_values')
        
        # Determine format of h_values (string "1 2 3" or list [1, 2, 3])
        if isinstance(h_values, str):
            h_list = [int(x) for x in h_values.replace(',', ' ').split()]
        elif isinstance(h_values, list):
            h_list = [int(x) for x in h_values]
        else:
            raise ValueError("Invalid H values format")

        decrypted = decrypt_message(key, encrypted_text, h_list)
        return jsonify({
            'success': True,
            'decrypted': decrypted
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
