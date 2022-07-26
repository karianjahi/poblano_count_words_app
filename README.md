# poblano_count_words_app
This app counts the number of words in a sentence (or text)

You must install `pytest`, `pytest-cov` and `coverage` using `pip install`

To test the code just type: `pytest`

To measure coverage type: `pytest --cov`

To output coverage into a html `coverage html`

The immediate command above creates a folder known as `htmlcov`. Inside this folder exists the file `index.html`

You can then open the above html file using a browser of your choice e.g. `firefox htmlcov/index.html`


# Make the app pip-installable
- Traditionally, to access the python scripts from outside the App, we usually add a file called `__init__.py`. This file makes our app a package.

- To make our `poblano...app` pip installable, we do the following:
	- create `__init__.py` file
	- move all tests to their own folder called `tests`
	- to make sure that the tests will run, we need to add an empty file known as `__init__.py` in the tests folder
	- We now need to move the main script file to a folder of the same name as the project folder (not because it is a must that they should have the same name but it is a tradition)
	- We need to create another `__init__.py` file inside the newly created folder above
	- Add a file called `setup.py`. This is the file that renders our app (package) pip-installable.
