import re

def sort_words(text):
    words = re.findall(r'\b[a-zA-Zа-щА-ЩьЬюЮяЯіІїЇєЄґҐ]+\b', text)

    def custom_sort(word):
        ukr_alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
        word_lower = word.lower()

        if word_lower[0] in ukr_alphabet:
            return (0, word_lower)
        else:
            return (1, word_lower)

    sorted_words = sorted(words, key=custom_sort)
    return sorted_words

def main():
    try:
        with open('input.txt', 'r', encoding='utf-8') as file:
            full_text = file.read()

        #full_text = full_text.strip()
        sorted_words = sort_words(full_text)

        print('Відсортовані слова:', sorted_words)
        print('Кількість слів:', len(sorted_words))

    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")

main()
