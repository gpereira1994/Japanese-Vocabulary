# Japanese-Vocabulary
This program creates an Anki deck with japanese words that you can learn based
on the kanji that you currently know. This uses the 
[ankipandas](https://pypi.org/project/ankipandas/) 
and [genanki](https://github.com/kerrickstaley/genanki) packages to create 
said decks. 
The vocabulary words were extracted from the 
[Ultimate WaniKani deck](https://ankiweb.net/shared/info/266084933).

Procedure:

1. install[anki](https://apps.ankiweb.net/)
1. Install ankipandas and genanki packages
1. (Optional) If you have an Anki deck with the kanji that you know, when 
prompted for an input, press 1. This will generate a csv file with all card
notes in your Anki profile for you to extract your kanji.
1. Populate the 'known.txt' file with the kanji that you know (the hiragana 
are already included)
1. Run the program once more, and when prompted, press 2 to generate the Anki
deck with the words you can potentially write.

The cards are a simple Front and Back type. The front has the new vocabulary 
word, in kanji, as well as the word type(e.g. noun, i-adjective, na-adjective,
etc). In the back are the reading of the word, as well as the translation. 
The documentation of those two packages are linked so that the user can change 
the deck so that they may customize towards their preference.
