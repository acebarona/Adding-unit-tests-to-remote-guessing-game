import socket
import random

host = "127.0.0.1"  
port = 7777         

# bot_player.py

class BotPlayer:
    def __init__(self, lower=1, upper=100):
        self.lower = lower
        self.upper = upper
        self.last_guess = None

    def make_guess(self):
        self.last_guess = (self.lower + self.upper) // 2
        return self.last_guess

    def update(self, feedback):
        if feedback == "higher":
            self.lower = self.last_guess + 1
        elif feedback == "lower":
            self.upper = self.last_guess - 1


def get_range(difficulty):
    if difficulty == 1:
        return 1, 10
    elif difficulty == 2:
        return 1, 50
    return 1, 100

def main():
    s = socket.socket()
    s.connect((host, port))

    print(s.recv(1024).decode())
    difficulty = random.choice([1,2,3])
    print(f"Bot Choose {difficulty} difficulty")
    s.sendall(str(difficulty).encode())

    min_val, max_val = get_range(difficulty)
    print("Starting bot with range:", min_val, "-", max_val)

    print(s.recv(1024).decode())

    while True:
        guess = (min_val + max_val) // 2
        print(f"Bot guesses: {guess}")
        s.sendall(str(guess).encode())
        reply = s.recv(1024).decode().strip()
        print(reply)

        if "CORRECT!" in reply:
            break
        elif "Guess Higher" in reply:
            min_val = guess + 1
        elif "Guess Lower" in reply:
            max_val = guess - 1

    s.close()

if __name__ == "__main__":
    main()