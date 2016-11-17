Getting Started as a Contributor
================================

First create a virtualenv.

    mkdir -p ~/venv/battleship
    virtualenv --no-site-packages ~/venv/battleship
    source ~/venv/battleship/bin/activate

Then fetch the code and install the requirements.

    git clone https://github.com/JessaWitzel/battleship.git
    cd battleship
    pip install -r requirements.txt

Now run the tests to ensure your environment is setup correctly.

    tox

