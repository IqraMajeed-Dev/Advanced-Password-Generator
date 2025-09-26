# 🔐 Advanced Password Generator (Python + Tkinter)

A desktop password generator with GUI, strength analysis, history tracking, and clipboard support.  
Showcases Python skills and GUI development using Tkinter.

## Project Overview

This is a Python application that lets users generate secure passwords with customizable options. It includes:

- Custom length (6–32 characters)  
- Choice among uppercase, lowercase, digits, symbols  
- Real‑time strength feedback  
- History tracking with timestamps  
- One‑click copy to clipboard  
- Persistent storage (JSON)  
- Modern dark GUI theme  

The project was originally built as a university assignment in about 20–25 minutes, demonstrating quick and functional development.

## Features

### 🛠 Password Generation

- Set length between 6 and 32  
- Choose which character sets to include  
- Generate password instantly  

### 📊 Strength Analysis

- Computes strength based on length and character diversity  
- Displays strength with color (Weak / Medium / Strong)  

### 💾 History Tracking

- Saves passwords with timestamp  
- Shows last 10 entries  
- Uses a JSON file for storage  

### 📋 Clipboard Integration

- Copy password with a button  
- Shows confirmation after copy  

### 🎨 GUI Interface

- Dark theme  
- Simple, user‑friendly layout  
- Responsive controls  

## Technologies Used

- Python 3  
- Tkinter (for GUI)  
- JSON (for persistent storage)  
- pyperclip (clipboard interaction)  
- hashlib (optional hashing)  
- datetime (timestamping)  

## Repository Structure

```
Password-Generator/
│
├── password_generator.py        # main GUI application  
├── password_history.json        # stored history  
├── requirements.txt             # external dependencies  
├── README.md                    # project documentation  
├── screenshots/  
│   ├── main_interface.png  
│   ├── password_generated.png  
│   └── history_view.png  
└── examples/  
    ├── text_version.py          # CLI-only version  
    └── simple_version.py        # minimal generator  
```

## Screenshots Preview

- Main interface: `screenshots/main_interface.png`  
- Password generation: `screenshots/password_generated.png`  
- History view: `screenshots/history_view.png`  

## Installation & Usage

### Prerequisites

- Python 3.8+  
- pip  

### Installation Steps

```bash
git clone https://github.com/IqraMajeed-Dev/Password-Generator.git
cd Password-Generator
pip install -r requirements.txt
```

### Run the Application

```bash
python password_generator.py
```

If you only have the main file:

```bash
pip install pyperclip
python password_generator.py
```

## How to Use

1. Use controls to pick length and character types  
2. Click **Generate Password**  
3. Watch strength indicator  
4. Click **Copy to Clipboard** to copy  
5. Click **Save Password** to add to history  
6. View history entries in the window  

## Code Highlights

### Password Generation

```python
def generate_password(self):
    characters = ""
    if self.uppercase_var.get():
        characters += string.ascii_uppercase
    if self.lowercase_var.get():
        characters += string.ascii_lowercase
    # … digits and symbols similarly
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
```

### Strength Analysis

```python
def update_strength_indicator(self, password):
    score = 0
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1

    variety = sum([
        any(c.isupper() for c in password),
        any(c.islower() for c in password),
        any(c.isdigit() for c in password),
        any(not c.isalnum() for c in password)
    ])
    score += variety
    # Then update UI color/text based on score
```

## Developer

**Iqra Majeed**  
Passionate about Python development and desktop applications.  
This tool was built quickly as part of a university assignment, yet with full functionality and design awareness.

- GitHub: [IqraMajeed-Dev](https://github.com/IqraMajeed-Dev)  
- (Add your portfolio or LinkedIn link here)  

## License

This project is open source under the **MIT License**.  
You are free to use, modify, and distribute.

## Future Enhancements

- Add password expiration alerts  
- Group passwords by category  
- Export history to CSV/PDF  
- Enforce custom policies (e.g. “at least 2 digits”)  
- Add sync with cloud or remote storage  

---

Thank you for checking out this project!  
Feel free to raise issues or suggest features.
