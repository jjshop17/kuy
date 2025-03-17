import os
import random
import string
from eth_account import Account
import requests

# === Buat folder 'data' jika belum ada ===
if not os.path.exists("data"):
    os.makedirs("data")

# === Generate BEP-20 Address & Private Key ===
wallet = Account.create()
bep20_address = wallet.address
private_key = wallet.key.hex()

# === Simpan ke file 'data/address.txt' ===
address_file = "data/address.txt"
with open(address_file, "w") as file:
    file.write(f"Address: {bep20_address}\n")
    file.write(f"Private Key: {private_key}\n")

print("✅ Address dan Private Key berhasil dibuat!")
print(f"📌 Address: {bep20_address}")
print(f"🔑 Private Key: {private_key}")
print(f"📄 Data telah disimpan di '{address_file}'")

# === Generate Random Twitter Handle ===
def random_username(length=8):
    chars = string.ascii_lowercase + string.digits
    return "@" + "".join(random.choice(chars) for _ in range(length))

twitter_handle = random_username()
print(f"🐦 Random Twitter Handle: {twitter_handle}")

# === URL Formulir Google ===
form_url = "https://docs.google.com/forms/d/e/1FAIpQLScfUcqgUHDx3zEQmtSCpoUz3t3tMnEG-HDY7p1mmq8_Zg0Wyw/formResponse"

# === Ganti dengan Entry ID yang sesuai di Google Form ===
form_data = {
    "entry.123456789": bep20_address,  # Entry ID untuk BEP-20 Address
    "entry.987654321": twitter_handle, # Entry ID untuk Twitter Handle
    "entry.111111111": "Yes",          # "Did you import your wallet into Trust Wallet?" → Yes
    "entry.222222222": "OKX",          # "Which wallet did you import from?" → OKX
}

# === Kirim data ke Google Form ===
response = requests.post(form_url, data=form_data)

# === Cek apakah berhasil ===
if response.status_code == 200:
    print("✅ Data berhasil dikirim ke Google Form!")
else:
    print("❌ Gagal mengirim data. Status:", response.status_code)
  
