# Gmail Spam Bot

This is a simple Python script that allows you to send spam emails using Gmail accounts. Please note that sending unsolicited emails or spam is unethical and may violate legal regulations. Use this script responsibly and with proper authorization.

## Prerequisites

- Python 3.x
- `ssl`, `random`, `smtplib`, and `time` libraries

## Setup

1. Clone or download this repository to your local machine.

2. Open the script `spam_bot.py` in a text editor.

3. Modify the following variables to configure the script:

    - `port`: The SMTP port to use (default: 587).
    - `gmail`: Your Gmail address.
    - `email1`, `email2`, `email3`: Additional Gmail addresses (optional).
    - `password1`, `password2`, `password3`: Passwords for the respective Gmail addresses.
    - `reciever`: The email address of the recipient.
    - `what_to_send`: The content of the email you want to send.

4. Save the changes made to the script.

## Usage

1. Open a terminal or command prompt.

2. Navigate to the directory where the script `spam_bot.py` is located.

3. Run the script using the command: `python spam_bot.py`

4. Follow the on-screen instructions:

    - Choose the number of emails you want to use (1, 2, or 3).
    - Enter the required information for each email address and password.
    - Provide the email address of the recipient.
    - Specify the content of the email you want to send.

5. Choose the mode of operation:

    - Limited amount of messages: Specify the number of times to repeat sending emails and the duration to wait between each message.
    - Unlimited amount of messages: Specify the duration to wait between each message.

6. The script will start sending spam emails as per your configuration.

## Disclaimer

**Use this script responsibly and with proper authorization.** Sending unsolicited emails or spam is unethical and may be illegal in many jurisdictions. The purpose of this script is for educational and informational purposes only. The developers and contributors of this script are not responsible for any misuse or unlawful activities conducted with it.

Please comply with all relevant laws, regulations, and ethical considerations regarding email communications.
