import qrcode

data = 'Hello'

qr = qrcode.QRCode(version = 1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color = 'red', back_color = 'white')

img.save('C:/Users/Sohib Khodary/Desktop/QR Code with Python/myqrcode1.png')