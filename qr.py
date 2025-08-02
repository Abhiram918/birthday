import qrcode

url = "https://your-birthday-page-link.com"  # Replace this with your hosted page
qr = qrcode.make(url)
qr.save("birthday_animation_qr.png")
