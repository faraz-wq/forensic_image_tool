from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from forensic_utils import analyze_image, extract_metadata
import os

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    metadata = extract_metadata(file_path)
    tampering_analysis = analyze_image(file_path)

    result = {
        'metadata': metadata,
        'tampering_analysis': tampering_analysis
    }

    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
