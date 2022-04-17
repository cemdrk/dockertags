.PHONY: install uninstall format test


uninstall:
	pip uninstall -y dockertags

install: uninstall
	python setup.py install

format:
	isort src/
	black .

test:
	pytest -x -s . --pdb
