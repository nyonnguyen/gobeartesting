##REQUIREMENTS
Make sure **Python 3** is installed on your system.<br>
https://www.python.org/ftp/python/3.8.1/python-3.8.1.exe

**Pip** is used to manage dependencies. Go to https://pip.pypa.io/en/stable/installing/#do-i-need-to-install-pip for details.

Before start the project, install all dependencies by following command:<br>
> pip install -r requirements<br>

where *requirements* is the list of dependencies packaged along with this project.

## RUN
To run the test for demo, start by this command:
> robot -P ./Libs -d Results Tests

where:<br>
    ***-P ./Libs*** is the customized codes you need to include in this project<br>
    ***-d Results*** is where the report will be stored<br>
    ***Tests*** is where test scripts are defined

