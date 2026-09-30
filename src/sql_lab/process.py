import logging
import os
import pandas as pd
from sqlalchemy import create_engine, text

DBHOST = os.getenv('DBHOST')
DBUSER = os.getenv('DBUSER')
DBPASS = os.getenv('DBPASS')
DBNAME = os.getenv('DBNAME')
CSV_FILE = "MOCK_DATA.csv"
TABLE = "mock"

#logging
logging.basicConfig(
	level=logging.INFO,
	format="%(asctime)s - %(levelname)s - %(message)s"
)

def read_data(filename):
	"""reads csv file using pandas, returns dataframe"""
	logging.info("reading data{filename}")
	df = pd.read_csv(filename)
	#pandas read function
	logging.info("loaded into dataframe")
	return df

def clean_data(data):
	"""cleans data by dropping my rows with missing values"""
	logging.info("start cleaning")
	df_clean = data.dropna()
	#drops missing values and new df is df_clean
	logging.info("cleaned")
	return df_clean

def load_data(data, table="mock"):
    """Creates table (if it doesn't exist) and uploads DataFrame into MySQL."""
    if not all([DBHOST, DBUSER, DBPASS, DBNAME]):
        logging.error("missing database environment variables!")
        raise SystemExit("Set DBHOST, DBUSER, DBPASS, and DBNAME before running.")

    logging.info(f"connecting to database '{DBNAME}' on host '{DBHOST}'...")
    url = f"mysql+mysqlconnector://{DBUSER}:{DBPASS}@{DBHOST}:3306/{DBNAME}"
    engine = create_engine(url)

    
    try:
        logging.info(f"uploading {len(data)} rows into table '{table}'...")
        
        # 2. Indent data.to_sql inside the try block
        data.to_sql(name=table, con=engine, if_exists="append", index=False)
        
        with engine.connect() as conn:
            count = conn.execute(text(f"SELECT COUNT(*) FROM `{table}`")).scalar()
            
        logging.info(f"success. Table '{table}' now has {count} total rows.")
    except Exception as e:
        logging.error(f"upload failed: {e}")
        raise
    finally:
        engine.dispose()

def main():
	raw_data = read_data("MOCK_DATA.csv")
	cleaned_data = clean_data(raw_data)
	load_data(cleaned_data, table = "mock")

if __name__ == "__main__":
	main()
