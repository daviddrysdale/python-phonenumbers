Only raise issues that are **specific to the Python version** here, please.

Before reporting an issue with parsing particular numbers, check if the problem also occurs with the online version of the Java code at <https://libphonenumber.appspot.com/>

If the same problem is visible with the Java code, report the problem upstream not here:

- [checklist](https://github.com/google/libphonenumber/blob/master/CONTRIBUTING.md#checklist-before-filing-an-issue)
- (non-GitHub) [issue tracker](http://issuetracker.google.com/issues/new?component=192347).

If the problem **only** occurs with the Python version of the library, continue opening an Issue:

- Delete this template text.
- Include Python version (`python --version`)
- Include library version (`python -c "import phonenumbers; print(phonenumbers.__version__)"`)
