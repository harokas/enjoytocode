# pip install pillow
# pip install qrcode  
import qrcode
# Link to your website
input_data = "https://www.enjoytocode.com"
# Create an instance of qrcode
qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('qrcode01.png')

