from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:\Users\Sohib Khodary\Desktop\QR Code with Python\myqrcode.png')

result = decode(img)

print(result)