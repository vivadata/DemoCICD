
lint :
	pylint --rcfile=pylint.rc src


test :
	PYTHONPATH=. pytest -v tests
