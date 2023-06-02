.PHONY: venv clean

venv:
	# python3 -m venv venv
	# source ./venv/bin/activate
	pip install --upgrade pip
	pip install -r requirements.txt

run_server:
	python3 learn_dj/manage.py runserver


clean:
	# rm -rf venv
	rm -rf learn/sql/__pycache__  learn/sql/migrations/__pycache__