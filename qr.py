import qrcode

url = "https://abhiram918.github.io/birthday/"
qr = qrcode.make(url)
qr.save("birthday_animation_qr.png")
