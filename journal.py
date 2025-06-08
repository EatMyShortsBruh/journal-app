def save_to_file(content, filename="journal.txt"):
    if content:
        with open(filename, "a") as f:
            f.write(content + "\n\n")

def read_from_file():
    try:
        with open("journal.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return "No enrtries found."

