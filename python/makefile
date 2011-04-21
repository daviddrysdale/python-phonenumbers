
phonenumbers/data/__init__.py: ../resources/PhoneNumberMetaData.xml buildmetadatafromxml.py
	python buildmetadatafromxml.py ../resources/PhoneNumberMetaData.xml phonenumbers/data

metadata: phonenumbers/data/__init__.py tests/testdata/__init__.py

tests/testdata/__init__.py:  ../resources/PhoneNumberMetaDataForTesting.xml buildmetadatafromxml.py
	python buildmetadatafromxml.py ../resources/PhoneNumberMetaDataForTesting.xml tests/testdata

test: tests/testdata/__init__.py
	python tests/__init__.py

# Coverage; requires coverage module
COVERAGE_FILES=phonenumbers/*.py
coverage: coverage_clean coverage_generate coverage_report
coverage_clean:
	coverage -e
coverage_generate:
	coverage -x phonenumbers/re_util.py
	coverage -x tests/__init__.py
coverage_report:
	coverage -m -r $(COVERAGE_FILES)

sdist:
	python setup.py sdist

install: dist
	sudo python setup.py install

clean:
	rm -f MANIFEST *.pyc phonenumbers/*.pyc phonenumbers/data/*.pyc tests/*.pyc

distclean:
	rm -rf phonenumbers/data tests/testdata