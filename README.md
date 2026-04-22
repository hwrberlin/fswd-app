# Contents of this repository

This repository complements the [online notebooks](https://hwrberlin.github.io/fswd/) to the Full-Stack Web Development course at HWR Berlin.

It contains (a) the recommended documentation structure and (b) the web app code as shown in the individual teaching sessions. Development happens on the `main` branch. Additional branches have been created at natural teaching points. You may think of those as progressing "releases" of the app: as the semester unfolds, more features will be built in, with the occasional refactoring here and there.

I recommend you `git switch` to the particular branch alongside a notebook:

+ `git switch docs`: basic structure for your own documentation
+ `git switch intro`: "[Intro to full-stack web development with Flask](https://hwrberlin.github.io/fswd/fswd-intro.html)"
+ `git switch flask`: "[Flask framework: URL path routing deep dive](https://hwrberlin.github.io/fswd/flask.html)"
+ `git switch html+css`: "[Introduction to HTML an CSS](https://hwrberlin.github.io/fswd/html-css.html)"
+ `git switch ui`: "[User interfaces with WTForms and Bootstrap](https://hwrberlin.github.io/fswd/user-interfaces.html)"
+ `git switch sqlalchemy`: "[Relational databases with Flask-SQLAlchemy](https://hwrberlin.github.io/fswd/sqlalchemy.html)"

> You can perform (and commit) your own local changes. When you `git switch` to another branch, these previous changes will stay on the branch where you made them. You don't have the rights to `git push` local commits to the remote repo - any change you introduce will stay local on your machine.
>
> If you try to `git switch` while you have uncommitted local changes, git will fail with an error. One option is to set aside local changes with `git stash` (not part of commit history), and pull them back in with `git stash pop` at a later point (e.g., after you have done `git switch` to another branch).
> 
> The last-resort "hard reset" command is `git reset --hard`: this is a destructive command, deleting any local changes you may have done. Be sure to preserve them at some other location if you need them later. But you will end up with a clean copy of the remote repository.

The recommended documentation structure lived in hte `📁/docs` folder, as a source to GitHub Pages. For setup instructions, see [this notebook](https://hwrberlin.github.io/fswd/git.html#5-github-pages).

# Setup steps to run the app

**Step 1:** Set up and activate a [Python Virtual Environment](https://hwrberlin.github.io/fswd/python-vscode.html#32-use-the-python-virtual-environment-as-default-for-this-workspace).

**Step 2:** Install the required Python packages from the terminal with the command `pip install -r requirements.txt`:

```console
(venv) C:\Users\me\projects\webapp> pip install -r requirements.txt
```

> I created the file `📄requirements.txt` with this command: `pip freeze > requirements.txt`
>
> You want to run this command every time you `git switch` to the next lesson - but this is also mentioned in the particular notebook.

**Step 3** *(optional at branch `sqlalchemy`)*: Initialize the app's SQLite database via `flask init-db`:

```console
(venv) PS C:\Users\me\projects\webapp> flask init-db
Database has been initialized.
```

**Step 4:** Start the web server via `flask run --reload`:

```console
(venv) PS C:\Users\me\projects\webapp> flask run --reload
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
```

**Step 5:** Visit [http://127.0.0.1:5000/insert/sample](http://127.0.0.1:5000/insert/sample) to populate the app's database with some sample data.

**Step 6:** Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to view the landing page

> For subsequent runs, you just need to run **Step 4** and **Step 6** (assuming the Python Virtual Environment has been activated.)