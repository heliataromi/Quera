def guess_generator_iterator(guess_generator, min_value, max_value, assumed_number):
    generator = guess_generator(min_value, max_value)
    guess = next(generator)
    guesses = [guess]
    output = [guess]

    try:
        while True:
            if guess > assumed_number:
                guess = generator.send('G')
                guesses.append(guess)
                output.append(guess)
                if guess >= guesses[-2]:
                    output.append('!')

            elif guess < assumed_number:
                guess = generator.send('L')
                guesses.append(guess)
                output.append(guess)
                if guess <= guesses[-2]:
                    output.append('!')

            elif guess == assumed_number:
                guess = generator.send('E')
                guesses.append(guess)
                output.append(guess)
                output.append('!')

            if output.count('!') == 3:
                output.append('!!!')
                raise StopIteration

    except StopIteration:
        return output
