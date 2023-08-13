# Ocserv Telegram Bot for Certificate-Based Authentication

This repository contains a Telegram bot implemented in Python that manages certificate-based authentication for Ocserv servers. The bot allows authorized users to create, get, and revoke certificates, check online users, disconnect users, and obtain server status directly through Telegram commands.

## Ocserv Certificate-Based Authentication

The Ocserv (OpenConnect Server) is a widely used SSL VPN server. This project enhances Ocserv by integrating a Telegram bot, making it easier to manage user certificates and perform administrative tasks. The Ocserv server with certificate-based authentication is based on the work from the [Ocserv repository](https://github.com/chendong12/ocserv).

## Requirements

- Python 3.8 or higher
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) library (version 12.3.0)
- [dotenv](https://github.com/theskumar/python-dotenv) library
- A Telegram Bot Token obtained from the [BotFather](https://core.telegram.org/bots#botfather)
- Admin chat IDs added to a .env file as `ADMIN_CHAT_IDS` (comma-separated integers)

## Getting Started

1. Clone the repository to your local machine.

	git clone https://github.com/lennon81280/ocserv-telegram-bot.git
	cd ocserv-telegram-bot

Install the required Python packages.

	pip install python-telegram-bot python-dotenv

Create a .env file in the root directory of the project and add your Telegram Bot Token and the admin chat IDs.

	TELEGRAM_TOKEN=your_telegram_bot_token
	ADMIN_CHAT_IDS=comma,separated,list,of,admin,chat,ids

Ensure you have followed the instructions from the Ocserv repository for installing the Ocserv server with certificate-based authentication. Make any necessary modifications to the Ocserv server configuration to match your setup.
Customize the server actions in the Python script (bot.py) to interact with your Ocserv server.

Run the bot.

	python telegrambot.py 

Add your bot to a Telegram group or start a private chat with it, and use the commands specified below.

Available Commands

    /create <client_ocserv>: Create a new user certificate and send it to the user.
    /get <client_ocserv>: Send the certificate file for an existing user.
    /revoke <client_ocserv>: Revoke the certificate for an existing user.
    /online: Show a list of online users.
    /disconnect <user_name>: Disconnect a user from the Ocserv server.
    /status: Get the status of the Ocserv server.


## Contributing

Contributions are welcome! If you find a bug or have suggestions for improvements, feel free to open an issue or submit a pull request.
