from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

driver = webdriver.Chrome()
# Open WhatsApp Web once
driver.get("https://web.whatsapp.com")
# input("📱 Scan QR code (if needed) and press Enter...")
time.sleep(15)
# Load contacts
df = pd.read_csv("contacts.csv", encoding='utf-8-sig')

for i, row in df.iterrows():
    number = str(row["Number"]).strip()
    message = "Hello! 👋 This is a reminder for our Sunday Garba Workshop. Please don’t forget to join us. 💃🔥"

    url = f"https://web.whatsapp.com/send?phone={number}&text={message}"
    driver.get(url)
    print(f"➡️ Opening chat with {number}...")
    time.sleep(10)  # Wait for page + chat to load

    try:
        send_btn = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
        send_btn.click()
        print(f"✅ Message sent to {number}")
        time.sleep(2)
    except Exception as e:
        print(f"❌ Could not send to {number}: {e}")

driver.quit()
