# lab13/string_utils.py

def capitalize_words(text):
    """Функция для капитализации каждого слова в строке."""
    return ' '.join([word.capitalize() for word in text.split()])

def count_letters(text):
    """Функция для подсчета букв в строке (игнорирует цифры и спецсимволы)."""
    return len([char for char in text if char.isalpha()])
