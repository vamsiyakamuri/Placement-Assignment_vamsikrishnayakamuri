def count_pos_tags(text):
    verbs = 0
    nouns = 0
    pronouns = 0
    adjectives = 0

    words = text.split()

    for word in words:
        if word.endswith('ing') or word.endswith('ed'):
            verbs += 1
        elif word.endswith('s') or word.endswith('es'):
            nouns += 1
        elif word.lower() in ['he', 'she', 'it', 'they', 'we', 'i', 'you']:
            pronouns += 1
        elif word.endswith('ful') or word.endswith('ous'):
            adjectives += 1

    pos_counts = {
        'Verbs': verbs,
        'Nouns': nouns,
        'Pronouns': pronouns,
        'Adjectives': adjectives
    }

    return pos_counts

# Take user input
text = input("Enter a phrase or paragraph: ")

# Call the function and compute counts
counts = count_pos_tags(text)

# Print the counts
for pos, count in counts.items():
    print(f"{pos}: {count}")
