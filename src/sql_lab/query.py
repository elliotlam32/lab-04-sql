import logging
import os
import mysql.connector
import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Same defaults as basic-sql.ipynb; override with env vars if set.
DBHOST = os.environ.get("DBHOST")
DBUSER = os.environ.get("DBUSER")
DBPASS = os.environ.get("DBPASS")  # password on Canvas
DBNAME = os.environ.get("DBNAME")  # MOCK_DATA lives here

def get_data_by_group(value):
    """runs SELECT returning rows where the `group` column equals value."""
    logger.info(f"Querying table 'mock' for rows where `group` = '{value}'...")
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

        # Execute parameterized query safely using tuple parameter substitution
        cursor.execute(query, (value,))
        results = cursor.fetchall()

        logger.info(f"Successfully retrieved {len(results)} rows for group = '{value}'.")
        connection.close()
        return results

    except mysql.connector.Error as er:
        logger.error(f"Database error executing get_data_by_group: {er}")
        return None


def plot_counts(groupby):
    """Runs a SELECT ... GROUP BY query counting rows per distinct value of the specified column.

    Args:
        groupby (str): The name of the column to group rows by (e.g., 'group').

    Returns:
        pd.DataFrame: A DataFrame containing distinct column values and their row counts.
    """
    logger.info(f"Running GROUP BY query on column '{groupby}'...")

    # Select column and count rows per distinct group
    query = f"SELECT `{groupby}`, COUNT(*) FROM mock GROUP BY `{groupby}`;"

    try:
        # Establish connection to MySQL database
        connection = mysql.connector.connect(
            host=DBHOST,
            user=DBUSER,
            password=DBPASS,
            database=DBNAME,
        )
        cursor = connection.cursor()

        # Execute GROUP BY aggregation query
        cursor.execute(query)
        results = cursor.fetchall()

        logger.info(f"Successfully calculated row counts grouped by '{groupby}'.")
        connection.close()

        # Construct and return pandas DataFrame with aggregated results
        df = pd.DataFrame(results, columns=[groupby, "count"])
        return df

    except mysql.connector.Error as er:
        logger.error(f"Database error executing plot_counts: {er}")
        return None


def main():
    """Calls query functions to demonstrate filtering by 'group11' and displaying group counts."""
    # 1. Fetch and print rows specifically for 'group 1'
    print("=== Rows where group = 'group 1' ===")
    group1_results = get_data_by_group("group1")
    print(group1_results)

    # 2. Get and print value counts grouped only by the 'group' column
    print("\n=== Row Counts Grouped by 'group' ===")
    group_counts = plot_counts("group")
    print(group_counts)


if __name__ == "__main__":
    main()
