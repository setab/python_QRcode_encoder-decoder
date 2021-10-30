import qrcode

def qrencoder():
    directory =  input("Plz input the file directory for decoding QRcode(ex:'C:/folder/img_folder_name/' : ) : ")
    data = input("Plz input the sentence you want to put in the QRcode? : ")
    name = input("what should be the QRcode_file name be? :")
    
    img = qrcode.make(data)
    img.save("{}{}.png".format(directory,name))
    print("the QR code has been saved in {}".format(directory))
  

def customQRcode():
    agree =  input("Do you want your custom QRcode?(y/n) : ")


    if agree == "y":
        directory =  input("Plz input the file directory to save QRcode(ex:'C:/folder/img_folder_name/' : ) : ")
        data = input("Plz input the sentence you want to put in the QRcode? : ")
        name = input("what should be the QRcode_file name be? :")
        BoxSize = int(input("what box size do you want? : "))
        Border = int(input("Border size? : "))
        ImgColor = input("Plz input QRcode color : ").lower()
        Background_color = input("Plz input background color :").lower()
        QR = qrcode.QRCode(box_size=BoxSize,border=Border)
        QR.add_data(data)
        QR.make(fit=True)
        img = QR.make_image(fill_color=ImgColor, back_color = Background_color)
        img.save("{}{}.png".format(directory,name))
        print("the QR code has been saved in {}".format(directory))
    else:
        qrencoder()

            


customQRcode()