import qrcode

# Texto que quieres codificar
data = "https://utt.edu.mx"  # Puedes cambiarlo por cualquier texto o URL

# Crear el objeto QR
qr = qrcode.QRCode(
    version=1,  # Tamaño del QR (1 es el más pequeño)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Nivel de corrección
    box_size=10,  # Tamaño de cada cuadro
    border=4,     # Borde alrededor del QR
)

# Agregar datos
qr.add_data(data)
qr.make(fit=True)

# Crear imagen
img = qr.make_image(fill_color="black", back_color="white")

# Guardar y mostrar
img.save("codigo_qr.png")
img.show()
