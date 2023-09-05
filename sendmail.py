# sendmail.py
"""
ZeptoMail Python API
Author: Nguyễn Hồng Thế <nguyenhongthe.net>
Description: Gửi email thông qua ZeptoMail API trong python.
Date: 2023-08-24
"""

import os
from dotenv import load_dotenv
import requests
from jinja2 import Template

load_dotenv()


# Khai báo các thông tin cần thiết
api_url = os.getenv("API_URL")
sendmail_token = os.getenv("SENDMAIL_TOKEN")
bounce_address = os.getenv("BOUNCE_ADDRESS")
from_name = os.getenv("FROM_NAME")
from_email = os.getenv("FROM_EMAIL")
subject = os.getenv("EMAIL_SUBJECT")
to_email = os.getenv("TO_EMAIL")
to_name = os.getenv("TO_NAME")
reply_to_name = os.getenv("REPLY_TO_NAME")
reply_to_email = os.getenv("REPLY_TO_EMAIL")
email_template = os.getenv("EMAIL_TEMPLATE")


# Hàm gửi email
def send_email(subject, to_email, to_name, reply_to_name, reply_to_email):
    """
    Gửi email thông qua ZeptoMail API
    :param api_url: Đường dẫn API
    :param sendmail_token: Mã token để gọi API
    :param bounce_address: Địa chỉ để nhận email bị trả lại (Nếu email gửi đi không thành công)
    :param from_name: Tên người gửi
    :param from_email: Email người gửi
    :param subject: Tiêu đề email
    :param to_email: Email người nhận
    :param to_name: Tên người nhận
    :param reply_to_name: Tên người nhận phản hồi
    :param reply_to_email: Email người nhận phản hồi
    :return: Response text (Phản hồi từ ZeptoMail API)
    """

    # Đọc file template
    with open(email_template, "r") as f:
        template_body = f.read()

    # Render template
    template = Template(template_body)
    # Render HTML body
    rendered_html_body = template.render(
        # Thông tin ví dụ về sản phẩm, sử dụng để render template
        # Là các biến được truyền vào template thông qua ninjia2 template engine
        # Thay thế bằng thông tin sản phẩm của bạn
        name=to_name,
        product_name="Nguyễn Hồng Thế Blog",
        login_url_link="https://nguyenhongthe.net",
        login_url_text="Nguyễn Hồng Thế Blog",
        username="nguyenhongthe",
        trial_end_link="https://nguyenhongthe.net",
        trial_date="2024-01-01",
        team="Nguyễn Hồng Thế Blog"
        )

    payload = {
        "bounce_address": bounce_address,
        "from": {
            "name": from_name,
            "address": from_email
        },
        "to": [
            {
                "email_address": {
                    "address": to_email,
                    "name": to_name
                }
            }
        ],
        "reply_to": {
            "name": reply_to_name,
            "address": reply_to_email
        },
        "subject": subject,
        "htmlbody": rendered_html_body
    }

    headers = {
        'accept': "application/json",
        'content-type': "application/json",
        'authorization': sendmail_token
    }

    response = requests.post(api_url, json=payload, headers=headers)

    return response.text

# Nhận và in ra response
response_text = send_email(subject, to_email, to_name, reply_to_name, reply_to_email)
print(response_text)
