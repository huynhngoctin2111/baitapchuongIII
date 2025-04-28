import requests
# pip install requests

from bs4 import BeautifulSoup
# pip install beautifulsoup4

import pandas as pd
# pip install pandas

# 1. Gửi HTTP request đến trang web
response = requests.get("https://genk.vn/tin-ict.chn")

# 2. Kiểm tra nếu request thành công
if response.status_code == 200:

    # 3. Sử dụng BeautifulSoup để phân tích HTML
    soup = BeautifulSoup(response.content, "html.parser")

    # 4. Tìm kiếm các bài báo có thẻ h4 với class="knswli-title"
    news = soup.findAll('h4', class_='knswli-title')
    print(news)

    # Lấy link của tất cả các bài viết đó
    # links = []
    # for link in news:
    #     url = link.find('a').attrs["href"]
    #     links.append(url)

    links = [link.find('a').attrs["href"] for link in news]
    print(links)
# Tạo danh sách để lưu dữ liệu
data = []

# 5. Đối với mỗi bài báo, lấy tiêu đề, tóm tắt, nội dung, link ảnh bài viết
for link in links:
    news = requests.get("https://genk.vn" + link)
    soup = BeautifulSoup(news.content, "html.parser")
    title = soup.find("h1", class_="kbwc-title clearfix").text
    summary = soup.find("h2", class_="knc-sapo").text
    body = soup.find("div", id="ContentDetail")

    try:
        content = body.decode_contents()
    except:
        content = ""

    try:
        image = body.find("img").attrs["src"]
    except:
        image = ""

    item = [title, summary, content, image]
    data.append(item)

# print(data)

# 6. Lưu dữ liệu vào file Excel
df1 = pd.DataFrame(data, columns=["title", "summary", "content", "image"])
df1.to_excel("output.xlsx")
