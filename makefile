.PHONY: html
html:
	doxygen doc/doxygen.dox

.PHONY: clean
clean:
	rm -rf doc/_output