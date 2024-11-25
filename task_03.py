import tkinter as tk
from tkinter import messagebox, simpledialog
import re
import secrets
import string

# Password rules
PASSWORD_RULES = {
    "min_length": 8,
    "uppercase": True,
    "lowercase": True,
    "numbers": True,
    "special_chars": True
}

# Predefined strength meter
STRENGTH_METER = ["Weak", "Moderate", "Strong", "Very Strong"]

def calculate_strength(password):
    """Calculate password strength based on rules."""
    strength = 0
    feedback = []
    
    if len(password) >= PASSWORD_RULES["min_length"]:
        strength += 1
    else:
        feedback.append(f"Use at least {PASSWORD_RULES['min_length']} characters.")
    
    if PASSWORD_RULES["uppercase"] and any(c.isupper() for c in password):
        strength += 1
    else:
        feedback.append("Include uppercase letters.")
    
    if PASSWORD_RULES["lowercase"] and any(c.islower() for c in password):
        strength += 1
    else:
        feedback.append("Include lowercase letters.")
    
    if PASSWORD_RULES["numbers"] and any(c.isdigit() for c in password):
        strength += 1
    else:
        feedback.append("Include numbers.")
    
    if PASSWORD_RULES["special_chars"] and any(c in string.punctuation for c in password):
        strength += 1
    else:
        feedback.append("Include special characters.")
    
    strength_metric = STRENGTH_METER[min(strength, len(STRENGTH_METER)-1)]
    return {"strength_metric": strength_metric, "feedback": feedback}


def generate_password():
    """Generate a strong password suggestion."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(12))


def create_passphrase():
    """Generate a passphrase from random words."""
    words = ["blue", "taco", "forest", "light", "moon", "ocean", "star", "rain", "cloud"]
    return '-'.join(secrets.choice(words) for _ in range(4))


def check_password_strength():
    """Pop-up for checking password strength."""
    password = simpledialog.askstring("Password Strength", "Enter your password:")
    if password:
        result = calculate_strength(password)
        feedback = "\n".join(result['feedback'])
        messagebox.showinfo("Password Strength", f"Strength: {result['strength_metric']}\n\nFeedback:\n{feedback}")


def suggest_password():
    """Pop-up for password suggestion."""
    password = generate_password()
    messagebox.showinfo("Password Suggestion", f"Suggested Password:\n{password}")


def strength_metric_demo():
    """Pop-up to show the strength metric of a password."""
    password = simpledialog.askstring("Strength Metric", "Enter your password:")
    if password:
        result = calculate_strength(password)
        messagebox.showinfo("Strength Metric", f"Password Strength Metric: {result['strength_metric']}")


def passphrase_mode():
    """Pop-up for passphrase generation."""
    passphrase = create_passphrase()
    messagebox.showinfo("Passphrase Mode", f"Generated Passphrase:\n{passphrase}")


# Main GUI
def main():
    root = tk.Tk()
    root.title("Password Complexity Checker")
    root.geometry("400x400")
    
    tk.Label(root, text="Password Complexity Checker", font=("Arial", 16, "bold")).pack(pady=10)
    
    tk.Button(root, text="Check Password Strength", command=check_password_strength, width=25).pack(pady=5)
    tk.Button(root, text="Strength Metric", command=strength_metric_demo, width=25).pack(pady=5)
    tk.Button(root, text="Suggest Password", command=suggest_password, width=25).pack(pady=5)
    tk.Button(root, text="Passphrase Mode", command=passphrase_mode, width=25).pack(pady=5)
    tk.Button(root, text="Exit", command=root.destroy, width=25).pack(pady=20)
    
    root.mainloop()


if __name__ == "__main__":
    main()
