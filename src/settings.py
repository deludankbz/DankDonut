# Copyright (c) 2025 deludank. All Rights Reserved.
# Standard settings for the bot

import psutil, platform, os, sys
import logging
from pathlib import Path
from logging.config import dictConfig
from dotenv import load_dotenv

load_dotenv()

# OWNERSHIP
OWNER = [435421256028782603]

# TOKENS
BOT_TOKEN = os.getenv('BOT_TOKEN')
BOT_PREFIX = "?"

# DIRS
# NOTE: unfortunally this path has to be like this due to glob
BASE_DIR = Path(__file__).parent 
COG_DIR = BASE_DIR / "cogs/"
CHATSOUNDS_DIR = 'extra/chatsounds/'

# Voice Chat shit
FFMPEG_OPS = { 
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5", 
    "options": "-vn"
}
YT_OPS = { 'format': 'bestaudio', 'noplaylist': True }

# LOGGING
LOGGING_CONFIG = {
    "version": 1,
    "disabled_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[%(levelname)s] : ( %(asctime)s - Module @ %(module)s ): %(message)s"
        },
        "standard": {
            "format": "[ %(levelname)s@%(name)s ] :: %(message)s"
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
            "mode": "a",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "bot": {
            "handlers": ["console"], 
            "level": "INFO", 
            "propagate": False
            },
        "discord": {
            "handlers": ["console2", "file"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

VER = "1.3.1"
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

gendocsPath = os.path.join(os.getcwd(), 'logs/gendocs.html')

def getSysInfo():
    info = f"""
```ansi
[2;34m[2;45m[2;37mDankDonut v{VER}
[0m[2;34m[2;45m[0m[2;34m[0m[1;2m[1;2m[1;34mHardware Info:
[0m[0m[1;34m    OS:[0m[0m[2;34m[2;34m[0m[2;34m[0m [2;32m{platform.platform()}
[2;34m[1;34m    CPU:[0m[2;34m[0m[2;32m {platform.processor()} [2;36m@[0m[2;32m {psutil.cpu_freq().max} GHz [0m[2;34m[2;34m[1;34m{psutil.cpu_count(logical=False)} Cores[0m[2;34m[0m[2;34m[0m; [2;34m[1;34m{psutil.cpu_count(logical=True)} Threads[0m[2;34m[0m
[2;32m    [0m    [2;33m{psutil.cpu_percent(interval=1)}% average usage.[0m
[2;34m[1;34m    RAM:[0m[2;34m[0m [2;33m[2;32m{psutil.virtual_memory().percent}% used of [0m[2;33m[0m[2;33m[2;33m{round(psutil.virtual_memory().total/1000000000, 2)} GB[0m[2;33m[0m

```
"""
    return info

def restart() -> None:
    """ Restarts the bot fully """
    # NOTE: For anyone curious, `os.execv()` replaces the current process with new one 
    os.execv(sys.executable, ['python3'] + sys.argv)

def update() -> None:
    """ Update the bot's files using `git pull` """
    os.system("git pull")

# EXTRA STUFF
def gendocs(aSortedCMD: list) -> list[str]:
    result = list()

    if os.path.isfile(gendocsPath):
        os.remove(gendocsPath)
        gendocs(aSortedCMD)

    with open(gendocsPath, 'w') as docfile:
        docfile.write('<!-- Generated docs for GitHub pages -->')
        for line in aSortedCMD:
            htmlCommandTemplate = f"""
<!-- {line.name}@{line.cog_name} -->
<div class="command-content">
    <p class="name">{line.name} <span class="aliases">{line.aliases if len(line.aliases) != 0 else ""}</span></p>
    <div class="desc">
        <p class="cog">{line.cog_name}</p>
        <p class="help">{line.help}</p>
    </div>
</div>
            """
            docfile.write(htmlCommandTemplate)
            result.append(htmlCommandTemplate)
            
    return result

dictConfig(LOGGING_CONFIG)
