import random
import string

game_over = False
game_start = True

word_lst = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(word_lst)
lives = 8

print("H A N G M A N")

guessed = []
dashes = []


while game_start:
    game = input('\nType "play" to play the game, "exit" to quit: ')
    if game == "play":

        for _ in word:
            dashes.append("-")

        while not game_over:

            print(f"\n{''.join(dashes)}")
            guess = input("Input a letter: ")

            if len(guess) != 1:
                print("You should input a single letter")
                continue
            if guess not in list(string.ascii_lowercase):
                print("Please enter a lowercase English letter")
                continue

            for i in range(len(word)):
                if guess == word[i]:
                    dashes[i] = guess

            if guess in guessed:
                print(f"You've already guessed this letter")


            if guess not in guessed:
                if guess not in word:
                    lives -= 1
                    print(f"That letter doesn't appear in the word")

            guessed.append(guess)

            if lives == 0:
                game_over = True
                print("You lost!")

            if "-" not in dashes:
                print(f"\n{''.join(dashes)}")
                print("You guessed the word!\nYou survived!")
                game_over = True

    elif game == 'exit':
        game_start = False
    else:
        continue
