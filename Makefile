PROJECT = xmas
ID = pikesley/${PROJECT}

all: build

build:
	docker build \
		--tag ${ID} .

run:
	docker run \
	--volume $(shell pwd)/${PROJECT}:/opt/${PROJECT} \
	--interactive \
	--tty \
	${ID}:latest \
	bash
