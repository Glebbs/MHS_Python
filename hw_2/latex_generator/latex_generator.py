def latex_table(data):
    if not data or len(data) == 0:
        return ""

    num_columns = len(data[0])

    result = "\\begin{tabular}{" + "|".join(["c" for _ in range(num_columns)]) + "}\n"

    for i, row in enumerate(data):
        result += " & ".join(map(str, row)) + "\\\\\n"
        if i == len(data) - 1:
            continue
        result += "\\hline\n"

    result += "\\end{tabular}"
    return result


def latex_image(file_path, label=None, caption=None, width=None):
    result = "\\begin{figure}[ht]\\centering\n"
    if width is not None:
        result += "\\includegraphics[width=" + str(width) + "\\textwidth]{" + file_path + "}\n"
    else:
        result += "\\includegraphics{" + file_path + "}\n"
    if label is not None:
        result += "\\label{" + label + "}\n"
    if caption is not None:
        result += "\\caption{" + caption + "}\n"
    result += "\\end{figure}"
    return result
