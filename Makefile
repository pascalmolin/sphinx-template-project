# CONDA SETUP
# see https://stackoverflow.com/questions/60115420/check-for-existing-conda-environment-in-makefile
#
CONDA_ENV_NAME:=mysphinx
ifeq (,$(shell which conda))
	HAS_CONDA=False
else
	HAS_CONDA=True
	ENV_DIR=$(shell conda info --base)
	MY_ENV_DIR=$(ENV_DIR)/envs/$(CONDA_ENV_NAME)
	CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate
endif
# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= $(CONDA_ACTIVATE) $(CONDA_ENV_NAME) && sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile environment
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


environment:
ifeq (True,$(HAS_CONDA))
ifneq ("$(wildcard $(MY_ENV_DIR))","") # check if the directory is there
	@echo ">>> Found $(CONDA_ENV_NAME) environment in $(MY_ENV_DIR). Skipping installation..."
else
	@echo ">>> Detected conda, but $(CONDA_ENV_NAME) is missing in $(ENV_DIR). Installing ..."
	conda env create -f environment.yml -n $(CONDA_ENV_NAME)
endif
else
	@echo ">>> Install conda first."
	exit
endif

clean-conda:
ifeq (True,$(HAS_CONDA))
ifneq ("$(wildcard $(MY_ENV_DIR))","") # check if the directory is there
	conda env remove --name $(CONDA_ENV_NAME)
endif
endif
