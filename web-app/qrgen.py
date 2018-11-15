import qrcode

def genImage(code,name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(code)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    filename = name
    img.save("static/images/qr/qr"+filename+".png","PNG")

# genImage(x)
