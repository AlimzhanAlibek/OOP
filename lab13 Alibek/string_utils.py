def capitalize_words(text):
   return ' '.join([word.capitalize() for word in text.split()])

def count_letters(text):
    return len([char for char in text if char.isalpha()])
