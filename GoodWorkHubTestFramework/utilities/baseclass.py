"""Baseclass module."""
import inspect
import logging
import pytest

@pytest.mark.usefixtures('org_setup')
class BaseClass:
    """Inherit from the class(Parent class or base class)."""

    def getLogger(self):
        """Use for logging."""
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter('%(asctime)s :%(levelname)s : %(name)s :%(message)s')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger


