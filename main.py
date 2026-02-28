import os
import qrcode

org_name = "Save Speechless Organization"
email = "savespeechless@gmail.com"
dog_id = input("Enter Dog ID: ").strip()
address = "Swami Colony, Nagpur, Maharashtra 440013"
google_maps_link = "https://maps.app.goo.gl/2Mf8iTiFNLvGzEVV6"

qr_data = f"""
Dog ID: {dog_id}
Organization: {org_name}
Email: {email}
Location: {google_maps_link}
Address: {address}
"""

folder = "Images"
os.makedirs(folder, exist_ok=True)

file_path = os.path.join(folder, f"{dog_id}.png")

qr = qrcode.QRCode(
    version=None,
    box_size=10,
    border=4
)

qr.add_data(qr_data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(file_path)

print("QR code generated successfully!")
print(f"Saved at: {file_path}")