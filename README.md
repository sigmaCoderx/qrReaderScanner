# Telegram QR Code Generator & Scanner Bot

A simple Telegram bot built with `pyTelegramBotAPI` (telebot) that creates QR codes from text and decodes QR codes from sent images using the QR Server API.

---

## Features

- **Generate QR Codes:** Send any text to the bot, and it returns a generated QR code image.
- **Scan QR Codes:** Send a photo of a QR code, and the bot reads it and returns the decoded text.
- **Inline Buttons:** Quick access links to connected Telegram groups and channels.

---

## Prerequisites

- **Python 3.x** installed on your machine.
- A **Telegram Bot Token** from [@BotFather](https://t.me/BotFather).

---

## Setup & Installation

1. Clone or download this repository.
2. Install the required Python libraries:

   ```bash
   pip install pyTelegramBotAPI requests
