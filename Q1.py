def highest_frequency_word_length(string):
    # Split the string into words
    words = string.split()

    # Count the frequency of each word
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    # Find the highest frequency
    max_frequency = max(frequency.values())

    # Find the length of the highest-frequency word
    highest_frequency_word = max(word for word, freq in frequency.items() if freq == max_frequency)
    highest_frequency_word_length = len(highest_frequency_word)

    return highest_frequency_word_length


# Example usage
string = "write write write all the number from from from 1 to 100"
print(highest_frequency_word_length(string))
