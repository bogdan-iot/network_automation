import json
import pytest
from mydict import MyDict
from unittest.mock import MagicMock
from src.cisco import CiscoSSHDevice

with open("mock_data_cisco.json", "r") as f:
    netbox_data = json.load(f)
    mock_devices = [MyDict(x) for x in netbox_data["devices"]]
    mock_prefixes = [MyDict(x) for x in netbox_data["prefixes"]]


class TestNetBox:
    @pytest.fixture
    def mock_dcim(self):
        # Create a mock dcim object and mock the devices.all() method
        mock_dcim = MagicMock()
        mock_dcim.devices.all.return_value = mock_devices
        return mock_dcim
