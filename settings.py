import os
import logging
from pathlib import Path
from logging.config import dictConfig
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN, BOT_PREFIX = os.getenv('BOT_TOKEN'), os.getenv('BOT_PREFIX')

OWNER = 435421256028782603

BASE_DIR = Path(__file__).parent
COG_DIR = BASE_DIR / "cogs"

# ! don't use this; not finished
LOGGING_CONFIG = {
    "version": 1,
    "disabled_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[%(levelname)s] : ( %(asctime)s ) - ( Module @ %(module)s ): %(message)s"
        },
        "standard": {
            "format": "[%(levelname)s] - ( Name : %(name)s ) : %(message)s"
            },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
        "console2": {
            "level": "WARNING",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "logs/infos.log",
            "mode": "w",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "bot": {
            "handlers": ["console"], "level": "INFO", "propagate": False
            },
        "discord": {
            "handlers": ["console2", "file"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

VER = 1.0
DD_LOGO = f"""
\u001b[38;5;214m======================================================================================
\u001b[38;5;92m      d8b                      d8b             d8b                                    
      88P                      ?88             88P                               d8P  
     d88                        88b           d88                             d888888P
 d888888   d888b8b    88bd88b   888  d88' d888888   d8888b   88bd88b ?88   d8P  ?88'  
d8P' ?88  d8P' ?88    88P' ?8b  888bd8P' d8P' ?88  d8P' ?88  88P' ?8bd88   88   88P   
88b  ,88b 88b  ,88b  d88   88P d88888b   88b  ,88b 88b  d88 d88   88P?8(  d88   88b   
`?88P'`88b`?88P'`88bd88'   88bd88' `?88b,`?88P'`88b`?8888P'd88'   88b`?88P'?8b  `?8b  

\u001b[38;5;214m Made by Deludank                                                       Version : {VER}
======================================================================================\u001b[0m \n"""

dictConfig(LOGGING_CONFIG)