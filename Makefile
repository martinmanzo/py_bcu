build: # Builds the lib.
	python setup.py sdist

publish: # Builds and publish to PyPi.
	$(MAKE) build
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*
	twine upload dist/*
