#!/usr/bin/env zsh

echo "Updating dependencies\n"
echo "Activating virtual environment\n"
source .venv/bin/activate

echo "\npip-compile --generate-hashes --strip-extras requirements-dev.in\n"
pip-compile --generate-hashes --strip-extras requirements-dev.in
if [ $? -ne 0 ]; then
    echo "\nError: Failed to compile requirements-dev.in\n"
    deactivate
    exit 1
fi

echo "\npip-compile --allow-unsafe --generate-hashes --strip-extras\n"
pip-compile --generate-hashes --strip-extras
if [ $? -ne 0 ]; then
    echo "\nError: Failed to compile requirements.in\n"
    deactivate
    exit 1
fi

echo "\npip-sync requirements-dev.txt requirements.txt\n"
pip-sync requirements-dev.txt requirements.txt
if [ $? -ne 0 ]; then
    echo "\nError: Failed to sync requirements-dev.txt and requirements.txt\n"
    deactivate
    exit 1
fi

echo "\nValidate the requirements files:"
echo "- The command 'pip-sync' will have already installed the dependencies."
echo "- The command 'pip instasll' will complain if the generated requirements are invalid!"
echo "\npip install -r requirements-dev.txt -r requirements.txt\n"
pip install -r requirements-dev.txt -r requirements.txt
if [ $? -ne 0 ]; then
    echo "\nError: Invalid requirements\n"
    deactivate
    exit 1
fi

echo "\nDeactivating virtual environment\n"
deactivate
