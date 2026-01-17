import logging
import os
from datetime import datetime




LOG_File = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(),"logs")
os.makedirs(log_path,exist_ok=True)
LOG_File_PATH = os.path.join(log_path,LOG_File)

logging.basicConfig(
    filename = LOG_File_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)