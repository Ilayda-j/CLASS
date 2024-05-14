# Makefile

.PHONY: run-python run-command all

# This target runs a Python script named script.py
run-python:
	@python3 Apps/build_ui_scripts.py

# This target runs a generic command-line command, in this case, echo
run-command:
	@nbdev_prepare

# This target runs both the Python script and the command-line command
all: run-python run-command