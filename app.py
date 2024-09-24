from flask import Flask, request, send_file
from TTS.utils.synthesizer import Synthesizer

app = Flask(__name__)
synthesizer = Synthesizer()

@app.route('/synthesize', methods=['POST'])
def synthesize():
    text = request.json.get("text")
    output_path = "output.wav"
    synthesizer.tts_to_file(text=text, file_path=output_path)
    return send_file(output_path, mimetype='audio/wav')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
