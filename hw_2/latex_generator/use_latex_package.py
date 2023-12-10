from latex_generator import latex_table, latex_image

data = [
    ["A", "B", "C"],
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

table_code = latex_table(data)
image_code = latex_image("img.png", "exampleLabel", "Example caption", 0.5)

latex_document = f"""
    \\documentclass{{article}}
    
    \\usepackage[english]{{babel}}
    
    \\usepackage[letterpaper,top=2cm,bottom=2cm,left=3cm,right=3cm,marginparwidth=1.75cm]{{geometry}}
    
    \\usepackage{{amsmath}}
    \\usepackage{{graphicx}}
    \\usepackage[colorlinks=true, allcolors=blue]{{hyperref}}
    
    \\title{{Your Paper}}
    \\author{{You}}
    
    \\begin{{document}}
    
    {table_code}
    
    {image_code}
    
    \\end{{document}}
"""

with open("example.tex", "w") as output_file:
    output_file.write(latex_document)
