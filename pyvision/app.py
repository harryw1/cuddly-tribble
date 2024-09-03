from flask import Flask, request, render_template, redirect, url_for, send_file
import pytesseract
from PIL import Image
import csv
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' not in request.files:
            return redirect(request.url)
        file = request.files['image']
        if file.filename == '':
            return redirect(request.url)
        if file:
            image = Image.open(file.stream)
            text = pytesseract.image_to_string(image)
            
            # Save the OCR result to a CSV file
            csv_filename = 'ocr_result.csv'
            with open(csv_filename, 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(['OCR Result'])
                csvwriter.writerow([text])
            
            return redirect(url_for('download_file', filename=csv_filename))
    return render_template('index.html')

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)