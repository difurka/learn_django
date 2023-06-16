.PHONY: venv clean run_server

all: run_server

venv:
	# python3 -m venv venv
	# source ./venv/bin/activate
	pip install --upgrade pip
	pip install -r requirements.txt

run_server:
	python3 calc/manage.py runserver


clean:
	# rm -rf venv
	rm -rf calc/calc/__pycache__ calc/calc_web/__pycache__  calc/calc_web/migrations/__pycache__