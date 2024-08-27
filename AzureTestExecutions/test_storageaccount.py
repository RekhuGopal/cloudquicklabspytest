from azure.identity import AzureCliCredential
from azure.mgmt.storage import StorageManagementClient

# Replace these values with your Azure subscription ID, resource group, and storage account name
SUBSCRIPTION_ID = '063965e0-d141-48d4-b8bd-0dfdc0dc00ff'
RESOURCE_GROUP = 'demorg'
STORAGE_ACCOUNT_NAME = 'cloudquicklabssa'

from AzureTestCases.azure_storageaccount_tests import azure_check_if_storage_account_exists
# Authenticate using Azure CLI credentials
credential = AzureCliCredential()

# Create a Storage Management Client
storage_client = StorageManagementClient(credential, SUBSCRIPTION_ID)

def test_azure_check_if_storage_account_exists():
    assert azure_check_if_storage_account_exists(storage_client ,RESOURCE_GROUP, STORAGE_ACCOUNT_NAME ) == True