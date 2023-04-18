import random

words = ['apple', 'banana', 'cherry', 'grapefruit', 'kiwi', 'lemon', 'mango', 'orange', 'pineapple', 'strawberry']


def draw_hangman(attempts_left):
    hangman_parts = [
        ' O ',
        '/|\\',
        '/ \\'
    ]
    for i, part in enumerate(hangman_parts[:3 - attempts_left]):
        print(part)


def main():
    word = random.choice(words)
    guessed_word = ['_' for _ in word]
    attempts_left = 3
    guessed_letters = set()

    while attempts_left > 0 and '_' in guessed_word:
        print(' '.join(guessed_word))
        draw_hangman(attempts_left)
        print('Угаданные буквы:', ', '.join(sorted(guessed_letters)))

        letter = input('Введите букву: ').lower()
        if letter in guessed_letters:
            print('Вы уже вводили эту букву.')
            continue

        guessed_letters.add(letter)

        if letter in word:
            for i, c in enumerate(word):
                if c == letter:
                    guessed_word[i] = letter
        else:
            attempts_left -= 1

    draw_hangman(attempts_left)

    if attempts_left > 0:
        print('Поздравляем, вы угадали слово:', word)
    else:
        print('Вы проиграли. Загаданное слово было:', word)


if __name__ == '__main__':
    main()

