import pymongo
import pandas as pd
import numpy as np
import json
import os, sys
from dataclasses import dataclass

@dataclass
class Environment_variable:
    mongo_db_url = os.getenv('MONGO_DB_URL')


env_var = Environment_variable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
TARGET_COLUMNS = 'expenses'


