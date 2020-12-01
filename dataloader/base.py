import os

import numpy as np


def create_loader():
  return BaseLoader()

class BaseLoader():

  def __init__(self):
    self.is_threaded = False
  
  def parse_args(self):
    """
    Parse arguments partially and return the remaining arguments.
    Args:
      args: The list of arguments.
    Returns:
      args: Parsed arguments.
      remaining_args: The list of remaining arguments.
    """
    raise NotImplementedError

  def prepare(self):
    """
    Prepare the data loader.
    Args:
      scales: The list of scales.
    """
    raise NotImplementedError
  
  def get_num_texts(self):
    """
    Get the number of texts.
    Returns:
      The number of texts.
    """
    raise NotImplementedError