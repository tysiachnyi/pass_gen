import string
import random
import pyperclip


def display_error(func, text):
    """
    Display an error message.

    Args:
        func (str): The name of the function where the error occurred.
        text (str): The error message to display.
    """
    print(f"Error in function {func}: {text}")


def generate_password(domain=" ", length=14):

    if length < 14:
        display_error("generate_password", "length of password is less than 14")
        raise ValueError("Length of password must be at least 14")

    filename = "passwords.txt"

    characters = string.ascii_letters + string.digits + string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))

    with open(filename, "a") as file:
        file.write(f"""{domain} _ {password} \n""")


def find_password(domain):
    print(domain)
    credentials = {}
    with open("passwords.txt", "r") as file:
        lines = file.read().split("\n")

        for line in lines:
            if line.strip():
                parts = line.split(" _ ")
                if len(parts) == 2:
                    username = parts[0]
                    password = parts[1]
                    credentials[username] = password
    print(credentials[domain])
    pyperclip.copy(credentials[domain])


def main():
    print("""Hey! this is a password generator""")

    type = input("g-generate, u-update, v-view: ")

    if type == "g":
        domain = input("key pls: ")
        length = int(input("length pls (min 14): "))
        generate_password(domain, length)

    if type == "v":
        domain = input("key pls: ")
        find_password(domain)


if __name__ == "__main__":
    main()
