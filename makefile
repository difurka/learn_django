.PHONY: venv clean

venv:
	# python3 -m venv venv
	# source ./venv/bin/activate
	pip install --upgrade pip
	pip install -r requirements.txt

clean:
	rm -rf venv
	rm -rf learn_dj/learn_dj/__pycache__ learn_dj/main/__pycache__ learn_dj/main/migrations/__pycache__