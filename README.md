# Image to Text Translator

**Image to Text Translator** is a Flask-based web application that extracts text from images and translates it between English and Vietnamese. It uses Optical Character Recognition (OCR) with the help of **easyOCR**, and translation is done using **Google Translate**. It also provides spelling correction for better accuracy.

---

## Features

- Upload an image file.
- Extract text from the image using OCR.
- Correct spelling errors in the extracted text.
- Translate text from English to Vietnamese, and vice versa.
- Displays the original text, corrected text, and translated text.

---

## URL

Once the application is running, you can access it via the following URL:

- http://localhost:5000/image-to-text


---

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x
- Install dependencies via `requirements.txt`.

---

## Installation

###  Clone the Repository

Clone the project to your local machine.

```bash
git clone https://github.com/DangToNhanDev/image-to-text.git
```

### Install the Required Dependencies
```bash
pip install -r requirements.txt
```
### Project Structure
```bash
image-to-text/
├── app.py                # Main application file
├── config.py             # Configuration settings
├── requirements.txt      # Project dependencies
├── forms/
│   └── form_opencv.py    # Form handling for image upload
├── templates/
│   └── image_to_text.html # HTML template for displaying results
└── static/
    └── uploads/          # Folder for storing uploaded images
```

### Screenshot of Output

<img src="https://github.com/HitDrama/Image-To-Text-Translate/blob/main/static/train/img-text-test.png" alt="Result Image" width="600">

---
Author
Developed by Dang To Nhan Dev.
