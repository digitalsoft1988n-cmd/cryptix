# Cryptix

Cryptix is a modular desktop application built with PySide6 for encrypting and decrypting text using a user-provided key. The project is designed with scalability and maintainability in mind, following a clear separation of concerns between UI, business logic, and core encryption logic.

---

## Features

* Encrypt text using a secure key-based approach
* Decrypt previously encrypted text with the same key
* Simple and intuitive tab-based interface (Encrypt / Decrypt)
* Copy output directly to clipboard
* Clean architecture for easy extension

---

## Tech Stack

* Python
* PySide6 (Qt for Python)
* cryptography (Fernet-based encryption)

---

## Project Structure

```
app/                    # Application entry and configuration
├── core/               # Core encryption logic
├── services/           # Business logic layer
├── ui/                 # User interface (views, controllers)
├── resources/          # Static assets
├── tests/              # Unit tests
├── run.py              # Entry point
```

---

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/cryptix.git
cd cryptix
```

2. Create a virtual environment (recommended):

```
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

---

## Running the Application

```
python ./app/main.py
```

---

## Architecture Overview

The application follows a layered architecture:

* UI Layer (`ui/`)
  Handles user interaction and presentation

* Controller Layer (`ui/controllers/`)
  Connects UI to business logic

* Service Layer (`services/`)
  Contains application use cases

* Core Layer (`core/`)
  Implements encryption and key handling

This structure ensures that core logic remains independent of the UI and can be reused in other interfaces such as CLI or web apps.

---

## Future Improvements

* File encryption and decryption
* Save/load encrypted data
* Key strength validation
* UI enhancements and theming
* Packaging as a standalone executable

---

## License

MIT License
