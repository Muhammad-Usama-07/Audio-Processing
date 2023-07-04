# from flask import Flask, request, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/record', methods=['POST'])
# def record_voice():
#     # Save the voice recording to the server
#     voice_file = request.files['voice']
#     voice_file.save('voice.wav')
#     print('********** voice saved')
#     return 'Voice recording saved successfully!'


# if __name__ == '__main__':
#     app.run(debug=True, port=8000)


from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    if 'audio' not in request.files:
        return jsonify(message='No audio file uploaded'), 400

    audio_file = request.files['audio']
    if audio_file.filename == '':
        return jsonify(message='No selected audio file'), 400

    audio_file.save('./recording.wav')  # Save the audio file to the current folder
    return jsonify(message='Audio file saved'), 200

if __name__ == '__main__':
    app.run()
    
