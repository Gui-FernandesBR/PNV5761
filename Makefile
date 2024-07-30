pdf:
	pandoc listas\1_modelagem\1_em_aula\index.rst \
		-V geometry:margin=1in \
		-V papersize=letter \
		-V indent=true \
		-V fontsize=12pt \
		--number-sections \
		-o listas\1_modelagem\1_em_aula\index.pdf

other:
		-H ./docs/latex/preamble.tex \
		-V fontfamily=cmbright \


# TODO: ao final da disciplina, escrever um "bundle" com todas as listas
