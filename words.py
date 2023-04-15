def print_upper_words(words, start_letters):
    """Prints each word in the given list on a separate line in all uppercase, but only if the word starts with one of the letters in the given start_letters set."""
    for word in words:
        if word[0].lower() in start_letters:
            print(word.upper())