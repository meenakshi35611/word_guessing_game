import random
word_bank = [
    "journey", "capture", "lantern", "puzzle", "whisper",
    "thunder", "mission", "blanket", "freedom", "harvest",
    "melody", "sunrise", "balance", "trouble", "radiant",
    "orchard", "fantasy", "courage", "gravity", "kingdom",
    "venture", "mystery", "library", "glacier", "emerald"
]
word= random.choice(word_bank)
guessedword= ['_']*len(word)
attempts = 6
while attempts>0:
    print('\nCurrent word: ' + ' '.join(guessedword))
    guess=input('Guess a letter: ')
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedword[i] = guess
        print('Great guess!')
    else:
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))
    
    if '_' not in guessedword:
        print('\nCongratulations!! You guessed the word: ' + word)
        break
        
    elif '_' in guessedword  and attempts==0:
        print('\nYou\'ve run out of attempts! The word was: ' + word)