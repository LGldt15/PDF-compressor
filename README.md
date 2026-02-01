# 📄 PDF Auto-Compressor

This Python script automates the compression of PDF files.

---

## 🛠 Installation

### 1. Prerequisites
* **Python 3.x** must be installed + some libraries (pathlib, fitz, shutil)


* **Windows Users:** Ensure you check "Add Python to PATH" during installation.

### 2. Project Setup
Open a terminal (PowerShell on Windows or Terminal on Unix) in the project folder and run the following commands:

* install the libraries by copying this in your terminal:
* ```Terminal/shell
  pip install pathlib
  pip install pymupdf
  pip install shutil


## How to use

* Simply put all the pdf files you want to compress inside the **ogPDF** folder and run the following command in your terminal in the right directory
* ```Terminal/shell
  python PDFcompression.py
  

## Warning 
* if your file is to light (less than 1mb) the compressed file might me heavier than the original one but wont go over a certain limit (this will be corrected in a future update)


