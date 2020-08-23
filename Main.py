#make sure to install pyqrcode and pypng library before execution:
#follow below command to install library
#pip install pyqrcode
#pip install pypng

import pyqrcode
import png
from pyqrcode import QRCode 

#This will store the URL
data= "https://github.com/rohitrj5775/"

#This will generate qrcode
img = pyqrcode.create(data)

#This will save the qrcode in png format with proper scaling
img.png("qrcode.png", scale = 7)
 
