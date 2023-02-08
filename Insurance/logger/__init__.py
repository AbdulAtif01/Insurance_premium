import logging
from datetime import datetime
import os

LOG_DIR = 'Insurance_log'

Current_Time_stamp = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

Log_File_Name = f"log_{Current_Time_stamp}.log"

os.makedirs(LOG_DIR,exist_ok = True)

Log_File_Path = os.path.join(LOG_DIR,Log_File_Name)

logging.basicConfig(filename=Log_File_Path,
filemode = "w",
format = '[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
level=logging.DEBUG,

)