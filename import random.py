import random
def hangman():
    words = ["harshad", "python", "programming", "developer", "function" ]
    secret_word = random.choice(words)
    guessed_letters = []
    attempts_left = 6
    display_word = ["_" for _ in secret_word]
    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print("You have 6 incorrect guesses.")
    while attempts_left > 0:
        print("Word:", " ".join(display_word))
        print("Guessed letters:", guessed_letters)
        print("Attempts left:", attempts_left)
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        guessed_letters.append(guess)
        if guess in secret_word:
            print("Correct guess!")
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    display_word[i] = guess
        else:
            print("Wrong guess!")
            attempts_left -= 1
        if "_" not in display_word:
            print("Congratulations! You guessed the word:", secret_word)
            return
    print("Game Over! The word was:", secret_word)
hangman()
