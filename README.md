# currency-converter-api

Running Test Coverages


The testing/ module has pytest unit tests.
To run the complete coverage test :
python -m coverage run -m pytest test

To run specific sub-test module :
python -m coverage run -m pytest test/<folder/file name of the test>

To output the report for the previously run coverage tests:
coverage report --omit=<environment_folder_name>/*

To export the report in HTML:
coverage html --omit=<environment_folder_name>/*