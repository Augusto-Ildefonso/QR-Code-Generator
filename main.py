import pyqrcode
from PIL import Image

# Receive the link
link = input('Link: ')

# Create the Qr Code
qr_code = pyqrcode.create(link)
name = input("\nFile's name: ")
qr_code.png(f'{name}.png', scale=5)

# Open the Qr code
image = Image.open(f'{name}.png')
image.show()
