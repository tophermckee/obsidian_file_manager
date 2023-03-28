from pathlib import Path
from pyomd import Notes
from pyomd import Note
from pyomd.metadata import MetadataType
import os, logging
import __main__

logging.basicConfig(
    level=logging.INFO,
    format="\n[%(levelname)s] %(asctime)s -- %(filename)s on line %(lineno)s\n\tFunction name: %(funcName)s\n\tMessage: %(message)s\n",
    datefmt='%B-%d-%Y %H:%M:%S',
    filename=f"logs/{Path(__main__.__file__).stem}.log",
    filemode='w'
)