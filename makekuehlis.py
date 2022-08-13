#! /usr/bin/env python
import pandas as pd
import sys


def get_kg_lists(frame: pd.DataFrame):
    all_lists = []
    for column in frame:
        list1 = list(frame[column])
        cleaned_list = [x for x in list1 if type(x) == str]
        current_length = len(cleaned_list)
        fillup = (8 - current_length % 8) % 8
        print(fillup)
        for counter in range(fillup):
            cleaned_list.append(" ")
        all_lists.append(cleaned_list)
    return all_lists


frame = pd.read_excel("kochgruppennamen.xlsx")

list_of_lists = get_kg_lists(frame)
for list in list_of_lists:
    print(f"list of length {len(list)}")
    print("\n".join(list))
    print("end")
sys.exit()
# def file_to_list(file):
#     with open(file, "r") as file_object:
#         my_variable = file_object.read().splitlines()
#     return list(
#         filter(None, pd.unique(my_variable).tolist())
#     )  # Remove Empty/Duplicates Values


# kochgruppen1 = file_to_list("ps1.txt")
# kochgruppen2 = file_to_list("ps2.txt")
# kochgruppen3 = file_to_list("ps3.txt")
# kochgruppen4 = file_to_list("ps4.txt")

# kochgruppen = [kochgruppen1, kochgruppen2, kochgruppen3, kochgruppen4]

# file = open("superliste.tex", "w")
# file.write(
#     "\\documentclass{article}\\usepackage[ngerman]{babel}\\usepackage{geometry}\\usepackage{lmodern}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\pagestyle{empty}\n\\begin{document}\n"
# )


for packstreet_number in range(4):
    for j in range(4):
        if packstreet_number == 3 and j == 3:
            continue
        file.write("\\begin{table}[p]\n  \\begin{tabular}{ll}")
        for i in range(3):
            file.write(
                "    \\hspace{-2em}    \\fbox{\\begin{minipage}[t][6cm][t]{8cm}\n        \\fontsize{45}{54} \\selectfont\n        \\phantom{ }\\\\\n      \\phantom{ }"
            )
            file.write(str(packstreet_number + 1))
            file.write(" ")
            file.write(kochgruppen[packstreet_number][6 * j + 2 * i])
            file.write(
                "    \\end{minipage}}\n    &\n\\fbox{\\begin{minipage}[t][6cm][t]{8cm}\n        \\fontsize{45}{54} \\selectfont\n        \\phantom{ }\\\\\n        \\phantom{ } "
            )
            file.write(str(packstreet_number + 1))
            file.write(" ")
            file.write(kochgruppen[packstreet_number][6 * j + 2 * i + 1])
            file.write("      \end{minipage}}\\\\")
        file.write("\\end{tabular}\n\\end{table}\n\n\n")
file.write("\\end{document}")
