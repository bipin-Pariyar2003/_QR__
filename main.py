import qrcode
img = qrcode.make("https://nepali-date-picker-alpha.vercel.app/")
type(img)
img.save("date-picker-qr.jpg")