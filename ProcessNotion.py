import os
import csv
import pandas as pd
from notion_client import Client
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotionDatabaseDW:
    def __init__(self, notion_token, database_id):
        self.notion = Client(auth=notion_token)
        self.database_id = database_id

    def query_database(self):
        logging.info("Querying Notion database...")
        results = self.notion.databases.query(database_id=self.database_id)
        logging.info("Database query successful.")
        return results

    def extract_data_and_export_to_csv(self, results):
        logging.info("Extracting data from query results...")
        data = []
        columns = results["results"][0]["properties"].keys()

        for page in results["results"]:
            row = {}
            row['id'] = page["id"]
            for column in columns:
                property_type = page["properties"][column]["type"]
                if property_type in page["properties"][column]:
                    row[column] = page["properties"][column][property_type]
                else:
                    row[column] = ""
            data.append(row)

        df = pd.DataFrame(data)
        df.to_csv("notion_database.csv", index=False, quoting=csv.QUOTE_NONNUMERIC)
        logging.info("Data extracted and exported to CSV.")
        return df

    def preprocess_df(self, df):
        logging.info("Preprocessing DataFrame...")
        df['Date'] = df['Date'].apply(lambda x: x['start'])
        df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
        df = df[['Date', 'id', 'Lesson']]
        df = df.sort_values(by=['Date'])
        logging.info("DataFrame preprocessed.")
        return df

    def filter_df(self, df):
        logging.info("Filtering DataFrame...")
        df_false = df[df['Lesson']==False]
        filtered_df = df_false[(df_false['Date'] > df[df['Lesson']].iloc[-1]['Date']) & (df_false['Date'] <= pd.to_datetime('today'))]
        logging.info("DataFrame filtered.")
        return filtered_df

if __name__ == "__main__":
    os.environ['NOTION_TOKEN'] = "secret_CMReE8WJf2haF5GOtXhTdQhV0cuqgKkQ3jbZonPwaa6"
    notion_token = os.environ['NOTION_TOKEN']
    database_id = "4f78345b0ef34834a390df791deca075"

    DW = NotionDatabaseDW(notion_token, database_id)
    results = DW.query_database()
    df = DW.extract_data_and_export_to_csv(results)
    df = DW.preprocess_df(df)
    filtered_df = DW.filter_df(df)
    logging.info("Filtered DataFrame:\n%s", filtered_df)
