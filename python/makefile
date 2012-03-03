PYTHON=python
PACKAGE=phonenumbers
alldata: metadata geodata locale

# Dump the JRE's Locale information
DumpLocale.class: DumpLocale.java
	javac $<

phonenumbers/geodata/locale.py: DumpLocale.class
	java DumpLocale > $@

locale: phonenumbers/geodata/locale.py

phonenumbers/geodata/__init__.py: buildgeocodingdata.py ../resources/geocoding
	$(PYTHON) buildgeocodingdata.py ../resources/geocoding $@

tests/testgeodata/__init__.py: buildgeocodingdata.py ../resources/test/geocoding
	$(PYTHON) buildgeocodingdata.py ../resources/test/geocoding $@

geodata: phonenumbers/geodata/__init__.py tests/testgeodata/__init__.py

phonenumbers/data/__init__.py: ../resources/PhoneNumberMetaData.xml buildmetadatafromxml.py
	$(PYTHON) buildmetadatafromxml.py ../resources/PhoneNumberMetaData.xml phonenumbers/data .

metadata: phonenumbers/data/__init__.py tests/testdata/__init__.py geodata

tests/testdata/__init__.py:  ../resources/PhoneNumberMetaDataForTesting.xml buildmetadatafromxml.py
	$(PYTHON) buildmetadatafromxml.py ../resources/PhoneNumberMetaDataForTesting.xml tests/testdata phonenumbers

test: alldata tests/testdata/__init__.py
	$(PYTHON) -m testwrapper

# Coverage; requires coverage module
COVERAGE=$(shell hash python-coverage 2>&- && echo python-coverage || echo coverage)
COVERAGE_FILES=phonenumbers/*.py
coverage: alldata tests/testdata/__init__.py coverage_clean coverage_generate coverage_report
coverage_clean:
	$(COVERAGE) -e
coverage_generate:
	$(COVERAGE) -x testwrapper.py
coverage_report:
	$(COVERAGE) -m -r $(COVERAGE_FILES)
coverage_annotate:
	$(COVERAGE) annotate $(COVERAGE_FILES)

VERSION=$(shell grep __version__ phonenumbers/__init__.py | sed 's/__version__ = "\(.*\)"/\1/')
TARBALL=dist/$(PACKAGE)-$(VERSION).tar.gz
# Build setuptools packaged tarball $(TARBALL)
sdist: alldata
	$(PYTHON) setup.py sdist
$(TARBALL): sdist

install: alldata
	$(PYTHON) setup.py build
	sudo $(PYTHON) setup.py install

clean:
	rm -f MANIFEST *.pyc phonenumbers/*.pyc phonenumbers/data/*.pyc phonenumbers/geodata/*.pyc
	rm -rf phonenumbers/__pycache__ phonenumbers/data/__pycache__ phonenumbers/geodata/__pycache__
	rm -f phonenumbers/*.py,cover .coverage*
	rm -f tests/*.pyc tests/testdata/*.pyc tests/testgeodata/*.pyc
	rm -rf build deb_dist dist

distclean: clean
	rm -rf phonenumbers/data tests/testdata
	rm -rf $(PACKAGE).egg-info
	rm -rf build
	rm -f DumpLocale.class

# Create Debian package.  Requires py2dsc, included in the python-stdeb package.
DEB_PACKAGE=python-$(PACKAGE)
DEB_VERSION=$(VERSION)-1_all
deb: deb_dist/$(DEB_PACKAGE)_$(DEB_VERSION).deb

deb_dist/$(DEB_PACKAGE)_$(VERSION)-1_all.deb: $(TARBALL)
	py2dsc $(TARBALL)
	cd deb_dist/$(PACKAGE)-$(VERSION) && dpkg-buildpackage -us -uc -nc
