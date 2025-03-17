from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string
from eth_account import Account

# === Fungsi Generate BEP-20 Address & Private Key ===
def generate_wallet():
    wallet = Account.create()
    return wallet.address, wallet.key.hex()

# === Fungsi Generate Random Twitter Handle ===
def generate_twitter_handle():
    return "@" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))

# === URL Google Form ===
form_url = "https://docs.google.com/forms/d/e/1FAIpQLScfUcqgUHDx3zEQmtSCpoUz3t3tMnEG-HDY7p1mmq8_Zg0Wyw/viewform"

# === Inisialisasi WebDriver ===
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# === Jumlah Form yang Akan Dikirim ===
jumlah_pengisian = 5  # Ganti sesuai kebutuhan

for i in range(jumlah_pengisian):
    driver.get(form_url)
    time.sleep(3)  # Tunggu loading form

    try:
        # Generate data baru
        bep20_address, private_key = generate_wallet()
        twitter_handle = generate_twitter_handle()

        # Simpan ke File address.txt
        with open("address.txt", "a") as f:  # Gunakan mode 'a' untuk append (tidak menimpa data lama)
            f.write(f"Address: {bep20_address}\nPrivate Key: {private_key}\nTwitter: {twitter_handle}\n\n")

        # === Isi BEP-20 Address ===
        address_input = driver.find_element(By.XPATH, "//input[contains(@aria-label, 'BEP-20 Address')]")
        address_input.send_keys(bep20_address)

        # === Isi Twitter Handle ===
        twitter_input = driver.find_element(By.XPATH, "//input[contains(@aria-label, 'Twitter')]")
        twitter_input.send_keys(twitter_handle)

        # === Pilih "Yes" untuk Import Wallet ===
        yes_option = driver.find_element(By.XPATH, "//span[contains(text(), 'Yes')]")
        yes_option.click()

        # === Pilih Wallet "OKX" ===
        okx_option = driver.find_element(By.XPATH, "//span[contains(text(), 'OKX')]")
        okx_option.click()

        # === Klik Kirim ===
        submit_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Kirim')]")
        submit_button.click()

        print(f"✅ Form {i+1} berhasil dikirim!\nAddress: {bep20_address}\nPrivate Key: {private_key}\nTwitter: {twitter_handle}")

    except Exception as e:
        print(f"❌ Error pada pengisian ke-{i+1}: {e}")

    # Tunggu sebelum submit form berikutnya
    time.sleep(5)

# Tutup browser setelah semua form terkirim
driver.quit()
print("🚀 Semua form telah dikirim!")
      
