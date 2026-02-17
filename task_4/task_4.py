from __future__ import annotations


def parse_input(user_input: str) -> tuple[str, list[str]]:
    parts = user_input.strip().split()
    if not parts:
        return "", []
    command = parts[0].lower()
    args = parts[1:]
    return command, args


def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 2:
        return "Invalid command."
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 2:
        return "Invalid command."
    name, phone = args
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated."


def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 1:
        return "Invalid command."
    name = args[0]
    return contacts.get(name, "Contact not found.")


def show_all(contacts: dict[str, str]) -> str:
    if not contacts:
        return "No contacts saved."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main() -> None:
    contacts: dict[str, str] = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break
        if command == "hello":
            print("How can I help you?")
            continue
        if command == "add":
            print(add_contact(args, contacts))
            continue
        if command == "change":
            print(change_contact(args, contacts))
            continue
        if command == "phone":
            print(show_phone(args, contacts))
            continue
        if command == "all":
            print(show_all(contacts))
            continue

        print("Invalid command.")


def _self_check() -> None:
    c: dict[str, str] = {}
    assert parse_input("ADD John 123") == ("add", ["John", "123"])
    assert add_contact(["John", "123"], c) == "Contact added."
    assert show_phone(["John"], c) == "123"
    assert change_contact(["John", "555"], c) == "Contact updated."
    assert show_phone(["John"], c) == "555"
    assert "John: 555" in show_all(c)
    print("task_4: all asserts passed")


if __name__ == "__main__":
    _self_check()
    main()
