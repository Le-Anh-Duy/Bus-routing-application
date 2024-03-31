import logging

class Logger:
  """
  A simple logger class that provides convenience methods for logging messages.
  """

  def __init__(self, name, level=logging.INFO, file_name=None):
    """
    Initializes the logger with a name, logging level, and optional file for logging.

    Args:
      name (str): The name for the logger.
      level (int, optional): The minimum severity level for logged messages. Defaults to logging.INFO.
      file_name (str, optional): The filename to log messages to. Defaults to None (console only).
    """

    self.logger = logging.getLogger(name)
    self.logger.setLevel(level)

    # Add file handler if provided
    if file_name:
      file_handler = logging.FileHandler(file_name)
      self.logger.addHandler(file_handler)

  def debug(self, message):
    """Logs a debug message."""
    self.logger.debug(message)

  def info(self, message):
    """Logs an informational message."""
    self.logger.info(message)

  def warning(self, message):
    """Logs a warning message."""
    self.logger.warning(message)

  def error(self, message):
    """Logs an error message."""
    self.logger.error(message)

  def critical(self, message):
    """Logs a critical message."""
    self.logger.critical(message)

# Example usage
my_logger = Logger(__name__, level=logging.DEBUG, file_name="myapp.log")

my_logger.debug("This is a debug message")
my_logger.info("This is an informational message")
my_logger.warning("This is a warning message")
