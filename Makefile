install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	#force install latest whisper
	pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git
test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

format:	
	black *.py hugging-face/zero_shot_classification.py 

lint:
	# Use find to collect Python files recursively so Make's shell doesn't leave
	# glob patterns unexpanded when there are no matching files in the current
	# working directory.
	find . -name "*.py" \
		-not -path "./.git/*" \
		-not -path "./.venv/*" \
		-not -path "./venv/*" \
		-not -path "./__pycache__/*" | xargs pylint --disable=R,C --ignore-patterns=test_.*?py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

checkgpu:
	echo "Checking GPU for PyTorch"
	python utils/verify_pytorch.py
	echo "Checking GPU for Tensorflow"
	python utils/verify_tf.py

refactor: format lint

deploy:
	#echo #deploy goes here
		
all: install lint test format deploy
