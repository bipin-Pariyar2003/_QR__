import qrcode
img = qrcode.make("https://nepali-date-picker-alpha.vercel.app/")
type(img)
img.save("date-picker-qr.jpg")


img1 = qrcode.make("https://bipinpariyar2003.pythonanywhere.com/")
type(img1)
img1.save("portfolio-qr.jpg")