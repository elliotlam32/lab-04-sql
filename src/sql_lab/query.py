import logging
import os
import mysql.connector
import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

#variables from environments
DBHOST = os.environ.get("DBHOST")
DBUSER = os.environ.get("DBUSER")
DBPASS = os.environ.get("DBPASS")  
DBNAME = os.environ.get("DBNAME") 

def get_data_by_group(value):
    """returns rows where the group column equals value."""
    logger.info(f"querying table 'mock' for rows where `group` = '{value}'...")
    query = "SELECT * FROM mock WHERE `group` = %s;"

    try:
        # Establish connection to MySQL database
        connection = mysql.connector.connect(
            host=DBHOST,
            user=DBUSER,
            password=DBPASS,
            database=DBNAME,
        )
        cursor = connection.cursor()

        cursor.execute(query, (value,))
        results = cursor.fetchall()

        logger.info(f"Successfully retrieved {len(results)} rows for group = '{value}'.")
        connection.close()
        return results

    except mysql.connector.Error as er:
        logger.error(f"error: {er}")
        return None


def plot_counts(groupby):
    """runs a value counts function, gives value counts for each distinct level in the column.

    arguments:
        groupby (str): The name of the column to group rows by (e.g., 'group').

    returns:
        pd.DataFrame: A DataFrame containing distinct column values and their row counts.
    """
    logger.info(f"running GROUP BY query on column '{groupby}'...")

    # Select column and count rows per distinct group
    query = f"SELECT `{groupby}`, COUNT(*) FROM mock GROUP BY `{groupby}`;"

    try:
        # connect to MySQL database
        connection = mysql.connector.connect(
            host=DBHOST,
            user=DBUSER,
            password=DBPASS,
            database=DBNAME,
        )
        cursor = connection.cursor()

        # execute GROUP BY aggregation query
        cursor.execute(query)
        results = cursor.fetchall()

        logger.info(f" calculated row counts grouped by '{groupby}'.")
        connection.close()

        # return pandas DataFrame with results
        df = pd.DataFrame(results, columns=[groupby, "count"])
        return df

    except mysql.connector.Error as er:
        logger.error(f" error: {er}")
        return None


def main():
    """Calls query functions to demonstrate filtering by 'group11' and displaying group counts."""
    # 1. Fetch and print rows specifically for 'group 1'
    print(" rows where group = 'group 1'")
    group1_results = get_data_by_group("group1")
    print(group1_results)

    # 2. Get and print value counts grouped only by the 'group' column
    print(" Row Counts Grouped by 'group'")
    group_counts = plot_counts("group")
    print(group_counts)


if __name__ == "__main__":
    main()
