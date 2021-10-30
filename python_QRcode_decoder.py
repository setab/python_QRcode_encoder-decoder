import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

def qrdecoder():
    directory =  input("Plz input the file directory for decoding QRcode(ex:'C:/folder/img_folder_name/' : ) : ")
    name =  input("what is the QRcode name? : ")
    img = Image.open("{}{}.png".format(directory,name))
    result = decode(img)
    print(result)

qrdecoder()