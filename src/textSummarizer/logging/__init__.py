import os 
import sys
import logging

# define the logging string
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"


#define the log directory and filepath
log_dir="logs"
log_file_path = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)

# give the basic config for the logs
logging.basicConfig(
    level=logging.INFO,
    format= logging_str,
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler(sys.stdout)

    ]
)

# create the logger object that uses the logging config

logger = logging.getLogger("textSummarizerLogger")

