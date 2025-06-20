
import secrets
import string

# ---------- helper functions ----------

def get_positive_int(prompt: str) -> int:
    """Ask for a positive integer until the user gives one."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive number.")
        except ValueError:
            print("That doesn’t look like a number. Try again.")

def get_yes_no(prompt: str) -> bool:
    """Return True for y/Y, False for n/N; keep asking otherwise."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in {"y", "n"}:
            return choice == "y"
        print("Please enter y or n.")

def build_pool(use_letters: bool, use_numbers: bool, use_symbols: bool) -> str:
    """Build the character pool based on user choices."""
    pool = ""
    if use_letters:
        pool += string.ascii_letters          # a‑zA‑Z
    if use_numbers:
        pool += string.digits                 # 0‑9
    if use_symbols:
        pool += string.punctuation            # !@#$…
    return pool

def generate_password(length: int,
                      pool: str,
                      need_letters: bool,
                      need_numbers: bool,
                      need_symbols: bool) -> str:
    """Generate a password that meets all selected criteria."""
    while True:  # loop until it satisfies all requirements
        pwd = ''.join(secrets.choice(pool) for _ in range(length))
        if need_letters   and not any(ch.isalpha() for ch in pwd):
            continue
        if need_numbers   and not any(ch.isdigit() for ch in pwd):
            continue
        if need_symbols   and not any(ch in string.punctuation for ch in pwd):
            continue
        return pwd

# ---------- main program ----------

def main():
    print("=== Password Generator ===")

    length = get_positive_int("Desired password length: ")

    print("\nInclude the following (y/n):")
    use_letters = get_yes_no(" • Letters (a‑z, A‑Z)? ")
    use_numbers = get_yes_no(" • Numbers (0‑9)?       ")
    use_symbols = get_yes_no(" • Symbols (!,@,#, etc.)? ")

    # Ensure at least one type is chosen
    if not (use_letters or use_numbers or use_symbols):
        print("\nYou must choose at least one character type. Restarting...\n")
        return main()

    pool = build_pool(use_letters, use_numbers, use_symbols)
    password = generate_password(length, pool,
                                 use_letters, use_numbers, use_symbols)

    print("\nYour generated password:")
    print(password)

if __name__ == "__main__":
    main()
