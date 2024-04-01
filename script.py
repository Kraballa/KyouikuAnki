import genanki
import codecs

model = genanki.Model(
    1866456749,
    "Kyoiku Model",
    fields= [
        {"name": "Kanji"},
        {"name": "Grade"},
        {"name": "Meaning"},
        {"name": "Onyomi"},
        {"name": "Kunyomi"},
    ],
    templates=[
        {
            "name": "Kyoiku Card",
            "qfmt": "{{Kanji}}",
            "afmt": "{{Kanji}}<hr/><p class='small'>Grade {{Grade}}</p>{{Meaning}}<br/>on: {{Onyomi}}<br/>kun: {{Kunyomi}}"
        }
    ],
    css=".card {font-family: 'ヒラギノ角ゴ Pro W3', 'Hiragino Kaku Gothic Pro', Osaka, 'メイリオ', Meiryo, 'ＭＳ Ｐゴシック', 'MS PGothic', 'MS UI Gothic', sans-serif;font-size: 50px; text-align:center; color: Black;} .small {font-size:20px;}"
)

files = ["grade1.txt", "grade2.txt", "grade3.txt", "grade4.txt", "grade5.txt", "grade6.txt"]

if __name__ == "__main__":

    deck = genanki.Deck(
        2099032349,
        "Kyouiku Kanji"
    )

    for i, grade in enumerate(files):
        with codecs.open(grade, encoding="utf-8") as file:
            for line in file:
                split = line.rstrip().split("\t")

                note = genanki.Note(
                    model=model,
                    fields=[split[0], f"{i+1}", split[1], split[2], split[3]]
                )
                deck.add_note(note)
    
    genanki.Package(deck).write_to_file('out.apkg')