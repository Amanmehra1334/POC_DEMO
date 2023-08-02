import os
import logging
import azure.functions as func
from azure.cosmos import CosmosClient
import pandas as pd

def get_container():
    try:
        cosmos_account = os.environ.get("CosmosAccountKey")
        cosmos_conn_str = os.environ.get("CosmosConnectionString")
        database_name = os.environ.get("DatabaseName")
        container_name = os.environ.get("ContainerName")

        client = CosmosClient(cosmos_account, cosmos_conn_str)

        logging.info("Initializing database client")
        database = client.get_database_client(database_name)

        logging.info("initializing container client")
        container = database.get_container_client(container_name)

        if container:

            logging.info("container fetched successfully")
            return container
        else:
            return "no such container available"
    except Exception as e:

        logging.info("error occured in fetching container")
        return e
    



