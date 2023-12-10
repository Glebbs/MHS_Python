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


data = [
    ["A", "B", "C"],
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(latex_table(data))
