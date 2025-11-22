import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("🔐 PASSWORD GENERATOR")

    while True:
        try:
            length = int(input("\nEnter password length (min 6): "))
            if length < 6:
                print("⚠️ Length must be at least 6!")
                continue

            count = int(input("How many passwords to generate? "))

            print("\n🔑 Generated Password(s):")
            for i in range(count):
                print(f"{i+1}. {generate_password(length)}")

            again = input("\nGenerate again? (yes/no): ").lower()
            if again != "yes":
                print("\n👋 Exiting Password Generator...")
                break

        except ValueError:
            print("⚠️ Please enter valid numbers!")

# Run the tool
password_generator()
