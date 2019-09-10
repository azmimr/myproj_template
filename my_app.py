"""This is a sample app which uses the modules in this project.
"""

# Required imports for logging, configuration files
import logging
from logging.config import fileConfig
from configparser import ConfigParser
from datetime import datetime

# Imports for DS, ML from external packages

# Other imports from external packages

# Imports from custom packages
import mypackage


# Setup logging for this app
# New log file createddaily
log_filename = f"my_app_{datetime.now().strftime('%Y%m%d')}.log"
fileConfig('logging_config.ini', defaults={'logfilename': log_filename})
logger = logging.getLogger()  # Using root so oth loggers will be captured


def main():
    logger.info("Creating an instance of MyClass")
    my_instance = mypackage.MyClass()

    logger.info("Reading in config file")
    config = ConfigParser()
    config.read('config_sample.ini')

    logger.info("Display a value from the config file")
    print(f"Compression flag = {config['DEFAULT'].getboolean('Compression')}")

    logger.info("Calling display function from MyClass instance")
    my_instance.my_function()
    my_instance.my_function(text="This is in the app.")

    logger.info("End of App\n")


if __name__ == "__main__":
    main()
