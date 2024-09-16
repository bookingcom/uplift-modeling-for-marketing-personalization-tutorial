.PHONY: help publish

help: # Show help for each of the Makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

publish-ghp: # Publish the jupyter book tutorial to GitHub pages.
	pip install jupyter-book
	pip install ghp-import
	pip install -r tutorial/requirements-local.txt
	jupyter-book build --all tutorial
	ghp-import -n -p -f tutorial/_build/html
