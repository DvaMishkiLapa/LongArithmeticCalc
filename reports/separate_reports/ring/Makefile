SHELL=/bin/bash

STUDENT = А.А. Уткин
DEGREE = к.ф.-м.н.
DIRECTOR = М.Г. Завгородний
SED = "s/{{student}}/${STUDENT}/; s/{{degree}}/${DEGREE}/; s/{{director}}/${DIRECTOR}/"
file = report.tex

all: titlepage
	pdflatex $(file)
	pdflatex $(file)
	biber report
	pdflatex $(file)
	pdflatex $(file)

pdflatex:
	@pdflatex $(file)

titlepage:
	@sed -e ${SED} titlepage.fodt > tp-output.fodt
	libreoffice --headless --convert-to pdf tp-output.fodt

overfull:
	@pdflatex $(file) | grep -va Underfull | grep  -a . | grep -aC 12 Overfull
	@pdflatex $(file) | grep -c Overfull

clean:
	rm -f ./grap/*.pdf
	rm -f *.aux *.bbl *.bcf *.blg *.log *out *.run.xml *.toc
