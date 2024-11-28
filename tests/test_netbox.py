import json
import pytest
from mydict import MyDict
from unittest.mock import MagicMock
from src.netbox import NetBoxInstance

with open("mock_data_netbox.json", "r") as f:
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

    @pytest.fixture
    def mock_ipam(self):
        # Create a mock ipam object and mock the prefixes.all() method
        mock_ipam = MagicMock()
        mock_ipam.prefixes.all.return_value = mock_prefixes
        return mock_ipam

    def test_duplicated_device_serials(self, mock_dcim):
        """Test for checking duplicated device serials in NetBox."""
        # Create an instance of NetBoxInstance
        instance = NetBoxInstance(url="http://fake-url", token="fake-token")

        # Inject the mock dcim object into the instance
        instance.dcim = mock_dcim

        # Call the method under test
        duplicates = instance.duplicated_device_serials()

        # Assertions
        assert duplicates == ["ABC123"], "Should detect the duplicated serial 'ABC123'"
        mock_dcim.devices.all.assert_called_once()  # Ensure the mock was called

    def test_prefixes_number(self, mock_ipam):
        # Create an instance of NetBoxInstance
        instance = NetBoxInstance(url="http://fake-url", token="fake-token")

        # Inject the mock ipam object into the instance
        instance.ipam = mock_ipam

        # Call the method under test
        prefixes = instance.get_prefixes_number()

        # Assertions
        assert prefixes == 2
        mock_ipam.prefixes.all.assert_called_once()  # Ensure the mock was called
