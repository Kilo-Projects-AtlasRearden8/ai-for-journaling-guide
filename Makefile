.PHONY: build clean test serve

PYTHON := python3

build:
	$(PYTHON) build.py

clean:
	rm -rf site/

test:
	$(PYTHON) -c "import build; build.run_tests()"

serve:
	$(PYTHON) -m http.server 8000 --directory site/
