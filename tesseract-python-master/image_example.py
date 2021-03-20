from PIL import Image
import pytesseract

def ocr_core(filename):
    im = Image.open(filename)
    tesseract_exe_path_installation="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    pytesseract.pytesseract.tesseract_cmd=tesseract_exe_path_installation
    text = pytesseract.image_to_string(im, lang = 'eng')
    return text



