import os
import shutil
import smtplib
import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

# Paths
SOURCE_DIR = '.'  # Thư mục chứa file database
BACKUP_DIR = './backup'  # Thư mục để lưu file backup

# Tạo thư mục backup nếu chưa có
os.makedirs(BACKUP_DIR, exist_ok=True)

def send_email(subject, body):
    try:
        message = MIMEMultipart()
        message["From"] = EMAIL_SENDER
        message["To"] = EMAIL_RECEIVER
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, message.as_string())

        print("Email sent successfully.")

    except Exception as e:
        print(f"Failed to send email: {e}")

def backup_database():
    try:
        files = os.listdir(SOURCE_DIR)
        db_files = [file for file in files if file.endswith(".sql") or file.endswith(".sqlite3")]

        if not db_files:
            raise Exception("No database files found to backup.")

        for db_file in db_files:
            src_path = os.path.join(SOURCE_DIR, db_file)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file_name = f"{db_file}_{timestamp}"
            dest_path = os.path.join(BACKUP_DIR, backup_file_name)
            shutil.copy2(src_path, dest_path)
            print(f"Backed up {db_file} to {dest_path}")

        send_email(
            subject="Database Backup Successful",
            body=f"Backup completed successfully at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."
        )

    except Exception as e:
        send_email(
            subject="Database Backup Failed",
            body=f"Backup failed with error: {str(e)} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."
        )

# Schedule job at 00:00 every day
schedule.every().day.at("00:00").do(backup_database)

print("Backup service is running...")

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)
