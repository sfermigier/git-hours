test:
	pytest

clean:
	rm -rf dist

build: clean
	poetry build

upload: build
	twine upload dist/*

format:
	black src tests
