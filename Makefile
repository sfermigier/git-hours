test:
	echo "TODO"

clean:
	rm -rf dist

build:
	poerty build

upload: clean build
	twine upload dist/*

