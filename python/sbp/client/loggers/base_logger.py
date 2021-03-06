# Copyright (C) 2015 Swift Navigation Inc.
# Contact: Mark Fine <mark@swiftnav.com>
#
# This source is subject to the license found in the file 'LICENSE' which must
# be be distributed together with this source. All other rights reserved.
#
# THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
# EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.

from ...table import dispatch
import calendar
import time

class BaseLogger(object):
  """
  BaseLogger

  The :class:`BaseLogger` provides log helper functions and context management.

  Parameters
  ----------
  filename : string
    File to log to.

  """
  def __init__(self, filename):
    self.handle = open(filename, "w+")
    self.base_time = time.time()

  def __enter__(self):
    return self

  def __exit__(self, *args):
    self.flush()
    self.close()

  def flush(self):
    self.handle.flush()

  def close(self):
    self.handle.close()

  def timestamp(self):
    """
    Timestamp generator.
    """
    return calendar.timegm(time.gmtime())

  def delta(self):
    """
    Relevant time differential generator.
    """
    return int((time.time() - self.base_time) * 1000)


class LogIterator(object):
  """
  LogIterator

  The :class: `LogIterator` provides an abstract interface for reading
  serialized logs of SBP data.

  Parameters
  ----------
  handle : File-like handle
    Any file-like handle providing SBP messages.

  """
  def __init__(self, handle, dispatcher=dispatch):
    self.handle = handle
    self.dispatcher = dispatcher

  def __enter__(self):
    return self

  def __exit__(self, *args):
    self.flush()
    self.close()

  def __iter__(self):
    return self

  def flush(self):
    self.handle.flush()

  def close(self):
    self.handle.close()

  def next(self):
    """Return the next record tuple from the log file. If an unknown SBP
    message type is found, it'll return the raw SBP. If EOF, throws
    exception and then returns to start of file.

    Returns
    -------
    (float, float, object)
      (elapsed msec since beginning of log, UTC timestamp, msg)

    """
    raise NotImplementedError("next() not implemented!")
