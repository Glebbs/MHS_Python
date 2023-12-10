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


print(latex_image("img.png", "exampleLabel", "Example caption", 0.5))
