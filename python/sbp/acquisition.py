#!/usr/bin/env python
# Copyright (C) 2015 Swift Navigation Inc.
# Contact: Fergus Noble <fergus@swiftnav.com>
#
# This source is subject to the license found in the file 'LICENSE' which must
# be be distributed together with this source. All other rights reserved.
#
# THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
# EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.

from construct import *
from sbp import SBP
from sbp.utils import fmt_repr
import six

# Automatically generated from piksi/yaml/swiftnav/sbp/acquisition.yaml
# with generate.py at 2015-04-06 23:40:11.138411. Please do not hand edit!


SBP_MSG_ACQ_RESULT = 0x0015
class MsgAcqResult(SBP):
  """SBP class for message MSG_ACQ_RESULT (0x0015).
  
  This message describes the results from an attempted GPS signal
acquisition search for a satellite PRN over a code phase/carrier
frequency range. It contains the parameters of the point in the
acquisition search space with the best signal-to-noise (SNR)
ratio.


  Parameters
  ----------
  snr : float
    SNR of best point.
  cp : float
    Code phase of best point.
  cf : float
    Carrier frequency of best point.
  prn : int
    PRN identifier of the satellite signal for which
acquisition was attempted.


  """
  _parser = Struct("MsgAcqResult",
                   LFloat32('snr'),
                   LFloat32('cp'),
                   LFloat32('cf'),
                   ULInt8('prn'),)

  def __init__(self, sbp):
    self.__dict__.update(sbp.__dict__)
    self.from_binary(sbp.payload)

  def __repr__(self):
    return fmt_repr(self)
 
  def from_binary(self, d):
    p = MsgAcqResult._parser.parse(d)
    self.__dict__.update(dict(p.viewitems()))

  def to_binary(self):
    return MsgAcqResult.build(self.__dict__)
    

msg_classes = {
  0x0015: MsgAcqResult,
}