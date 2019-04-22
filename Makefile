directory = venv

force_venv: | $(directory)
	@echo "will run no matter what"
	rm -rf ./venv
	virtualenv -p python3 $(directory)
	source ./$(directory)/bin/activate; \
	pip install -r requirements.txt; \

venv:
$(directory): 
	@virtualenv -p python3 $(directory)
	@source ./$(directory)/bin/activate; \
	if [ -a requirements.txt ] ; \
	then \
     @pip install -r requirements.txt ; \
	fi;


test_all:
	python -m unittest tests/*.py

