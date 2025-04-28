import requests
from bs4 import BeautifulSoup
import pandas as pd

# Gửi HTTP request đến trang web
response = requests.get("https://www.24h.com.vn/tin-tuc-cong-nghe-c453.html")

# Kiểm tra nếu request thành công
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Tìm các bài báo có thẻ h3 và class liên quan
    articles = soup.findAll("div", class_="box-news-item")
    
    # Lưu danh sách link bài viết
    links = [article.find("a").attrs["href"] for article in articles]
    
    # Tạo danh sách để lưu dữ liệu
    data = []

    # Lặp qua từng link bài báo để lấy dữ liệu chi tiết
    for link in links:
        news = requests.get("https://www.24h.com.vn" + link)
        news_soup = BeautifulSoup(news.content, "html.parser")

        try:
            title = news_soup.find("h1", class_="baiviet-title").text.strip()
            print(title)
        except:
            title = ""

        try:
            summary = news_soup.find("h2", class_="baiviet-sapo").text.strip()
        except:
            summary = ""

        try:
            body = news_soup.find("div", class_="text-conent")
            content = body.decode_contents() if body else ""
        except:
            content = ""

        try:
            image = news_soup.find("div", class_="bv-avt").find("img")["src"]
        except:
            image = ""

        # Lưu vào danh sách
        item = [title, summary, content, image]
        data.append(item)

#     # Lưu dữ liệu vào file Excel
#     df = pd.DataFrame(data, columns=["title", "summary", "content", "image"])
#     df.to_excel("24h_tech_news.xlsx", index=False)

#     print("Dữ liệu đã được lưu vào file 24h_tech_news.xlsx")

else:
    print("Không thể truy cập trang web.")
