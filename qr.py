import qrcode

url = "https://abhiram918.github.io/birthday/vighnesh.html"
qr = qrcode.make(url)
qr.save("birthday_animation_qr.png")
