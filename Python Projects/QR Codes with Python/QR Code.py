import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://www.youtube.com/@GoogleDevelopers"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file nami