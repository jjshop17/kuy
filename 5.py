from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string
from eth_account import Account
from webdriver_manager.chrome import ChromeDriverManager

# === Generate Random BEP-20 Address & Private Key ===
wallet = Account.create()
bep20_address = wallet.address
private_key = wallet.key.hex()

# === Simpan ke File address.txt ===
address_file = "address.txt"
with open(address_file, "w") as f:
    f.write(f"Address: {bep20_address}\nPrivate Key: {private_key}")

# === Generate Random Twitter Handle ===
def generate_twitter_handle():
    return "@" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))

twitter_handle = generate_twitter_handle()

# === URL Google Form ===
form_url = "https://docs.google.com/forms/d/e/1FAIpQLScfUcqgUHDx3zEQmtSCpoUz3t3tMnEG-HDY7p1mmq8_Zg0Wyw/viewform"

# === Inisialisasi WebDriver dengan WebDriver Manager ===
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Jalankan Chrome tanpa GUI (opsional)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get(form_url)
time.sleep(3)  # Tunggu loading form

# === Isi BEP-20 Address ===
address_input = driver.find_element(By.XPATH, "//input[@type='text' and @aria-label='BEP-20 Address in Trust Wallet']")
address_input.send_keys(bep20_address)

# === Isi Twitter Handle ===
twitter_input = driver.find_element(By.XPATH, "//input[@type='text' and @aria-label='X (Twitter) Handle']")
twitter_input.send_keys(twitter_handle)

# === Pilih "Yes" untuk Import Wallet ===
yes_option = driver.find_element(By.XPATH, "//span[text()='Yes']")
yes_option.click()

# === Pilih Wallet "OKX" ===
okx_option = driver.find_element(By.XPATH, "//span[text()='OKX']")
okx_option.click()

# === Klik Kirim ===
submit_button = driver.find_element(By.XPATH, "//span[text()='Kirim']")
submit_button.click()

# === Tunggu beberapa detik lalu tutup browser ===
time.sleep(5)
driver.quit()

print(f"✅ Data berhasil dikirim!\nAddress: {bep20_address}\nPrivate Key: {private_key}\nTwitter: {twitter_handle}")
