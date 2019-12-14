all: style test clean

travis: style test-no-cov

style:
	python -m pylama

test:
	python -m pytest --random-order --cov -vv -s

test-no-cov:
	python -m pytest --random-order -vv --exitfirst

install:
	python -m pip install -r requirements.txt

clean:
	@find . -depth -name __pycache__ -exec rm -fr {} \;
	@find . -depth -name .pytest_cache -exec rm -fr {} \;

systemd-install:
	sudo systemctl enable /home/pi/xmas/systemd/apiserver.service
	sudo systemctl enable /home/pi/xmas/systemd/chaser.service

stop-services:
	sudo service apiserver stop
	sudo service chaser stop

run-server:
	sudo uvicorn apiserver:app --host 0.0.0.0 --port 5000 --reload

push-code:
	rsync -av /opt/xmas pi@xmas.local:
