test:
	echo "TODO"

clean:
	rm -rf dist

build: clean
	poetry build

upload: build
	twine upload dist/*

