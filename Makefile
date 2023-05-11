.ONESHELL:
SHELL = /bin/bash

.PHONY : all
## all: runs all targets except help
all : env html clean

.PHONY : env 
## env: creates and configures the environment
env :
    source /srv/conda/etc/profile.d/conda.sh
    conda env create -f environment.yml 
    conda activate final_proj
    conda install ipykernel
    python -m ipykernel install --user --name final_proj --display-name "IPython - final_proj"

## html: build the JupyterBook
.PHONY : html 
html: 
    jupyter-book build .
    
## - html-hub: build static website so it can be viewed on hosted JupyterHub (via URL proxy).
.PHONY: html-hub
html-hub: conf.py
    sphinx-build  . _build/html  -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
    @echo
    @echo "To start the Python http server, use:"
    @echo "cd _build/html"
    @echo "python -m http.server"
    @echo "and visit this link with your browser:"
    @echo "https://stat159.datahub.berkeley.edu/user-redirect/proxy/8000/index.html"
    
    
## clean: clean up files in "_build"  and "figures" folders
.PHONY : clean
clean: 
    rm -rf _build/*
##  rm -rf figures/*

## help: prints documentation
.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<