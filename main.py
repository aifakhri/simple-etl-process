import pandas as pd
from requests import get
from sql_ops import open_connection, create_table, insert_data


BASE_URL = "https://api.openbrewerydb.org/breweries"
SQLITE_PATH = "breweries.db"
DROPPED_COLUMNS = [
    "id", "address_2", "address_3", 
    "county_province", "updated_at", "created_at"
]
CHANGED_DTYPE = {
    "longitude": float,
    "latitude": float,
}


def check_data_status(status=False):
    """Checking table status before/after transformation

    False is to show data before transformation process.
    True is to show data after transformation process.
    """
    text = "After" if status else "Before"
    print(f"Data Information {text} Transformation")
    df_breweries.head()
    df_breweries.info()


# Data Extraction: Get the API data
response = get(BASE_URL)

# Handling Error if the request failed
if response.status_code != 200:
    print("Requests Error, Terminate Program")
    exit()

# Transform requests result to JSON then into Pandas DataFrame
data = response.json()
df_breweries = pd.json_normalize(data)

# showing the DataFrame before data transformation
check_data_status()

# Data Transformation 1: Removing unnecessary table
df_breweries.drop(DROPPED_COLUMNS, axis=1, inplace=True)

# Data Transformation 2: Change data type
df_breweries = df_breweries.astype(CHANGED_DTYPE)

# Data Transformation 3: Changed null values
for col in df_breweries.columns:
    if (df_breweries[col].dtype == "O"):
        df_breweries[col].fillna("Unknown", inplace=True)
    elif (df_breweries[col].dtype == float):
        df_breweries[col].fillna(0.0, inplace=True)

# Data Transformation 4: Get Duplicates
total_duplicates = len(df_breweries[df_breweries.duplicated(keep=False)])
if total_duplicates > 0:
    df_breweries.drop_duplicates(keep="first", inplace=True)

check_data_status(True)
# Loading data into SQLite
connection = open_connection(SQLITE_PATH)

# 1. Creating Table if any
create_table(connection)

# 2. Insert Data to Table
# Change DataFrame to List
data = df_breweries.values.tolist()
insert_data(connection, data)
