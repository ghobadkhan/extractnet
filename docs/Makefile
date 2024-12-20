# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS ?=
SPHINXBUILD ?= sphinx-build
SOURCEDIR = .
BUILDDIR = _build
TYPE ?= html

.PHONY: help build show sleep

build:
	@$(SPHINXBUILD) -M $(TYPE) "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

show:
	@google-chrome $(BUILDDIR)/$(TYPE)/index.html


sleep:
	@sleep 1

build-show: build sleep show

	
# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)