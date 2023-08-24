# ZeptoMail Python API

## Author
Nguyễn Hồng Thế  
Website: [nguyenhongthe.net](https://nguyenhongthe.net)

## Description
This script sends emails using the ZeptoMail API. It allows you to customize the email content using Jinja2 templates.

## Prerequisites

1. Python 3.6+
2. [requests](https://pypi.org/project/requests/) package (Install using `pip install requests`).
3. [dotenv](https://pypi.org/project/python-dotenv/) package (Install using `pip install python-dotenv`).
4. [Jinja2](https://pypi.org/project/Jinja2/) package (Install using `pip install Jinja2`).

or quick install via requirements.txt:

```bash
pip install -r requirements.txt
```
## Setup
1. Clone the repository or download the script.
2. Create a `.env` file in the same directory as the script with the following content:
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
3. Please replace the placeholders with appropriate values.

## Usage
Run the script using the following command:

```bash
python sendmail.py
```

## Template Customization
1. Create an HTML template file (e.g., email_template.html) and define your email layout using HTML and Jinja2 placeholders.
2. In the script, the template is loaded, and Jinja2 variables are used to render the email content.

## License
This project is licensed under the [MIT](LICENSE).