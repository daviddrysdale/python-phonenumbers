
phonenumbers/data/__init__.py: ../resources/PhoneNumberMetaData.xml buildmetadatafromxml.py
	python buildmetadatafromxml.py ../resources/PhoneNumberMetaData.xml phonenumbers/data

metadata: phonenumbers/data/__init__.py tests/testdata/__init__.py

tests/testdata/__init__.py:  ../resources/PhoneNumberMetaDataForTesting.xml buildmetadatafromxml.py
	python buildmetadatafromxml.py ../resources/PhoneNumberMetaDataForTesting.xml tests/testdata

test: tests/testdata/__init__.py
	python phonenumbers/__init__.py
	python phonenumbers/re_util.py
	python phonenumbers/unicode_util.py
	python tests/__init__.py

# Coverage; requires coverage module
COVERAGE_FILES=phonenumbers/*.py
coverage: coverage_clean coverage_generate coverage_report
coverage_clean:
	coverage -e
coverage_generate:
	coverage -x phonenumbers/re_util.py
	coverage -x phonenumbers/unicode_util.py
	coverage -x tests/__init__.py
coverage_report:
	coverage -m -r $(COVERAGE_FILES)
coverage_annotate:
	coverage annotate $(COVERAGE_FILES)

VERSION=$(shell grep __version__ phonenumbers/__init__.py | sed 's/__version__ = "\(.*\)"/\1/')
TARBALL=dist/phonenumbers-$(VERSION).tar.gz
# Build setuptools packaged tarball $(TARBALL)
sdist: 
	python setup.py sdist
$(TARBALL): sdist

install: sdist
	sudo python setup.py install

clean:
	rm -f MANIFEST *.pyc phonenumbers/*.pyc phonenumbers/data/*.pyc tests/*.pyc
	rm -rf build deb_dist dist

distclean:
	rm -rf phonenumbers/data tests/testdata

# Create Debian package.  Requires py2dsc, included in the python-stdeb package.
DEB_VERSION=$(VERSION)-1_all
deb: deb_dist/python-phonenumbers_$(DEB_VERSION).deb

deb_dist/python-phonenumbers_$(VERSION)-1_all.deb: $(TARBALL)
	py2dsc $(TARBALL)
	cd deb_dist/phonenumbers-$(VERSION) && dpkg-buildpackage -us -uc -nc