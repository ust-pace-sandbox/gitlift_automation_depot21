import random
import time
from datetime import datetime

def generate_random_password(length=12):
    """Generate a random password with letters, digits, and special characters."""
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def roll_dice(num_dice=2):
    """Simulate rolling dice."""
    rolls = [random.randint(1, 6) for _ in range(num_dice)]
    return rolls, sum(rolls)

def guess_number_game():
    """Simple number guessing game."""
    target = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print("\n🎮 Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts.")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            
            if guess < target:
                print("📈 Too low!")
            elif guess > target:
                print("📉 Too high!")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                return
        except ValueError:
            print("❌ Please enter a valid number.")
    
    print(f"\n😢 Game over! The number was {target}")

def main():
    print("=" * 50)
    print("Random Python Program Demo")
    print(f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    # Generate random passwords
    print("\n🔐 Random Passwords:")
    for i in range(3):
        print(f"  Password {i+1}: {generate_random_password()}")
    
    # Roll dice
    print("\n🎲 Rolling 2 dice:")
    rolls, total = roll_dice()
    print(f"  Rolls: {rolls}")
    print(f"  Total: {total}")
    
    # Random choices
    print("\n🎯 Random Selections:")
    colors = ["Red", "Blue", "Green", "Yellow", "Purple"]
    print(f"  Random color: {random.choice(colors)}")
    print(f"  Random number (1-100): {random.randint(1, 100)}")
    print(f"  Random float (0-1): {random.random():.4f}")
    
    # Play guessing game
    play = input("\n🎮 Would you like to play the guessing game? (yes/no): ").lower()
    if play in ['yes', 'y']:
        guess_number_game()
    
    print("\n👋 Thanks for running this random program!")

if __name__ == "__main__":
    main()
