.PHONY: install uninstall


uninstall:
	pip uninstall dockertags

install: uninstall
	python setup.py install

format:
	black .

test:
	pytest -x -s . --pdb
