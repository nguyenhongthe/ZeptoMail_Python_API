
# ZeptoMail Python API

## Tác giả

[Nguyễn Hồng Thế Blog](https://nguyenhongthe.net)

## Mô tả

Kịch bản này gửi email bằng cách sử dụng API của ZeptoMail. Nó cho phép bạn tùy chỉnh nội dung email bằng cách sử dụng các mẫu Jinja2.

## Yêu cầu

1. Python 3.6+
2. Gói [requests](https://pypi.org/project/requests/) (Cài đặt bằng `pip install requests`).
3. Gói [dotenv](https://pypi.org/project/python-dotenv/) (Cài đặt bằng `pip install python-dotenv`).
4. Gói [Jinja2](https://pypi.org/project/Jinja2/) (Cài đặt bằng `pip install Jinja2`).

hoặc cài đặt nhanh thông qua requirements.txt:

```bash
pip install -r requirements.txt
```

## Thiết lập

1. Clone repo này. Hoặc tải xuống và giải nén nếu bạn không sử dụng Git.
2. Tạo tệp `.env` trong cùng thư mục với script này với nội dung sau:

   ```
   API_URL=<ZeptoMail API URL>
   SENDMAIL_TOKEN=<Your ZeptoMail API token>
   FROM_NAME=<Your Name>
   FROM_EMAIL=<Your Email>
   EMAIL_SUBJECT=<Email Subject>
   TO_EMAIL=<Recipient's Email>
   TO_NAME=<Recipient's Name>
   REPLY_TO_NAME=<Reply-to Name>
   REPLY_TO_EMAIL=<Reply-to Email>
   EMAIL_TEMPLATE=<Path to your email template file>
   ```

3. Vui lòng thay các giá trị trống bằng các giá trị thích hợp.

## Sử dụng
Chạy script bằng lệnh sau:

```bash
python sendmail.py
```

## Tùy chỉnh mẫu template

1. Tạo tệp mẫu HTML (ví dụ: email_template.html) và xác định bố cục email của bạn bằng HTML và các trình giữ chỗ Jinja2.
2. Trong script, mẫu được tải và các biến Jinja2 được sử dụng để hiển thị nội dung email.


## Đóng góp và báo lỗi

Repo này được đồng bộ tự động với `repo.vnscdn.com`. Nếu bạn muốn đóng góp hoặc báo lỗi, hãy truy cập vào repo chính [nguyenhongthe/repo.vnscdn.com](https://github.com/nguyenhongthe/repo.vnscdn.com/tree/main/packages/zeptomail_python_api) nơi mã gốc được phát triển.

## Bản quyền và giấy phép

Copyright (c) 2013-2023 Nguyễn Hồng Thế Blog - Phát hành theo giấy phép [MIT](LICENSE).