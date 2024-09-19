import logging
import os
from datetime import datetime

# Generate the log file name with the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create the directory for the logs
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Define the full path to the log file
LOG_FILE_path = os.path.join(logs_dir, LOG_FILE)

# Configure the logging
logging.basicConfig(
    filename=LOG_FILE_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Correct the main block
if __name__ == "__main__":
    logging.info("Logging has started")

    # Add a print statement to verify if this block is running
    print("Logging has started and should be written to", LOG_FILE_path)

    # Manually flush the logging handlers
    for handler in logging.getLogger().handlers:
        handler.flush()
