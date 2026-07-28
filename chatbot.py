def get_response(message):

    msg = message.lower()

    if "fantasy" in msg:
        return """Recommended Books:
• Harry Potter
• The Hobbit
• Percy Jackson"""

    elif "mystery" in msg:
        return """Recommended Books:
• Sherlock Holmes
• Murder on the Orient Express"""

    elif "romance" in msg:
        return """Recommended Books:
• Pride and Prejudice
• It Ends With Us"""

    elif "self" in msg:
        return """Recommended Books:
• Atomic Habits
• Deep Work"""

    elif "happy" in msg:
        return "Try Harry Potter or The Alchemist."

    elif "sad" in msg:
        return "The Midnight Library is a great choice."

    elif "dan brown" in msg:
        return "Read The Da Vinci Code."

    elif "jk rowling" in msg:
        return "Harry Potter Series."

    elif "hi" in msg or "hello" in msg:
        return "Hello! 👋 Tell me your favourite genre, author or mood."

    elif "bye" in msg:
        return "Goodbye! Happy Reading 📚"

    return "Please tell me a genre, author or mood."
  
