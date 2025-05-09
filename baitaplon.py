from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Thiết lập trình duyệt
options = Options()
options.add_argument("--headless")  # chạy ngầm, không hiện cửa sổ trình duyệt
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)

base_url = "https://alonhadat.com.vn/nha-dat/can-ban/nha-dat/3/da-nang.html"
data = []

# Lặp qua 5 trang
for page in range(1, 6):
    print(f"Đang lấy trang {page}...")
    url = base_url + f"?page={page}" if page > 1 else base_url
    driver.get(url)
    time.sleep(2)  # đợi trang load xong

    listings = driver.find_elements(By.CSS_SELECTOR, ".content-item")

    for item in listings:
        try:
            title = item.find_element(By.CSS_SELECTOR, "div.ct_title a").text.strip()
        except:
            title = ""

        try:
            description = item.find_element(By.CSS_SELECTOR, "div.ct_desc").text.strip()
        except:
            description = ""

        try:
            spans = item.find_elements(By.CSS_SELECTOR, ".ct_dt span")
            area = ""
            for span in spans:
                if "Diện tích" in span.text:
                    area = span.text.strip()
                    break
        except:
            area = ""

        try:
            price = item.find_element(By.CSS_SELECTOR, ".price").text.strip()
        except:
            price = ""

        try:
            address = item.find_element(By.CSS_SELECTOR, ".ct_address").text.strip()
        except:
            address = ""

        data.append({
            "Tiêu đề": title,
            "Mô tả": description,
            "Diện tích": area,
            "Giá": price,
            "Địa chỉ": address
        })

driver.quit()

# Lưu vào CSV
df = pd.DataFrame(data)
df.to_csv("alonhadat_da_nang.csv", index=False, encoding='utf-8-sig')
print("Đã lưu vào alonhadat_da_nang.csv")
