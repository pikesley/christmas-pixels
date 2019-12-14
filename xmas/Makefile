all: style test clean

style:
	python -m pylama

test:
	python -m pytest --random-order --cov -vv -s --exitfirst

install:
	python -m pip install -r requirements.txt

clean:
	@find . -depth -name __pycache__ -exec rm -fr {} \;
	@find . -depth -name .pytest_cache -exec rm -fr {} \;

push-code:
	rsync -av /opt/xmas pi@xmas.local:
	scp /opt/xmas/Makefile.pi pi@xmas.local:xmas/Makefile

run-api:
	REDIS_HOST=redis uvicorn apiserver:APP --host 0.0.0.0 --port 5000 --reload

run-celery:
	REDIS_HOST=redis celery worker -A workers.light_worker --loglevel INFO

run-lamplighter:
	python scripts/lamplighter.py
