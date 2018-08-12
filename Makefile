.PHONY: all help qa clean coverage run

# target: all - Default target. Does nothing.
all:
	@clear
	@echo "Hello $(LOGNAME), nothing to do by default"
	@echo "Try 'make help'"

# target: help - Display callable targets.
help:
	@clear
	@egrep "^# target:" [Mm]akefile

# target: qa - Run tests
qa:
	pytest

# target: clean - Delete pycache
clean:
	echo "### Cleaning *.pyc and .DS_Store files "
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '.DS_Store' -exec rm -f {} \;
	find . -name "__pycache__" -type d -exec rm -rf {} +

# target: coverage - Test coverage
coverage:
	py.test --cov=.

# target: run - Run skeleton with uwsgi
run:
	uwsgi --http :9090 --touch-reload settings.py --touch-reload views.py --touch-reload templates/* --wsgi-file start.py --honour-stdin --check-static .
