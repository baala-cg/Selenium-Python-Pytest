# Selenium | Python | PyTest | POM | Virtualenv | Allure Reports 

# Libraries required:
1. PyCharm - Community Edition
2. Python
3. oracle-jdk-8


# Install virtual env
--pip install virtualenv
or
--pip -m pip install virtualenv

# Verify python version
python --version
where python


# Create virtual env with name venv1
virtualenv --python=<python.exe path from "where python" command> virtual env name

My system:
--virtualenv --python="C:\Users\JyothyKrishna\AppData\Local\Programs\Python\Python311\python.exe" venv2
--virtualenv --python="C:\Programs Files\miniconda\4.7\python.exe" venv2
--cd venv2/Scripts
--activate.bat

--deactivate

# Install all the requirements from the requirements.txt
--pip install -r requirements.txt

If above is not working, try below
--C:\Windows\System32\venv1\Scripts\python.exe -m pip install -r requirements.txt
--pip list

If there is an SSL error, try below:
Navigate to
--C:\Program Files\miniconda\latest\Library\bin

copy below 4 files to
1. libcrypto-1_1-x64.dll
2. libcrypto-1_1-x64.pdb
3. libssl-1_1-x64.dll
4. libssl-1_1-x64.pdb

paste them in below location:
--C:\Program Files\miniconda\latest\DLLs


# Allure installation:
download allure-commandline 2.20 library
https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.0/
Extract the zip file and then place the directory in Program Files(x86)

copy the bin path and add it to Path env in environment variables section


# Java installation:
Set up the env variable

# In PyCharm:
File-> Settings - > Project -> Project Interpreter -> Settings -> Add -> Existing environment -> Browse ->
select python.exe from virtual env - venv1

# Run the test suite from Terminal:

To run the test by displaying the verbose output on console:
pytest -v

Another way to trigger the run:
python -m pytest

To run test by passing browser value as an argument:
python -m pytest --browser firefox

To generate html report: (additional supporting files folder)
python -m pytest --html=reports/report_test.html

To generate html report that can be shared:
python -m pytest --html=reports/report_test.html --self-contained-html

To generate allure report:
python -m pytest --alluredir=reports/allure-reports
allure serve reports/allure-reports
