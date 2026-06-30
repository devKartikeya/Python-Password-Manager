# 🔐 Python Password Manager

A lightweight but robust command-line Password Manager built with Python that helps you securely organize account credentials in a local JSON database.

The application allows users to save account information, search stored credentials, generate strong passwords, and evaluate password strength—all from a simple interface. Access to stored credentials is protected using a master password.

---

## ✨ Features

### 📥 Add New Accounts

Store credentials for different websites and services.

Each account includes:

* 🌐 Website Name
* 👤 Username
* 🔑 Password
* 📝 Description

---

### 🔍 Search Accounts

Quickly search for a saved account by its website name.

To protect sensitive information, the application requires the master password before displaying stored credentials.

---

### 📋 View All Accounts

Display every stored account in the password vault after successful master password verification.

---

### 🎲 Password Generator

Generate random passwords with customizable length.

Supports:

* Lowercase alphabets
* Numeric characters

---

### 🛡️ Password Strength Checker

Quickly evaluate the strength of any password based on its length.

Password categories include:

* Weak
* Moderate
* Strong

---

## 📂 Data Storage

Account information is stored locally using a JSON file.

The master password is stored separately and is required to access saved credentials.

---

## 🛠️ Technologies Used

* Python
* JSON
* OS Module
* Random Module
* String Module
* Command-Line Interface (CLI)

---

## 📚 Concepts Practiced

* Functions
* File Handling
* JSON Operations
* Dictionaries
* Lists
* User Input Handling
* Conditional Statements
* Loops
* Random Password Generation
* Password Validation
* Local Data Persistence

---

## 📁 Project Structure

```text
Python-Password-Manager/
│
├── main.py
├── accounts.json
├── .env
└── README.md
```

---

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/your-username/Python-Password-Manager.git
```

Navigate into the project directory:

```bash
cd Python-Password-Manager
```

Run the application:

```bash
python main.py
```

---

## 📌 Menu Options

* Add a new account
* View all saved accounts
* Generate a random password
* Check password strength
* Search for an account
* Exit the application

---

## 🎯 Purpose

This project was built to strengthen Python fundamentals while developing a practical command-line utility.

It focuses on working with:

* Local data storage
* Credential management
* Random password generation
* File handling
* JSON manipulation
* Command-line application development

---

## 🚀 Future Improvements

Potential future enhancements include:

* Password encryption
* Password update functionality
* Special character support in generated password
* SQLite database support
* GUI version using Tkinter or CustomTkinter
* Better password strength analysis
* Export and backup functionality

---

⭐ If you found this project helpful, consider giving the repository a star!
