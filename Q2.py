def is_valid_string(s):
    # Count the frequency of each character
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1

    # Count the frequency of each frequency count
    frequency_count = {}
    for freq in frequency.values():
        frequency_count[freq] = frequency_count.get(freq, 0) + 1

    # If there is only one unique frequency count, it is a valid string
    if len(frequency_count) == 1:
        return "YES"

    # If there are more than two unique frequency counts, it is not a valid string
    if len(frequency_count) > 2:
        return "NO"

    frequencies = list(frequency_count.keys())
    counts = list(frequency_count.values())

    # Check if the difference between the two frequency counts is 1 and occurs only once
    if counts.count(1) == 1 and (frequencies[counts.index(1)] - frequencies[counts.index(max(frequencies))] == 1 or frequencies[counts.index(1)] == 1):
        return "YES"

    # Check if the difference between the two frequency counts is 1 and occurs only at the minimum frequency count
    if counts.count(max(counts)) == 1 and frequencies[counts.index(max(counts))] - frequencies[counts.index(min(frequencies))] == 1:
        return "YES"

    return "NO"


# Example usage
s = "aabbcc"
print(is_valid_string(s))  
