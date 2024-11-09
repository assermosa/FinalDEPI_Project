from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Home route to render the main chatbot page
@app.route('/')
def home():
    return render_template('home.html')  # Ensure home.html has the chatbot interface

# Chat route to handle messages from the chatbot frontend
@app.route('/predict', methods=['POST'])
def predict():
    user_message = request.json['message'].lower()  # Get and process user's message

    # Simple keyword-based responses for testing
    if 'hello' in user_message:
        bot_response = "Hi there! How can I assist you today?"
    elif 'how are you' in user_message:
        bot_response = "I'm just a bot, but thanks for asking! How can I help?"
    elif 'weather' in user_message:
        bot_response = "I'm not equipped to give weather updates yet, but I can help with simple tasks!"
    else:
        bot_response = "I'm here to chat! Try saying 'hello' or asking how I am."

    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
