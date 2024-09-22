## Pip modules:
from loguru import logger

## Bot modules:
from config import DIR_PATH, BOT_NAME

## Create the logger.
logger.add(
    f"{DIR_PATH}/LOGS.log", 
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}", 
    rotation="1 MB", 
    compression="zip", 
    level="DEBUG", 
    colorize=True
)

## Logger for bot starting.
def start_logger() -> None:
    """Logger for bot starting.
    """
    logger.debug(f"""
    |------------------------------>
    | Bot {BOT_NAME} was launched!
    |------------------------------>
    """
)
    
## Logger for errors.
def error_logger(error: Exception) -> None:
    """Logger for bot errors.
    
    Args: 
        error (Exception) : An occured error.
    """
    logger.error(f"""
    |------------------------------>
    | An occured error while running {BOT_NAME},
    | Error: {error}
    |------------------------------>
    """)

## Logger for checking if commands is working.
def on_ready_logger() -> None:
    """Logger for bot commands starting.
    """
    logger.debug(f"""
    |------------------------------>
    | Bot {BOT_NAME} is ready to work!
    |------------------------------>
    """)
    
## Logger for commands.   
def command_logger(command: str, 
            username: str,
            user_id: int,
            channel_name: str, 
            guild_name: str, 
            command_args: list
        ) -> None:
    """Logger for bot commands.

    Args:
        command (str): command name.
        username (str): members username.
        channel_name (str): channel, where was used command.
        guild_name (str): guild name.
        command_args (list): arguments.
    """
    logger.info(f"""
    | Command: {command},
    | Username: {username},
    | Id: {user_id},
    | Channel: {channel_name},
    | Guild: {guild_name},
    | Args: {command_args}
    """)
    
## Logger for starting youtube request.
def init_youtube_request(url: str, title: str, video_id: int,) -> None:
    """Logging the initialization of downloader.

    Args:
        url (str): video url.
        title (str): video title.
        video_id (int): video_id.
    """
    
    logger.debug(f"""
    | INITIALIZATION THE DOWNLOADER 
    | URL: {url}
    | TITLE: {title}
    | VIDEO ID: {video_id}
    """)

## Logger for checking if file was downloaded.
def downloading_completed(filename: str) -> None:
    """Logging the completed download.

    Args:
        filename (str): name of file.
    """
    
    logger.info(f"""
    | FILE DOWNLOADED 
    | FILENAME: {filename}
    """)