
class User:
    def __init__(self, user_name, email, pass_word):
        self.user_name = user_name
        self.email = email
        self.pass_word = pass_word

    def display(self):
        print(f"Username: {self.user_name} | Email: {self.email}", end=" ")

    def is_gmail(self):
        return self.email.endswith("@gmail.com")


def main():
    users = []

    while True:
        user_name = input("Enter username (0 to stop): ")

        if user_name == "0":
            break

        email = input("Enter email: ")
        pass_word = input("Enter password: ")

        user = User(user_name, email, pass_word)
        users.append(user)

    print(f"\nTotal users: {len(users)}")

    for number, user in enumerate(users, start=1):
        print(f"{number}. ", end="")
        user.display()

        if user.is_gmail():
            print("| Gmail: YES")
        else:
            print("| Gmail: NO")


if __name__ == "__main__":
    main()
