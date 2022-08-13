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
        # print(fillup)
        for counter in range(fillup):
            cleaned_list.append(" ")
        all_lists.append(cleaned_list)
    return all_lists


frame = pd.read_excel("kochgruppennamen.xlsx")

list_of_lists = get_kg_lists(frame)
# for current_list in list_of_lists:
#     print(f"list of length {len(current_list)}")
#     print("\n".join(current_list))
#     print("end")
# sys.exit()


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

# kochgruppen = [kochgruppen1, kochgruppen2, kochgruppen3, kochgruppen4]

file = open("kuehlkistenkarten.tex", "w")
file.write(
    "\\documentclass[a4paper]{article}\n\\usepackage[ngerman]{babel}\n\\usepackage[textwidth=17cm,textheight=25cm]{geometry}\n\\usepackage{lmodern}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{adjustbox}\n\\pagestyle{empty}\n\\begin{document}\n\centering\n"
)

packstreet_number = 0
for packstreet in list_of_lists:
    packstreet_number += 1
    for page_number in range(int(len(packstreet) / 8)):
        file.write("\\begin{table}[p]\n  \\begin{tabular}{ll}")
        for i in range(4):
            if packstreet[0] != " ":
                file.write(
                    "\\fbox{\\begin{minipage}[t][6cm][t]{8cm}\n\\centering\n\\fontsize{40}{48} \\selectfont\n        \\phantom{ }\\\\\n      \\phantom{ }"
                )
                file.write(str(packstreet_number))
                file.write("\\newline ")
                file.write("\\maxsizebox{8cm}{!}{")
                file.write(packstreet.pop(0))
                file.write("}")
                file.write("    \\end{minipage}}\n    &\n")
            else:
                file.write(
                    "\\mbox{\\begin{minipage}[t][6cm][t]{8cm}\n\\centering\n \\fontsize{40}{48} \\selectfont\n        \\phantom{ }\\\\\n        \\phantom{ }\n"
                )
                file.write(" ")
                file.write("\\newline ")
                file.write("\\maxsizebox{8cm}{!}{")
                file.write(packstreet.pop(0))
                file.write("}")
                file.write("\n\\end{minipage}}\\\\")
            if packstreet[0] != " ":
                file.write(
                    "\\fbox{\\begin{minipage}[t][6cm][t]{8cm}\n\\centering\n \\fontsize{40}{48} \\selectfont\n        \\phantom{ }\\\\\n        \\phantom{ }\n"
                )
                file.write(str(packstreet_number))
                file.write("\\newline ")
                file.write("\\maxsizebox{8cm}{!}{")
                file.write(packstreet.pop(0))
                file.write("}")
                file.write("\n\\end{minipage}}\\\\")
            else:
                file.write(
                    "\\mbox{\\begin{minipage}[t][6cm][t]{8cm}\n\\centering\n \\fontsize{40}{48} \\selectfont\n        \\phantom{ }\\\\\n        \\phantom{ }\n"
                )
                file.write(" ")
                file.write("\\newline ")
                file.write("\\maxsizebox{8cm}{!}{")
                file.write(packstreet.pop(0))
                file.write("}")
                file.write("\n\\end{minipage}}\\\\")

        file.write("\\end{tabular}\n\\end{table}\n\n\n")
file.write("\\end{document}")
