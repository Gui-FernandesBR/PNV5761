.PHONY: aulas modelagem1 black

aulas:
	pandoc aulas/index.rst \
		-V geometry:margin=1in \
		-V papersize=letter \
		-V indent=true \
		-V fontsize=12pt \
		--number-sections \
		-o aulas/index.pdf

modelagem1:
	pandoc listas/1_modelagem/1_em_aula/index.rst \
		-V geometry:margin=1in \
		-V papersize=letter \
		-V indent=true \
		-V fontsize=12pt \
		--number-sections \
		-o listas/1_modelagem/1_em_aula/index.pdf

black:
	black .
