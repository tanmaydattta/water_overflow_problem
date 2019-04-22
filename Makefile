directory = venv

force_venv: | $(directory)
	@echo "will run no matter what"
	rm -rf ./venv
	virtualenv -p python3 $(directory)
	source ./$(directory)/bin/activate; \
	pip install -r requirements.txt; \

$(directory): 
	virtualenv -p python3 $(directory)
	source ./$(directory)/bin/activate; \
	pip install -r requirements.txt; \

test_all:
	python -m unitttest tests/*

