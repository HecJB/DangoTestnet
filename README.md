
# DangoTestnet

**Full automation script to interact with Dango Testnet-1.5**

---

## Overview

This repository contains a complete automation script written in Python using **Pyppeteer** to interact with the [Dango Testnet-1.5](http://test-portal.dango.exchange/signup). The script automates key user workflows including:

- Creating a username on the Dango testnet
- Connecting a MetaMask wallet
- Testing core features such as:
  - Sending tokens
  - Converting tokens
  - Adding a margin account

The script automates browser interactions including MetaMask extension popups to simulate a real user experience on the Dango decentralized exchange testnet.

---

## Features

- Automated wallet connection and approval via MetaMask
- Username creation with availability checks
- Sending tokens to other addresses
- Token conversion operations
- Margin account creation and management
- Handles MetaMask transaction confirmation popups
- Runs in non-headless Chromium for full extension support

---

## Prerequisites

- Python 3.7+
- [Pyppeteer](https://github.com/pyppeteer/pyppeteer) Python library
- MetaMask Chrome extension unpacked folder
- A MetaMask wallet configured for Dango Testnet-1.5 RPC with testnet funds
- Basic knowledge of blockchain wallets and testnets

---

## Installation

1. Clone this repository:

```
git clone https://github.com/HecJB/DangoTestnet.git
cd DangoTestnet
```

2. Install Python dependencies:

```
pip install -r requirements.txt
```

3. Download and unpack the MetaMask Chrome extension, then configure your wallet for the Dango Testnet-1.5 RPC.

---

## Configuration

- Update the script with the path to your MetaMask extension folder:

```
METAMASK_PATH = '/path/to/metamask/extension'
```

- Set your desired username and wallet details inside the script.

---

## Usage

Run the automation script:

```
python dango_automation.py
```

The script will:

- Launch Chromium with MetaMask extension loaded
- Navigate to the Dango Testnet signup page
- Automate wallet connection and username creation
- Test sending tokens, converting tokens, and adding margin accounts
- Handle MetaMask transaction confirmation popups automatically

---

## Notes

- The script runs in **non-headless** mode because MetaMask UI requires a visible browser.
- Ensure your MetaMask wallet is unlocked before running the script.
- Use testnet funds only; do not use real assets.
- UI selectors used in the script may change if Dango updates their frontend — update selectors accordingly.

---

## Contributing

Contributions and improvements are welcome! Please open issues or pull requests.

---

## License

This project is licensed under the MIT License.

---

Citations:
[1] https://github.com/HecJB/DangoTestnet

---
Answer from Perplexity: https://www.perplexity.ai/search/arizona-company-programmer-PHRV.7S9RNOYammTwerPNw?utm_source=copy_output
