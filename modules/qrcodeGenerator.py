##############################################################
# IMPORTING ESSENTIALS FILES
###############################################################
import os
import pyqrcode
import barcode
from barcode.writer import ImageWriter
os.system("cls")

def CreateQRCode(query, filename):
    os.system("cls")
    data = str(query)
    print("\n")
    output = filename.replace(" ", "_")
    qr = pyqrcode.create(data)
    qr.png(f"Codes\\{output}.png", scale=8)
    return True

def BarcodeCreator(query, filename):
    data = str(query)
    output = filename.replace(" ", "_")
    a = barcode.get_barcode_class("code128")
    b = a(data, writer=ImageWriter())
    b.save(f"Codes\\{output}")
    return True
