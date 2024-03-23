#!/usr/bin/env bash
# Note: This file usually gets sourced.
if [[ -n $PYTHON_VENV_TEST_ROOT ]]; then
    echo "Script already sourced! Please open a new terminal."
    return 0
fi

PYTHON_VENV_TEST_ROOT=$(git rev-parse --show-toplevel)

# Create python virtual environment
python3 -m venv "$PYTHON_VENV_TEST_ROOT/.venv"

# Activate the environment
source "$PYTHON_VENV_TEST_ROOT/.venv/bin/activate"

# Install required packages
python3 -m pip install -r "$PYTHON_VENV_TEST_ROOT/requirements.txt"