# -*- coding: utf-8 -*-
"""
Created on October 30 2022
@author: asnadin
"""

import logging.config
from configs.log_config import logger_config

logging.config.dictConfig(logger_config)
logger = logging.getLogger("file_logger")



