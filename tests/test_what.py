import unittest

import mod.what

class WhatTest(unittest.TestCase):
  def test_thing(self):
    assert "working" in mod.what.thing()
