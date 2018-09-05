# encoding:utf-8
__author__ = 'admin'

import pytest
import pytest_html

def test_01():
    x = "python"
    assert "p" in x

def test_02():
    assert 4 < 5
