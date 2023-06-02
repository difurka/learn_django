.PHONY: venv clean

all: run_server

venv:
	# python3 -m venv venv
	# source ./venv/bin/activate
	pip install --upgrade pip
	pip install -r ../requirements.txt

run_server:
	python3 manage.py runserver


clean:
	# rm -rf venv
	rm -rf learn/__pycache__ /main/__pycache__ /main/migrations/__pycache__