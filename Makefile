.PHONY: help init test lint isort format
.DEFAULT: help

init:
	pip3 install -r requirements.txt


lint:
	flake8 --exclude=.tox --max-line-length=120 --statistics --count


isort:
	sh -c "isort --skip-glob=.tox --recursive . "


format: isort
	sh -c "autopep8 -i -r --max-line-length 120 . "


test:
	coverage run --source=tree,graph,heap,stack -m unittest discover -v


report: test
	coverage report --fail-under=50


htmlreport: test
	coverage html
	coverage report --fail-under=50
