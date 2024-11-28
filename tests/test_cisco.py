import json
import os
import pytest
from mydict import MyDict
from unittest.mock import MagicMock
from src.cisco import CiscoSSHDevice

current_dir = os.path.dirname(__file__)

test_file_path = os.path.join(current_dir, 'mock_data_cisco.json')

with open(test_file_path, "r") as f:
    netbox_data = json.load(f)
    mock_interfaces = [MyDict(x) for x in netbox_data["interfaces"]]

