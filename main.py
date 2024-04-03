import string
import random


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


def main():
    print("""Hey! this is a password generator""")

    type = input("g-generate, u-update, v-view: ")
    # logic for type

    if type == "g":
        domain = input("key pls: ")
        length = int(input("length pls (min 14): "))
        generate_password(domain, length)


if __name__ == "__main__":
    main()
