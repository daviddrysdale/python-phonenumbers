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
GEODIR=$(PYDIR)/phonenumbers/geodata
$(GEODIR):
	mkdir $@
$(GEODIR)/__init__.py: $(GEODIR)/geodata.db
$(GEODIR)/geodata.db: buildprefixdata.py $(TOPDIR)/resources/geocoding | $(GEODIR)
	$(PYTHON) buildprefixdata.py --var GEOCODE --shelf $(GEODIR)/geodata.db $(TOPDIR)/resources/geocoding $(GEODIR)/__init__.py .
TESTGEODIR=$(PYDIR)/tests/testgeodata
$(TESTGEODIR):
	mkdir $@
$(TESTGEODIR)/__init__.py: $(TESTGEODIR)/geodata.db
$(TESTGEODIR)/geodata.db: buildprefixdata.py $(TOPDIR)/resources/test/geocoding | $(TESTGEODIR)
	$(PYTHON) buildprefixdata.py --var GEOCODE --shelf $(TESTGEODIR)/geodata.db $(TOPDIR)/resources/test/geocoding $(TESTGEODIR)/__init__.py phonenumbers
geodata: $(GEODIR)/__init__.py $(TESTGEODIR)/__init__.py

# Generate Python files from carrier data
CARRIERDIR=$(PYDIR)/phonenumbers/carrierdata
$(CARRIERDIR):
	mkdir $@
$(CARRIERDIR)/__init__.py: $(CARRIERDIR)/carrierdata.db
$(CARRIERDIR)/carrierdata.db: buildprefixdata.py $(TOPDIR)/resources/carrier | $(CARRIERDIR)
	$(PYTHON) buildprefixdata.py --var CARRIER --shelf $(CARRIERDIR)/carrierdata.db $(TOPDIR)/resources/carrier $(CARRIERDIR)/__init__.py .
TESTCARRIERDIR=$(PYDIR)/tests/testcarrierdata
$(TESTCARRIERDIR):
	mkdir $@
$(TESTCARRIERDIR)/__init__.py: $(TESTCARRIERDIR)/carrierdata.db
$(TESTCARRIERDIR)/carrierdata.db: buildprefixdata.py $(TOPDIR)/resources/test/carrier | $(TESTCARRIERDIR)
	$(PYTHON) buildprefixdata.py --var CARRIER --shelf $(TESTCARRIERDIR)/carrierdata.db $(TOPDIR)/resources/test/carrier $(TESTCARRIERDIR)/__init__.py phonenumbers
carrierdata: $(CARRIERDIR)/__init__.py $(TESTCARRIERDIR)/__init__.py

# Generate Python files from timezone data
TZDIR=$(PYDIR)/phonenumbers/tzdata
$(TZDIR):
	mkdir $@
$(TZDIR)/__init__.py: $(TZDIR)/tzdata.db
$(TZDIR)/tzdata.db: buildprefixdata.py $(TOPDIR)/resources/timezones/map_data.txt | $(TZDIR)
	$(PYTHON) buildprefixdata.py --var TIMEZONE --shelf $(TZDIR)/tzdata.db --flat --sep '&' $(TOPDIR)/resources/timezones/map_data.txt $(TZDIR)/__init__.py .
TESTTZDIR=$(PYDIR)/tests/testtzdata
$(TESTTZDIR):
	mkdir $@
$(TESTTZDIR)/__init__.py: $(TESTTZDIR)/tzdata.db
$(TESTTZDIR)/tzdata.db: buildprefixdata.py $(TOPDIR)/resources/test/timezones/map_data.txt | $(TESTTZDIR)
	$(PYTHON) buildprefixdata.py --var TIMEZONE --shelf $(TESTTZDIR)/tzdata.db --flat --sep '&' $(TOPDIR)/resources/test/timezones/map_data.txt $(TESTTZDIR)/__init__.py phonenumbers
tzdata: $(TZDIR)/__init__.py $(TESTTZDIR)/__init__.py

# Generate Python files from main metadata
$(PYDIR)/phonenumbers/data/__init__.py: $(TOPDIR)/resources/PhoneNumberMetadata.xml $(TOPDIR)/resources/PhoneNumberAlternateFormats.xml buildmetadatafromxml.py
	$(PYTHON) buildmetadatafromxml.py --alt $(TOPDIR)/resources/PhoneNumberAlternateFormats.xml $(TOPDIR)/resources/PhoneNumberMetadata.xml $(PYDIR)/phonenumbers/data .
$(PYDIR)/phonenumbers/shortdata/__init__.py: $(TOPDIR)/resources/ShortNumberMetadata.xml buildmetadatafromxml.py
	$(PYTHON) buildmetadatafromxml.py --short $(TOPDIR)/resources/ShortNumberMetadata.xml $(PYDIR)/phonenumbers/shortdata .
$(PYDIR)/tests/testdata/__init__.py:  $(TOPDIR)/resources/PhoneNumberMetadataForTesting.xml buildmetadatafromxml.py
	$(PYTHON) buildmetadatafromxml.py $(TOPDIR)/resources/PhoneNumberMetadataForTesting.xml $(PYDIR)/tests/testdata phonenumbers
metadata: $(PYDIR)/phonenumbers/data/__init__.py $(PYDIR)/phonenumbers/shortdata/__init__.py $(PYDIR)/tests/testdata/__init__.py geodata carrierdata tzdata

alldata: metadata geodata carrierdata tzdata locale

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

# Profile
profile: alldata $(PYDIR)/tests/testdata/__init__.py profile_clean profile_report
profile_clean:
	rm -f phonenumbers.pstats
phonenumbers.pstats:
	python -m cProfile -o phonenumbers.pstats $(PYDIR)/tests/testwrapper.py
profile_report: phonenumbers.pstats
	python -c "import pstats; p = pstats.Stats('phonenumbers.pstats');p.sort_stats('time').print_stats(50)" | grep -v "test.py" | grep -v testwrapper.py

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

clean: coverage_clean profile_clean
	rm -f *.pyc
	rm -rf __pycache__
	rm -f $(PYDIR)/MANIFEST $(PYDIR)/*.pyc
	rm -f $(PYDIR)/phonenumbers/*.pyc
	rm -f $(PYDIR)/phonenumbers/data/*.pyc
	rm -f $(PYDIR)/phonenumbers/shortdata/*.pyc
	rm -f $(PYDIR)/phonenumbers/geodata/*.pyc
	rm -f $(PYDIR)/phonenumbers/carrierdata/*.pyc
	rm -f $(PYDIR)/phonenumbers/tzdata/*.pyc
	rm -rf $(PYDIR)/phonenumbers/__pycache__
	rm -rf $(PYDIR)/phonenumbers/data/__pycache__
	rm -rf $(PYDIR)/phonenumbers/shortdata/__pycache__
	rm -rf $(PYDIR)/phonenumbers/geodata/__pycache__
	rm -rf $(PYDIR)/phonenumbers/carrierdata/__pycache__
	rm -rf $(PYDIR)/phonenumbers/tzdata/__pycache__
	rm -f $(PYDIR)/phonenumbers/*.py,cover $(PYDIR)/.coverage*
	rm -f $(PYDIR)/tests/*.pyc $(PYDIR)/tests/testdata/*.pyc $(PYDIR)/tests/testgeodata/*.pyc $(PYDIR)/tests/testcarrierdata/*.pyc
	rm -rf $(PYDIR)/tests/__pycache__ $(PYDIR)/tests/testdata/__pycache__ $(PYDIR)/tests/testgeodata/__pycache__ $(PYDIR)/tests/testcarrierdata/__pycache__
	rm -rf $(PYDIR)/build $(PYDIR)/deb_dist $(PYDIR)/dist

metaclean:
	rm -rf $(PYDIR)/phonenumbers/data $(PYDIR)/phonenumbers/shortdata $(PYDIR)/tests/testdata
	rm -rf $(PYDIR)/phonenumbers/geodata $(PYDIR)/tests/testgeodata
	rm -rf $(PYDIR)/phonenumbers/carrierdata $(PYDIR)/tests/testcarrierdata
	rm -rf $(PYDIR)/phonenumbers/tzdata $(PYDIR)/tests/testtzdata

distclean: clean metaclean
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
$(PYDIR)/phonenumbers/pb2/phonenumber_pb2.py: $(TOPDIR)/resources/phonenumber.proto
	protoc -I$(TOPDIR)/resources --python_out=$(PYDIR)/phonenumbers/pb2 $<
testpb2: pb2
	cd $(PYDIR) && $(PYTHON) -m testpb2
