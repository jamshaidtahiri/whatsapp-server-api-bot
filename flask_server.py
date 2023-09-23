from flask import Flask, request, jsonify,render_template
from selenium_code import generate_qr_code_image
app = Flask(__name__)

# Define dictionaries to simulate linked WhatsApp numbers and chat history
linked_numbers = {}
chat_history = {}


# API to display the HTML page with the QR code
# @app.route('/')
@app.route('/<phone_number>/Link', methods=['GET'])
def display_qr_code_page(phone_number):
    qr_code_image_base64 = generate_qr_code_image(phone_number)
    return render_template('index.html', qr_code_image_base64=qr_code_image_base64)

# API to link a new phone number using a QR code
# @app.route('/<phone_number>/Link', methods=['GET'])
# def generate_qr_code(phone_number):
#     # Generate and return a QR code to link the WhatsApp number
#     # You can use a library like qrcode to generate QR codes dynamically
#     qr_code = f"Sample QR Code for {phone_number}"
#     linked_numbers[phone_number] = qr_code
#     return jsonify({"qr_code": qr_code})

# API to send a new message, including an attachment
@app.route('/<phone_number>/Send', methods=['POST'])
def send_message(phone_number):
    recipient = request.args.get('To')
    message = request.args.get('Msg')
    file_url = request.args.get('file')
    
    # Simulate sending the message and attachment (you would implement the Selenium interaction here)
    sent_message = f"Message sent to {recipient}: {message}"
    
    # Store the sent message in the chat history
    if phone_number not in chat_history:
        chat_history[phone_number] = []
    chat_history[phone_number].append(sent_message)
    
    return jsonify({"message_status": "Sent"})

# API for syncing all messages for a phone number
@app.route('/<phone_number>/Sync', methods=['GET'])
def sync_messages(phone_number):
    recipient = request.args.get('To')
    
    # Retrieve chat history for the specified recipient
    if recipient:
        if recipient in chat_history:
            return jsonify({"chat_history": chat_history[recipient]})
        else:
            return jsonify({"chat_history": []})
    
    # Retrieve all chat history for the phone number
    if phone_number in chat_history:
        return jsonify({"chat_history": chat_history[phone_number]})
    else:
        return jsonify({"chat_history": []})

if __name__ == '__main__':
    app.run(debug=True)
