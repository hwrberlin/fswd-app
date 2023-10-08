# Contents of this repository

This repository complements the [online notebooks](https://hwrberlin.github.io/fswd/) to the Full-Stack Web Development course at HWR Berlin.

The commit history on the `main` branch has been enriched with [tags](https://git-scm.com/book/en/v2/Git-Basics-Tagging) that match the individual notebooks. Think of these tags as progressing "releases" of the app: as the semester unfolds, more features will be built in, with the occasional refactoring here and there.

I recommend you `git checkout` the repository at the tagged location of a particular notebook:

+ `git checkout docs`: basic structure for your own documentation
+ `git checkout intro`: "[Intro to full-stack web development with Flask](https://hwrberlin.github.io/fswd/02-fswd-intro.html)"
+ *... more to come*

> By checking out a particular tag, git will throw you a "detached HEAD" warning. This is a feature not a bug :) Consult the [git manual](https://git-scm.com/book/en/v2/Git-Basics-Tagging) for how to work around this warning, if you are so inclined.
> 
> Alternatively, you may revert to the latest commit with `git reset --hard`: this is a destructive command, deleting any local changes you may have done. Be sure to preserve them at some other location if you need them later.

In addition to exemplary code, this repository contains a basic structure for your documentation page in the `📁/docs` folder, as a source to GitHub Pages. For setup instructions, see [this notebook](https://hwrberlin.github.io/fswd/04-git.html#5-github-pages).

# Steps to execute the app

**Step 1:** set up and activate a [Python Virtual Environment](https://hwrberlin.github.io/fswd/01-python-vscode.html#32-use-the-python-virtual-environment-as-default-for-this-workspace).

**Step 2:** install the required Python packages from the terminal with the command `pip install -r requirements.txt`:

```console
(venv) C:\Users\me\projects\webapp> pip install -r requirements.txt
```

> I created the file `📄requirements.txt` with this command: `pip freeze > requirements.txt`

**Step 3:** initialize the app's SQLite database via `flask init-db`:

```console
(venv) PS C:\Users\me\projects\webapp> flask init-db
Database has been initialized.
```

**Step 4:** start the web server via `flask run --reload`:

```console
(venv) PS C:\Users\me\projects\webapp> flask run --reload
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
```

**Step 5:** visit [http://127.0.0.1:5000/insert/sample](http://127.0.0.1:5000/insert/sample) to populate the app's database with some sample data.

**Step 6:** visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to view the landing page