
# LaTeX Makefile
ALLFILES = ./thesis.tex\
		  Chapters/* \
		  Images/* \
		  Additional_files/* \
		  *.bib
MAINFILE = ./thesis

all: $(MAINFILE).pdf

.PHONY: clean

clean:
	rm -rf *.blg 
	rm -rf *.out 
	rm -rf *.bbl 
	rm -rf *.log
	rm -rf *.ind
	rm -rf *.ilg
	rm -rf *.lot
	rm -rf *.lof
	rm -rf *.ind
	rm -rf *.idx
	rm -rf *.aux
	rm -rf *.toc
	rm -rf *.pdf

thesis.pdf: $(FILES)
	pdflatex  $(MAINFILE).tex &> /dev/null
	pdflatex  $(MAINFILE).tex &> /dev/null
	bibtex $(MAINFILE) &> /dev/null
	pdflatex  $(MAINFILE).tex &> /dev/null
	pdflatex  $(MAINFILE).tex &> /dev/null

