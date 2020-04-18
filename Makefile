# Project Makefile

.DEFAULT_GOAL := all
C_NAME = obtx
IMG_NAME = 'pipe-obtx:0.1'
VOL_NAME = 'pipeline'

install:
	pip3 install -r requirements.txt

run:
	python3 example.py