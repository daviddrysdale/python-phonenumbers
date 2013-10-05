PYTHON=python
PACKAGE=phonenumbers
TOPDIR=../..
PYDIR=$(TOPDIR)/python

all: alldata

# Dump the JRE's Locale information
DumpLocale.class: DumpLocale.java
	javac $<
$(PYDIR)/phonenumbers/geodata/locale.py: DumpLocale.class | $(PYDIR)/phonenumbers/geodata
	java DumpLocale > $@
locale: $(PYDIR)/phonenumbers/geodata/locale.py

# Generate Python files from geocoding data
$(PYDIR)/phonenumbers/geodata:
	mkdir $@
$(PYDIR)/phonenumbers/geodata/__init__.py: buildprefixdata.py $(TOPDIR)/resources/geocoding | $(PYDIR)/phonenumbers/geodata
	$(PYTHON) buildprefixdata.py --var GEOCODE $(TOPDIR)/resources/geocoding $@
$(PYDIR)/tests/testgeodata:
	mkdir $@
$(PYDIR)/tests/testgeodata/__init__.py: buildprefixdata.py $(TOPDIR)/resources/test/geocoding | $(PYDIR)/tests/testgeodata
	$(PYTHON) buildprefixdata.py --var GEOCODE $(TOPDIR)/resources/test/geocoding $@
geodata: $(PYDIR)/phonenumbers/geodata/__init__.py $(PYDIR)/tests/testgeodata/__init__.py

# Generate Python files from carrier data
$(PYDIR)/phonenumbers/carrierdata:
	mkdir $@
$(PYDIR)/phonenumbers/carrierdata/__init__.py: buildprefixdata.py $(TOPDIR)/resources/carrier | $(PYDIR)/phonenumbers/carrierdata
	$(PYTHON) buildprefixdata.py --var CARRIER $(TOPDIR)/resources/carrier $@
$(PYDIR)/tests/testcarrierdata:
	mkdir $@
$(PYDIR)/tests/testcarrierdata/__init__.py: buildprefixdata.py $(TOPDIR)/resources/test/carrier | $(PYDIR)/tests/testcarrierdata
	$(PYTHON) buildprefixdata.py --var CARRIER $(TOPDIR)/resources/test/carrier $@
carrierdata: $(PYDIR)/phonenumbers/carrierdata/__init__.py $(PYDIR)/tests/testcarrierdata/__init__.py

# Generate Python files from metadata
$(PYDIR)/phonenumbers/data/__init__.py: $(TOPDIR)/resources/PhoneNumberMetadata.xml $(TOPDIR)/resources/PhoneNumberAlternateFormats.xml buildmetadatafromxml.py
	$(PYTHON) buildmetadatafromxml.py --alt $(TOPDIR)/resources/PhoneNumberAlternateFormats.xml $(TOPDIR)/resources/PhoneNumberMetadata.xml $(PYDIR)/phonenumbers/data .
$(PYDIR)/phonenumbers/shortdata/__init__.py: $(TOPDIR)/resources/ShortNumberMetadata.xml buildmetadatafromxml.py
	$(PYTHON) buildmetadatafromxml.py --short $(TOPDIR)/resources/ShortNumberMetadata.xml $(PYDIR)/phonenumbers/shortdata .
$(PYDIR)/tests/testdata/__init__.py:  $(TOPDIR)/resources/PhoneNumberMetadataForTesting.xml buildmetadatafromxml.py
	$(PYTHON) buildmetadatafromxml.py $(TOPDIR)/resources/PhoneNumberMetadataForTesting.xml $(PYDIR)/tests/testdata phonenumbers
metadata: $(PYDIR)/phonenumbers/data/__init__.py $(PYDIR)/phonenumbers/shortdata/__init__.py $(PYDIR)/tests/testdata/__init__.py geodata carrierdata

alldata: metadata geodata carrierdata locale

test: alldata
	cd $(PYDIR) && $(PYTHON) -m testwrapper

# Coverage; requires coverage module
COVERAGE=$(shell hash python-coverage 2>&- && echo python-coverage || echo coverage)
COVERAGE_FILES=$(subst $(PYDIR),.,$(wildcard $(PYDIR)/phonenumbers/*.py))
coverage: alldata $(PYDIR)/tests/testdata/__init__.py coverage_clean coverage_generate coverage_report
coverage_clean:
	cd $(PYDIR) && $(COVERAGE) -e
coverage_generate:
	cd $(PYDIR) && $(COVERAGE) -x testwrapper.py
coverage_report:
	cd $(PYDIR) && $(COVERAGE) -m -r $(COVERAGE_FILES)
coverage_annotate:
	cd $(PYDIR) && $(COVERAGE) annotate $(COVERAGE_FILES)

# Packaging
VERSION=$(shell grep __version__ $(PYDIR)/phonenumbers/__init__.py | sed 's/__version__ = "\(.*\)"/\1/')
TARBALL_LOCAL=dist/$(PACKAGE)-$(VERSION).tar.gz
TARBALL=$(PYDIR)/$(TARBALL_LOCAL)
# Build setuptools packaged tarball $(TARBALL)
sdist: alldata
	cd $(PYDIR) && $(PYTHON) setup.py sdist
$(TARBALL): sdist

install: alldata
	cd $(PYDIR) && $(PYTHON) setup.py build
	cd $(PYDIR) && sudo $(PYTHON) setup.py install

clean:
	rm -f *.pyc
	rm -f $(PYDIR)/MANIFEST $(PYDIR)/*.pyc
	rm -f $(PYDIR)/phonenumbers/*.pyc $(PYDIR)/phonenumbers/data/*.pyc $(PYDIR)/phonenumbers/geodata/*.pyc $(PYDIR)/phonenumbers/carrierdata/*.pyc
	rm -f $(PYDIR)/phonenumbers/*.py,cover $(PYDIR)/.coverage*
	rm -f $(PYDIR)/tests/*.pyc $(PYDIR)/tests/testdata/*.pyc $(PYDIR)/tests/testgeodata/*.pyc $(PYDIR)/tests/testcarrierdata/*.pyc
	rm -rf $(PYDIR)/build $(PYDIR)/deb_dist $(PYDIR)/dist

metaclean:
	rm -rf $(PYDIR)/phonenumbers/data $(PYDIR)/phonenumbers/shortdata $(PYDIR)/tests/testdata
	rm -rf $(PYDIR)/phonenumbers/geodata $(PYDIR)/tests/testgeodata
	rm -rf $(PYDIR)/phonenumbers/carrierdata $(PYDIR)/tests/testcarrierdata

distclean: clean metaclean distclean3
	rm -rf $(PYDIR)/$(PACKAGE).egg-info
	rm -rf $(PYDIR)/build
	rm -f $(PYDIR)/DumpLocale.class

# Create Debian package.  Requires py2dsc, included in the python-stdeb package.
DEB_PACKAGE=python-$(PACKAGE)
DEB_VERSION=$(VERSION)-1_all
deb: $(PYDIR)/deb_dist/$(DEB_PACKAGE)_$(DEB_VERSION).deb

$(PYDIR)/deb_dist/$(DEB_PACKAGE)_$(VERSION)-1_all.deb: $(TARBALL)
	cd $(PYDIR) && py2dsc $(TARBALL_LOCAL)
	cd $(PYDIR)/deb_dist/$(PACKAGE)-$(VERSION) && dpkg-buildpackage -us -uc -nc

#####################################################################################################
# Protobuf interface.  Requires local installation of protobuf compiler and Python package (google.protobuf)
pb2: $(PYDIR)/phonenumbers/pb2/phonenumber_pb2.py
$(PYDIR)/pb2/phonenumber_pb2.py: $(TOPDIR)/resources/phonenumber.proto
	protoc -I$(TOPDIR)/resources --python_out=$(PYDIR)/phonenumbers/pb2 $<
testpb2: pb2
	cd $(PYDIR) && $(PYTHON) -m testpb2

#####################################################################################################
# Python3 generation
PYTHON3=python3
PY3PACKAGE=phonenumbers3k
PY3DIR=$(TOPDIR)/python3
PYSRC=$(wildcard $(PYDIR)/*.py) $(wildcard $(PYDIR)/tests/*.py) $(wildcard $(PYDIR)/phonenumbers/*.py)
PY3SRC=$(subst $(PYDIR),$(PY3DIR),$(PYSRC))
python3: $(PY3SRC) all3data

$(PY3DIR):
	mkdir $@
$(PY3DIR)/phonenumbers: | $(PY3DIR)
	mkdir $@
$(PY3DIR)/phonenumbers/geodata: | $(PY3DIR)/phonenumbers
	mkdir $@
$(PY3DIR)/phonenumbers/carrierdata: | $(PY3DIR)/phonenumbers
	mkdir $@
$(PY3DIR)/tests: | $(PY3DIR)
	mkdir $@
$(PY3DIR)/tests/testgeodata:
	mkdir $@
$(PY3DIR)/tests/testcarrierdata:
	mkdir $@

# Always convert as a batch
$(PY3DIR)/phonenumbers/%.py: $(PYDIR)/phonenumbers/%.py | $(PY3DIR)/phonenumbers
	cp $(PYDIR)/phonenumbers/*.py $(PY3DIR)/phonenumbers
	2to3 --write --nobackups $(PY3DIR)/phonenumbers/*.py > /dev/null 2>&1
	2to3 --write --doctests_only --nobackups $(PY3DIR)/phonenumbers/*.py > /dev/null 2>&1
$(PY3DIR)/tests/%.py: $(PYDIR)/tests/%.py | $(PY3DIR)/tests
	cp $(PYDIR)/tests/*.py $(PY3DIR)/tests
	2to3 --write --nobackups $(PY3DIR)/tests/*.py > /dev/null 2>&1
$(PY3DIR)/%.py: $(PYDIR)/%.py | $(PY3DIR)
	cp $< $@
	2to3 --write --nobackups $@ > /dev/null 2>&1

# Python3 generation of .py files
$(PY3DIR)/phonenumbers/geodata/locale.py: DumpLocale.class | $(PY3DIR)/phonenumbers/geodata
	java DumpLocale -python3 > $@
locale3: $(PY3DIR)/phonenumbers/geodata/locale.py
$(PY3DIR)/phonenumbers/geodata/__init__.py: buildprefixdata.py $(TOPDIR)/resources/geocoding | $(PY3DIR)/phonenumbers/geodata
	$(PYTHON3) buildprefixdata.py --var GEOCODE $(TOPDIR)/resources/geocoding $@
$(PY3DIR)/tests/testgeodata/__init__.py: buildprefixdata.py $(TOPDIR)/resources/test/geocoding | $(PY3DIR)/tests/testgeodata
	$(PYTHON3) buildprefixdata.py --var GEOCODE $(TOPDIR)/resources/test/geocoding $@
geo3data: $(PY3DIR)/phonenumbers/geodata/__init__.py $(PY3DIR)/tests/testgeodata/__init__.py
$(PY3DIR)/phonenumbers/carrierdata/__init__.py: buildprefixdata.py $(TOPDIR)/resources/carrier | $(PY3DIR)/phonenumbers/carrierdata
	$(PYTHON3) buildprefixdata.py --var CARRIER $(TOPDIR)/resources/carrier $@
$(PY3DIR)/tests/testcarrierdata/__init__.py: buildprefixdata.py $(TOPDIR)/resources/test/carrier | $(PY3DIR)/tests/testcarrierdata
	$(PYTHON3) buildprefixdata.py --var CARRIER $(TOPDIR)/resources/test/carrier $@
carrier3data: $(PY3DIR)/phonenumbers/carrierdata/__init__.py $(PY3DIR)/tests/testcarrierdata/__init__.py

$(PY3DIR)/phonenumbers/data/__init__.py: $(TOPDIR)/resources/PhoneNumberMetadata.xml $(TOPDIR)/resources/PhoneNumberAlternateFormats.xml buildmetadatafromxml.py
	$(PYTHON3) buildmetadatafromxml.py --alt $(TOPDIR)/resources/PhoneNumberAlternateFormats.xml $(TOPDIR)/resources/PhoneNumberMetadata.xml $(PY3DIR)/phonenumbers/data .
$(PY3DIR)/phonenumbers/shortdata/__init__.py: $(TOPDIR)/resources/ShortNumberMetadata.xml buildmetadatafromxml.py
	$(PYTHON3) buildmetadatafromxml.py --short $(TOPDIR)/resources/ShortNumberMetadata.xml $(PY3DIR)/phonenumbers/shortdata .
$(PY3DIR)/tests/testdata/__init__.py:  $(TOPDIR)/resources/PhoneNumberMetadataForTesting.xml buildmetadatafromxml.py
	$(PYTHON3) buildmetadatafromxml.py $(TOPDIR)/resources/PhoneNumberMetadataForTesting.xml $(PY3DIR)/tests/testdata phonenumbers
meta3data: $(PY3DIR)/phonenumbers/data/__init__.py $(PY3DIR)/phonenumbers/shortdata/__init__.py $(PY3DIR)/tests/testdata/__init__.py geo3data carrier3data

all3data: meta3data geo3data carrier3data locale3

test3: python3 all3data
	cd $(PY3DIR) && $(PYTHON3) -m testwrapper

# Packaging
TARBALL3=$(PY3DIR)/dist/$(PY3PACKAGE)-$(VERSION).tar.gz
# Build setuptools packaged tarball $(TARBALL)
sdist3: all3data
	cd $(PY3DIR) && $(PYTHON3) setup.py sdist
$(TARBALL3): sdist3

clean3:
	rm -rf $(PY3DIR)/MANIFEST $(PY3DIR)/__pycache__
	rm -rf $(PY3DIR)/phonenumbers/__pycache__ $(PY3DIR)/phonenumbers/data/__pycache__ $(PY3DIR)/phonenumbers/geodata/__pycache__ $(PY3DIR)/phonenumbers/carrierdata/__pycache__
	rm -rf $(PY3DIR)/tests/__pycache__ $(PY3DIR)/tests/testdata/__pycache__ $(PY3DIR)/tests/testgeodata/__pycache__ $(PY3DIR)/tests/testgeodata/__pycache__
	rm -rf $(PY3DIR)/build $(PY3DIR)/deb_dist $(PY3DIR)/dist

metaclean3:
	rm -rf $(PY3DIR)/phonenumbers/data $(PY3DIR)/phonenumbers/shortdata $(PY3DIR)/tests/testdata
	rm -rf $(PY3DIR)/phonenumbers/geodata $(PY3DIR)/tests/testgeodata
	rm -rf $(PY3DIR)/phonenumbers/carrierdata $(PY3DIR)/tests/testcarrierdata

distclean3: clean3 metaclean3
	rm -rf $(PY3DIR)

