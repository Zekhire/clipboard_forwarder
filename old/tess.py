try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\krzys\AppData\Local\Tesseract-OCR\tesseract.exe'
print(pytesseract.image_to_string(Image.open("kawaii.jpg"), lang="pl"))
# print(pytesseract.image_to_string(Image.open("test.jpg"), lang="eng"))
# print(pytesseract.image_to_string(Image.open("10-AS-48747.jpg"), lang="eng"))
# print(pytesseract.image_to_string(Image.open("10-CD-42851.jpg"), lang="eng"))
