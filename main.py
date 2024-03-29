"""
This program was created in order to help learning japanese words that the user could write with the kanji that they
currently know by creating an Anki deck. In order to do that, the user needs to populate the 'known.txt' file with the
kanji that they know, without quotes and with one kanji per line.
Procedure:
0) Install genanki and ankipandas
1) (optional)If you have a kanji deck in Anki, when prompted, press 1 to generate a csv file with your Anki cards
2) Populate known.txt with the kanji you know (no need to add hiragana, they are already included)
3) When prompted by the program, press 2 to generate the Anki deck with potential words.
"""

import csv

import genanki
import PySimpleGUI as sg


def extract_kanji():
    """
    This function is used to generate a csv file from the user's Anki
    profile so that they may more easily create the
    necessary txt file
    """
    from ankipandas import Collection

    col = Collection()
    col.notes.to_csv("vocab.csv", encoding="utf-8-sig")


def generate_deck():
    """
    This function generates a new Anki deck that has the words you can
    form with the kanji and hiragana that you
    currently know.
    """
    with open("known.txt", "r", encoding="utf8") as file:
        known_kanji = []
        for line in file:
            known_kanji.append(line.replace("\n", "").strip())

    jp_en_dictionary = []
    with open("vocabulary.csv", "r", encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            jp_en_dictionary.append(row)

    count = 0
    possible_vocabulary = []
    for elm in jp_en_dictionary:
        testing = []
        for char in elm[0]:
            testing.append(char in known_kanji)
        if all(testing):
            possible_vocabulary.append(elm)
            count += 1

    print(f"Your deck has {count} cards.")

    my_model = genanki.Model(
        1607392319,
        "Simple Model",
        fields=[
            {"name": "Japanese Word"},
            {"name": "Type"},
            {"name": "Furigana"},
            {"name": "Translation"},
        ],
        templates=[
            {
                "name": "Base Card",
                "qfmt": """
<div
  style="font-family: Arial; text-align: center; font-size: 20px; padding: 20px"
>
  {{Japanese Word}}
</div>
<div
  style="font-family: Arial; text-align: center; font-size: 20px; padding: 20px"
>
  {{Type}}
</div>
""",
                "afmt": """
{{FrontSide}}
<hr id="answer" />
<div
  style="font-family: Arial; text-align: center; font-size: 20px; padding: 20px"
>
  {{Furigana}}
</div>
<div
  style="font-family: Arial; text-align: center; font-size: 20px; padding: 20px"
>
  {{Translation}}
</div>
""",
            },
        ],
    )

    my_deck = genanki.Deck(2059400110, "Japanese Vocabulary")

    for word in possible_vocabulary:
        my_note = genanki.Note(
            model=my_model, fields=[word[0], word[3], word[2], word[1]]
        )
        my_deck.add_note(my_note)

    genanki.Package(my_deck).write_to_file("Japanese Vocabulary.apkg")


def get_input():
    """This function creates a simple GUI to get the user's input"""
    layout = [
        [
            sg.Radio("Generate csv file", "RADIO1", default=True, key="csv"),
            sg.Radio("Generate Anki deck", "RADIO1", key="deck"),
        ],
        [sg.Button("Ok")],
    ]
    window = sg.Window("Anki Deck Generator", layout)
    event, values = window.read()
    window.close()
    return values["csv"], values["deck"]


def main():
    """This function is the main function of the program"""
    csv_file, deck = get_input()
    if csv_file:
        extract_kanji()
    elif deck:
        generate_deck()
    else:
        print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
