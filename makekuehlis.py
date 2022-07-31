kochgruppen1 = [
    "Beige",
    "Blau",
    "Braun",
    "Goldgelb",
    "Grau",
    "Gruen",
    "Kaminrot",
    "Korallenrot",
    "Lila",
    "Ocker",
    "Orange",
    "Petrol",
    "Pink",
    "Purpur",
    "Sand",
    "Schwarz",
    "Silber",
    "Tuerkis",
    "Ultramarin",
    "Violet",
    "Weiss",
    "Zitronengelb",
    " ",
    " ",
    " ",
]

kochgruppen2 = [
    "Adler",
    "Eisbaer",
    "Elefant",
    "Erd- maennchen",
    "Giraffe",
    "Gorilla",
    "Hund",
    "Kaenguru",
    "Katze",
    "Krokodil",
    "Loewe",
    "Luchs",
    "Maus",
    "Nashorn",
    "Panda",
    "Pelikan",
    "Pinguin",
    "Pottwal",
    "Robbe",
    "Schildkroete",
    "Storch",
    "Tiger",
    " ",
    " ",
    " ",
]

kochgruppen3 = [
    "Akkordeon",
    "Banjo",
    "Cello",
    "Dudelsack",
    "Floete",
    "Geige",
    "Harfe",
    "Horn",
    "Kazoo",
    "Klarinette",
    "Klavier",
    "Kontrabass",
    "Mandoline",
    "MAV",
    "MAV-veg",
    "Mund- harmonika",
    "Oboe",
    "Pauke",
    "Triangel",
    "Trommel",
    "Trompete",
    "Tuba",
    "Ukulele",
    "Xylophon" " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
]

kochgruppen4 = [
    "Ahorn",
    "Birke",
    "Buche",
    "Eberesche",
    "Eiche",
    "Ginko",
    "Kastanie",
    "Lerche",
    "Linde",
    "Mammut- baum",
    "Pappel",
    "Tanne",
    "Ulme",
    "Wacholder",
    "Walnuss",
    "Weide",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
]

kochgruppen = [kochgruppen1, kochgruppen2, kochgruppen3, kochgruppen4]

file = open("superliste.tex", "w")
file.write(
    "\\documentclass{article}\\usepackage[ngerman]{babel}\\usepackage{geometry}\\usepackage{lmodern}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\pagestyle{empty}\n\\begin{document}\n"
)


for k in range(4):
    for j in range(4):
        if k == 3 and j == 3:
            continue
        file.write("\\begin{table}[p]\n  \\begin{tabular}{ll}")
        for i in range(3):
            file.write(
                "    \\hspace{-2em}    \\fbox{\\begin{minipage}[t][6cm][t]{8cm}\n        \\fontsize{45}{54} \\selectfont\n        \\phantom{ }\\\\\n      \\phantom{ }"
            )
            file.write(str(k + 1))
            file.write(" ")
            file.write(kochgruppen[k][6 * j + 2 * i])
            file.write(
                "    \\end{minipage}}\n    &\n\\fbox{\\begin{minipage}[t][6cm][t]{8cm}\n        \\fontsize{45}{54} \\selectfont\n        \\phantom{ }\\\\\n        \\phantom{ } "
            )
            file.write(str(k + 1))
            file.write(" ")
            file.write(kochgruppen[k][6 * j + 2 * i + 1])
            file.write("      \end{minipage}}\\\\")
        file.write("\\end{tabular}\n\\end{table}\n\n\n")
file.write("\\end{document}")
