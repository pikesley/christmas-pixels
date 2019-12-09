all: style test clean

style:
	python -m pylama

test:
	python -m pytest --random-order --cov -vv -s

test-style:
	python -m pylama

test-unit:
	python -m pytest --verbose --random-order -k unit_

test-system:
	python -m pytest --verbose --random-order -k system_

test-coverage:
	@python -m pytest -q --cov > /dev/null
	python -m coverage report

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
