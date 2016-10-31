Getting Started
===============

You'll want to create a virtualenv.

    mkdir -p ~/venv/battleship
    virtualenv --no-site-packages ~/venv/battleship
    source ~/venv/battleship/bin/activate

Then you'll want to install the requirements.

    pip install -r requirements.txt

Now run the tests to ensure your environment is setup correctly.

    tox

