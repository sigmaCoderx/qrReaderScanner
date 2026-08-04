# 📷 QR Reader & Generator Telegram Bot

A Telegram bot that can both generate QR codes from any text and scan QR codes from uploaded images.

Simply send a message to generate a QR code, or upload a QR image to instantly decode its contents.

---

## Features

- 📷 Generate QR codes from any text
- 🔍 Scan QR codes from images
- ⚡ Fast QR generation and decoding
- 🤖 Telegram bot interface
- 🌐 Uses QRServer API
- 💬 Simple and easy to use

---

## Tech Stack

- Python
- pyTelegramBotAPI
- Requests
- QRServer API

---

## Installation

### Clone the repository

```bash
git clone https://github.com/sigmaCoderx/qrReaderScanner.git
cd qrReaderScanner
```

### Create a virtual environment (Optional)

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a Telegram bot using **BotFather**:

https://t.me/BotFather

Replace the placeholder inside the source code:

```python
bot = TeleBot("YOUR_BOT_TOKEN", parse_mode="HTML")
```

You can also customize the Telegram Group and Channel links.

---

## Running the Bot

```bash
python qrReaderScanner.py
```

---

## How It Works

### Generate a QR Code

1. Start the bot using `/start`.
2. Send any text.

Example:

```
https://github.com/sigmaCoderx
```

The bot instantly generates a QR code containing your text.

---

### Scan a QR Code

1. Send a photo containing a QR code.
2. The bot uploads the image to the QRServer API.
3. The decoded content is returned as a text message.

---

## Example

### Input

```
Hello World
```

### Output

```
📷 QR Code
```

---

### Input

*(Upload a QR Code image)*

### Output

```
Scanned Output:

Hello World
```

---

## Project Structure

```
qrReaderScanner/
├── qrReaderScanner.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Requirements

All project dependencies are listed in **requirements.txt**.

Install them with:

```bash
pip install -r requirements.txt
```

---

## Notes

- Requires an active internet connection.
- Uses the QRServer API for QR generation and decoding.
- Supports most standard QR codes.
- Never commit your Telegram Bot Token to GitHub.

---

## Future Improvements

- Support QR generation with custom colors
- Generate QR codes with logos
- Scan multiple QR codes in one image
- QR code history
- Batch QR generation
- Local QR decoding without external APIs

---

## License

MIT License

---

## Author

**flippedCoin**

GitHub: https://github.com/sigmaCoderx

---

⭐ If you found this project useful, consider giving it a star on GitHub.
