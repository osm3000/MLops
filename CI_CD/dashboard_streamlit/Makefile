test:
	echo "NOT IMPLEMENTED"

format:
	black *.py

lint:
	pylint --disable=R,C main.py

run:
	# export ORG_NAME=org-ijMIbIDtPwDKB9zHhpAwPK64;\
	# export OPENAI_API_KEY=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;\
	streamlit run main.py --server.port=8501 --server.address=0.0.0.0
	# streamlit run main.py

requirements_update:
	pipreqs --force

install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

build_docker:
	docker build . -t streamlit_app_example

run_docker:
	docker container run -p 8501:8501 -d streamlit_app_example
# all: format lint set_env_vars run
all: format run
# all_docker: run
	