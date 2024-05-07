install:
	pip install -r requirements.txt

test:
	python -m pytest -vv test_hello.py

format:
	black *.py

lint:
	pylint --disable=R,C --disable=invalid-name hello.py

all:  
	install lint test
