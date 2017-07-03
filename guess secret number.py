secret = 12

guess= int(raw_input("Guess the secret number(between 1 and 20):"))

if guess== secret:
    print"You guessed it - congratulations!"

else:
    print"Sorry, your guess is not correct...secret number is not" + str(guess)