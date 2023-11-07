TESTS = tests/*/*.py
MODULES = appli/modele/*.py appli/BD/*.py tests/*/*.py
MODULES_TESTED = appli/modele/*.py appli/BD/*.py


.PHONY: typehint
typehint:  
	mypy --ignore-missing-imports ${MODULES_TESTED}

.PHONY: tests
tests:  
	python3 -m unittest -v -b ${TESTS}

.PHONY: lint
lint:  
	pylint ${MODULES}

.PHONY: format
format:	
	yapf -ir ${MODULES}

.PHONY: coverage
coverage:
	python3 -m coverage run -m unittest -v -b ${TESTS}
	python3 -m coverage report -m ${MODULES_TESTED}

.PHONY: clean
clean:  
	find . -type f -name "*.pyc" | xargs rm -fr  
	find . -type d -name __pycache__ | xargs rm -fr
	find . -type d -name .mypy_cache | xargs rm -fr
	find . -type f -name .coverage | xargs rm -fr
	find . -type f -name .flaskenv | xargs rm -fr
	find . -type d -name .idea/ | xargs rm -fr

.PHONY: verif
verif: clean typehint lint coverage format clean
