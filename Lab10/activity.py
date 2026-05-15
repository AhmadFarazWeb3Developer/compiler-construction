import customtkinter as ctk
import re

# --- Theme ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# --- Token Definitions ---
KEYWORDS = {"if", "else", "while", "print"}
OPERATORS = {"+", "-", "*", "/", "=", "==", "!="}

# --- Lexical Analysis ---
def lexical_analysis(code):
    tokens = []
    words = re.findall(r'[A-Za-z_]\w*|\d+|==|!=|[+\-*/=(){};]', code)

    for word in words:
        if word in KEYWORDS:
            tokens.append((word, "KEYWORD"))
        elif word in OPERATORS:
            tokens.append((word, "OPERATOR"))
        elif word.isdigit():
            tokens.append((word, "NUMBER"))
        elif re.match(r'^[A-Za-z_]\w*$', word):
            tokens.append((word, "IDENTIFIER"))
        else:
            tokens.append((word, "UNKNOWN"))

    return tokens

# --- Syntax Checking ---
def syntax_check(code):
    lines = code.split("\n")

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if "=" in line:
            parts = line.split("=")
            if len(parts) != 2:
                return "Invalid Syntax"

    return "Valid Syntax"

# --- Identifier Check ---
def identifier_check(tokens):
    errors = []

    for token, typ in tokens:
        if typ == "IDENTIFIER":
            if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', token):
                errors.append(f"Invalid identifier: {token}")

    return errors

# --- Analyze ---
def analyze_code():
    code = input_box.get("1.0", "end")

    tokens = lexical_analysis(code)
    syntax = syntax_check(code)
    naming_errors = identifier_check(tokens)

    output_box.delete("1.0", "end")

    output_box.insert("end", "🔍 TOKENS\n\n")
    for t in tokens:
        output_box.insert("end", f"{t}\n")

    output_box.insert("end", f"\nSYNTAX RESULT:\n{syntax}\n")

    output_box.insert("end", "\nNAMING ERRORS:\n")
    if naming_errors:
        for err in naming_errors:
            output_box.insert("end", err + "\n")
    else:
        output_box.insert("end", "No errors\n")

# --- App ---
app = ctk.CTk()
app.title("Mini Compiler IDE")
app.geometry("1000x600")

# Layout
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(1, weight=1)

# Title
title = ctk.CTkLabel(app, text="Mini Compiler IDE", font=("Arial", 24, "bold"))
title.grid(row=0, column=0, columnspan=2, pady=10)

# Input Frame
input_frame = ctk.CTkFrame(app)
input_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

input_label = ctk.CTkLabel(input_frame, text="Code Editor")
input_label.pack(anchor="w", padx=10, pady=5)

input_box = ctk.CTkTextbox(input_frame)
input_box.pack(expand=True, fill="both", padx=10, pady=10)

# Output Frame
output_frame = ctk.CTkFrame(app)
output_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

output_label = ctk.CTkLabel(output_frame, text="Analysis Output")
output_label.pack(anchor="w", padx=10, pady=5)

output_box = ctk.CTkTextbox(output_frame)
output_box.pack(expand=True, fill="both", padx=10, pady=10)

# Button
analyze_btn = ctk.CTkButton(app, text="Analyze Code", command=analyze_code)
analyze_btn.grid(row=2, column=0, columnspan=2, pady=10)

app.mainloop()