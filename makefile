all:
	gcc -fPIC -shared -o module.so module.c
	python module.py
