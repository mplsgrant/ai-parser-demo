from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Assuming you have the functionality for the data you want to handle
def process_data(data, filepath):
    # Process your data here

    from ollama_ocr import OCRProcessor

    # Initialize OCR processor
    ocr = OCRProcessor(model_name='llama3.2-vision:11b')  # You can use any vision model available on Ollama

    # Process an image
    result = ocr.process_image(
        image_path=filepath, #"/home/journohack/Downloads/crime-one-page.pdf",
        prompt=data
    )

    return f"Processed data: {result}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get the data from the form
    filepath = request.form['filepath']
    data = request.form['data_input']
    processed = process_data(data, filepath)
    return render_template('result.html', processed_data=processed)

@app.route('/api/process', methods=['POST'])
def api_process():
    # Handle the data processing via an API
    filepath = request.form['filepath']
    data = request.json.get('data')
    processed = process_data(data, filepath)
    return jsonify({"processed_data": processed})

if __name__ == '__main__':
    app.run(debug=True)