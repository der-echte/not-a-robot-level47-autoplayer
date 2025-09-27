# Neal.fun Level 47 Autoplayer

A Python script that automatically plays **Level 47 ("I'm not a Robot")** from [Neal.fun](https://neal.fun).

The script detects when blocks reach the bottom of each lane and presses the corresponding arrow key at the right time.

---

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Disclaimer](#disclaimer)

---

## Description
This project demonstrates basic automation in Python using:

- **pyautogui** → for reading pixel colors from the screen  
- **keyboard** → for simulating key presses  

It is intended for **educational purposes only** to showcase automation concepts.  
This is **not an official tool** and is **not meant for cheating** in competitive settings.

---

## Features
- Detects white pixels at the bottom of each lane
- Automatically presses the correct arrow key
- Simple, lightweight, and easy to understand

---

## Requirements
- Python 3.10+ (recommended; some libraries may not fully support newer versions yet)
- Dependencies listed in `requirements.txt`

---

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage
1. Open **"I'm not a Robot – Level 47"** in your browser.  
2. Ensure the game window is positioned correctly (the script relies on fixed screen coordinates).  
3. Run the script:
   ```bash
   python autoplay.py
   ```
4. A short countdown will begin, after which the script will start automatically.  
5. Press `CTRL+C` in the terminal to stop the script at any time.

---

## How It Works
The script continuously monitors each lane's bottom position for a **white pixel (255, 255, 255)**.  
When detected, it triggers the corresponding key press:

| Lane          | Key Press |
|---------------|-----------|
| Left lane     | ⬅️       |
| Second lane   | ⬇️       |
| Third lane    | ⬆️       |
| Right lane    | ➡️       |

---

## Disclaimer
- This project is **for learning purposes only**.  
- Use responsibly; some games may detect automation tools.  
- The author is **not responsible for misuse**.

