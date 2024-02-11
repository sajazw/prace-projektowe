

zmienna1 = 'Witaj'
zmienna2 = input('podaj imię:')

print(zmienna1 + " " + zmienna2)

import random

# Lista pytań w formacie: (pytanie, odpowiedzi, poprawna odpowiedź)
questions = [
    ("Jaka jest stolica Polski?", ["A. Warszawa", "B. Kraków", "C. Gdańsk", "D. Wrocław"], "A"),
    ("Ile wynosi pierwiastek z 16?", ["A. 2", "B. 4", "C. 8", "D. 16"], "B"),
    ("Kto napisał \"Pan Tadeusz\"?", ["A. Adam Mickiewicz", "B. Juliusz Słowacki", "C. Henryk Sienkiewicz", "D. Jan Kochanowski"], "A"),
    ("Kto był pierwszym prezydentem USA?", ["A. George Washington", "B. Thomas Jefferson", "C. Abraham Lincoln", "D. John Adams"], "A"),
    ("Które państwo jest największe pod względem powierzchni?", ["A. Rosja", "B. Kanada", "C. Chiny", "D. Stany Zjednoczone"], "B"),
    ("Który pierwiastek chemiczny jest symbolizowany literą 'O'?", ["A. Tlen", "B. Węgiel", "C. Wodór", "D. Azot"], "A"),
    ("Jaki jest stolicą Francji?", ["A. Londyn", "B. Paryż", "C. Madryt", "D. Rzym"], "B"),
    ("Który pierwiastek chemiczny jest symbolem 'H'?", ["A. Węgiel", "B. Wodór", "C. Hel", "D. Azot"], "B"),
    ("Kto napisał powieść 'Zbrodnia i kara'?",
     ["A. Fiodor Dostojewski", "B. William Shakespeare", "C. Charles Dickens", "D. Leo Tolstoj"], "A"),
    ("Jak nazywa się największa planeta w Układzie Słonecznym?", ["A. Mars", "B. Jowisz", "C. Saturn", "D. Ziemia"],
     "B"),
    ("Który zespół wykonał przebój 'Bohemian Rhapsody'?",
     ["A. The Beatles", "B. Queen", "C. Led Zeppelin", "D. Pink Floyd"], "B")
]

def ask_question(question, options):
    print(question)
    for option in options:
        print(option)
    user_answer = input("Odpowiedź (wpisz literę): ").upper()
    return user_answer


def main():
    print("Witaj w grze Milionerzy!")
    pieniądze = 0
    for i, (question, options, correct_answer) in enumerate(questions, start=1):
        print(f"Pytanie {i}:")
        user_answer = ask_question(question, options)
        if user_answer == correct_answer:
            print("Poprawna odpowiedź! Wygrywasz kolejne 1000 złotych!")
            pieniądze += 1000
        else:
            print("Niestety, to nie jest poprawna odpowiedź.")
            break
    print(f"Koniec gry! Wygrałeś {pieniądze} złotych!")



if __name__ == "__main__":
    main()