all: clean build

clean:
	rm -rf build dialogflowpy_webhook.egg-info dist
	echo Clean is done

build:
	python3 setup.py sdist bdist_wheel
	echo dialogflowpy_webhook module has been successfully built. It is available in the dist directory

testupload:
	python3 -m twine upload --repository testpypi dist/*

produpload:
	python3 -m twine upload dist/*