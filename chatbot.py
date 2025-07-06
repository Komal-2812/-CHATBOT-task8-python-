import tkinter as tk
from tkinter import Scrollbar, Canvas, Frame

# --- Response Logic ---
def get_response(msg):
    msg = msg.lower()
    if msg == "exit":
        return "Thank you For Chat with me!.. Goodbye! 👋"
    
    elif "hello" in msg or "hi" in msg or "hy" in msg:
        return "Hey there! How can I help?"
    elif "how are you" in msg:
        return "I’m doing great, thanks for asking! 🤖"
    elif "your name" in msg:
        return "I’m Bot, your friendly assistant."
    elif "help" in msg:
        return ("Try asking me:\n"
            "- What is Python\n"
            "- I am sad\n"
            "- I need project\n"
            "- Resume tips\n"
            "- What is AI\n"
            "- Exit")
    
    # Emotions
    elif "i am sad" in msg or "feeling low" in msg:
        return "I'm here for you. Remember, tough times never last, but tough people do. 💪"

    elif "i am happy" in msg or "feeling good" in msg:
        return "Yay! I'm happy to hear that! 😄 Keep smiling!"

    # Computer studies
    elif "what is python" in msg:
        return "Python is a powerful, beginner-friendly programming language used for web, data science, automation, and more."

    elif "what is ai" in msg or "artificial intelligence" in msg:
        return "AI stands for Artificial Intelligence — the ability of a machine to mimic human thinking and learning."

    elif "how to learn coding" in msg:
        return "Start with Python! Practice daily on sites like W3Schools, GeeksForGeeks, or LeetCode. 💻"

    # Projects / Internship
    elif "i need project" in msg or "give project" in msg:
        return "Try a simple project like: Chatbot, To-Do app, Calculator, Weather App, or Portfolio Website."

    elif "internship" in msg:
        return "Internships help you gain real-world experience. You can find them on Internshala, LinkedIn, or company websites."

    elif "resume" in msg or "cv" in msg:
        return "Make sure your resume includes skills, projects, and a short summary. You can use Canva or Novoresume to design it."

    # Career
    elif "career advice" in msg:
        return "Explore your interests, build projects, network on LinkedIn, and don’t be afraid to start small."

    elif "job" in msg:
        return "Keep improving your skills. Practice coding, contribute to GitHub, and stay active on job platforms."

    # Unknown input fallback
    else:
        return "Sorry, I didn’t understand that. You can try saying things like 'project', 'python', or 'emotions'."

# --- Exit app ---
def exit_app(event=None):
    root.destroy()

# --- Display messages ---
def display_message(sender, msg, align="right", bg="#2A2F4F"):
    frame = Frame(scrollable_frame, bg=chat_bg, pady=5)
    
    if align == "left":
        side_val = "left"
        anchor_val = "w"
    else:
        side_val = "right"
        anchor_val = "e"

    label = tk.Label(
        frame,
        text=msg,
        bg=bg,
        fg="white",
        font=("Segoe UI", 12),
        wraplength=500,
        justify="left",
        padx=10,
        pady=7
    )
    label.pack(side=side_val, anchor=anchor_val)
    frame.pack(fill="x", anchor=anchor_val, padx=20)


# --- Handle send button ---
def send_message(event=None):
    msg = msg_entry.get().strip()
    if msg == "":
        return
    display_message("You", msg, align="right", bg="#4A55A2")
    msg_entry.delete(0, tk.END)
    response = get_response(msg)
    root.after(500, lambda: display_message("Bot", response, align="left", bg="#1A1A40"))
    if msg.lower() == "exit":
        root.after(1000, root.destroy)

# --- MAIN GUI START ---
root = tk.Tk()
root.title("💬 Chatbot")
root.attributes("-fullscreen", True)
root.bind("<Escape>", exit_app)

# --- Dark theme colors ---
chat_bg = "#121212"
header_bg = "#1F1F1F"
entry_bg = "#2D2D2D"
send_btn_bg = "#00796B"
send_btn_fg = "#FFFFFF"
exit_btn_bg = "#D32F2F"

# --- Header bar ---
header = tk.Frame(root, bg=header_bg)
header.pack(fill=tk.X)

title = tk.Label(header, text="💬 ChartBot - Dark Mode Chat", bg=header_bg, fg="white", font=("Segoe UI", 16, "bold"))
title.pack(side=tk.LEFT, padx=20, pady=10)

exit_btn = tk.Button(header, text="Exit", bg=exit_btn_bg, fg="white", font=("Segoe UI", 12),
                     command=exit_app)
exit_btn.pack(side=tk.RIGHT, padx=20, pady=10)

# --- Chat area ---
chat_frame = Frame(root, bg=chat_bg)
chat_frame.pack(fill=tk.BOTH, expand=True)

canvas = Canvas(chat_frame, bg=chat_bg, bd=0, highlightthickness=0)
scrollbar = Scrollbar(chat_frame, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas, bg=chat_bg)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# --- Input field ---
input_frame = Frame(root, bg=entry_bg, pady=10)
input_frame.pack(fill=tk.X, side=tk.BOTTOM)

# Text entry with placeholder behavior
def on_entry_click(event):
    if msg_entry.get() == "Type a message...":
        msg_entry.delete(0, tk.END)
        msg_entry.config(fg="black")

def on_focus_out(event):
    if msg_entry.get() == "":
        msg_entry.insert(0, "Type a message...")
        msg_entry.config(fg="gray")

msg_entry = tk.Entry(input_frame,
                     font=("Segoe UI", 13),
                     bg="white", fg="gray",
                     bd=0, relief="flat", insertbackground="black")
msg_entry.pack(fill=tk.BOTH, expand=True, padx=(15, 5), pady=5, side=tk.LEFT, ipady=6)
msg_entry.insert(0, "Type a message...")
msg_entry.bind("<FocusIn>", on_entry_click)
msg_entry.bind("<FocusOut>", on_focus_out)
msg_entry.bind("<Return>", send_message)

# Send Button with custom style and hover effect
def on_enter(e):
    send_btn.config(bg="#128C7E")

def on_leave(e):
    send_btn.config(bg=send_btn_bg)

send_btn = tk.Button(
    input_frame, text="Send",
    font=("Segoe UI", 12, "bold"),
    bg=send_btn_bg, fg="white",
    activebackground="#128C7E",
    bd=0, padx=20, pady=5,
    command=send_message
)
send_btn.pack(side=tk.RIGHT, padx=(5, 15), pady=5)
send_btn.bind("<Enter>", on_enter)
send_btn.bind("<Leave>", on_leave)


# --- Initial message ---
display_message("Bot", "👋 Welcome! I'm Bot. Type 'exit' or press [Esc] to close.", align="left", bg="#1A1A40")

root.mainloop()
