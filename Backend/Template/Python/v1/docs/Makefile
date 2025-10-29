# Minimal makefile for Sphinx documentation

SPHINXOPTS    ?=
SPHINXBUILD   ?= uv run sphinx-build
SPHINXAUTOBUILD     ?= uv run sphinx-autobuild
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Build and serve documentation with live reload
livehtml:
	@$(SPHINXAUTOBUILD) -b html $(SPHINXOPTS) "$(SOURCEDIR)" "$(BUILDDIR)/livehtml"

# Build and serve documentation with html output
html:
	@$(SPHINXBUILD) -b html $(SPHINXOPTS) "$(SOURCEDIR)" "$(BUILDDIR)/html"

# Clean build directory
clean:
	rm -rf $(BUILDDIR)/*

# Open HTML documentation in browser
open:
	open "$(BUILDDIR)/html/index.html"

# Build and open
build: html open

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
