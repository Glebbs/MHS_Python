FROM python:3.10

RUN apt-get update && \
    apt-get install -y texlive-latex-base texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended

COPY ./img.png latex_generator/latex_generator.py latex_generator/setup.py latex_generator/use_latex_package.py /app/

RUN pip install /app

WORKDIR /app

CMD python use_latex_package.py && pdflatex example.tex
