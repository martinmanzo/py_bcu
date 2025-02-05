build: # Builds the lib.
	python setup.py sdist

publish: # Builds and publish to PyPi.
	$(MAKE) build
	twine upload dist/*

test:
	pytest
