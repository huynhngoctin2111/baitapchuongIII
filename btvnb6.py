import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_genk_articles():
    url = "https://genk.vn/tin-ict.chn"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    articles = []
    mylist= soup.find_all("div", class_="knswli-right")
    
    for article in mylist:
        try:
            title = article.find("h4", class_="knswli-title").text.strip()
            summary = article.find("div", class_="knswli-sapo").text.strip()
        except AttributeError:
            continue 

        articles.append(f" **{title}**\n🔹 {summary}\n\n")

    return "\n".join(articles[:5])  

def send_email(sender, receiver, subject, body, password):
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, message.as_string())
        print(f"Email đã được gửi đến {receiver}")
        server.quit()
    except Exception as e:
        print(f"Lỗi khi gửi email: {e}")

if __name__ == "__main__":
    sender_email = "tin_2151220003@dau.edu.vn"
    app_password = "hfyg qfxx bmes dfjh"
    receiver_email = "tin_2151220003@dau.edu.vn"

    subject = "Tin tức công nghệ mới nhất từ Genk"
    body = get_genk_articles()  

    send_email(sender_email, receiver_email, subject, body, app_password)
