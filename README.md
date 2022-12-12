# Simple ETL Process with Python and SQLite
## Objectives
The objective of this project is to demonste ETL concept through a simple project.

## Project Description
This is a simple project to describe ETL process with Python and SQLite. The extraction process uses Python requests library and the transormation process uses Python requests library, then the data is loaded to the SQLite database with the help of Python `sqlite3` library. The data source is from openbrewery API which shares an open data of a list of breweries (mostly) in America. The API is open and requires no API Key, can be accessed based on several values. Please visit the API documentaiton for more detail.

## Library requirements
Here are the Python libraries that are used for this project
```
pandas=
requests=
sqlite3=
```
Pandas and Requests are external libraries, can be installed with `pip` or `conda`. On the other hand, `sqlite3` is a built in library and its version might depends on the Python version.

## Project Structure
There are two files: `main.py` and `sql_ops.py`. The `main.py` file is where the ETL process being computed. The `sql_ops.py` is used to store sql related functions:
1. Open cnnection function: to the SQLite (also it will immediately create `.db` file)
2. Execute SQL query function: to execute create and insert query process.
3. Create table function: consists of SQL query to create table along with the execution
4. Insert table function: cosnsist of SQL query to insert data to the table along with the execution

## ETL Process Overview
### Extraction Process
Using Python requests library to get the API response and its data with HTTP GET method. The program will be exited if the status code is other than 200.
### Transformation Process
The API response will be transformed to JSON then to Pandas DataFrame. There are 4 actions will be performed at this process:
1. Dropping unecessary information
2. Changing data type accordingly
3. Replacing NaN data.
4. Finding and dropping (if any) duplicates.
### Loading Process
There are 3 procedures:
1. Open Connection to the database by providing the path to the SQLite file.
2. Create table in the SQLite.
3. Inserting Data to the previously created table.

## How to
If you like to demonstrate this project feel free to clone this repo, then running the ``main.py`` file with Python.
Example running the program in Windows machine
```
python main.py
```