def azure_check_if_storage_account_exists (storage_client, resource_group, storage_account_name):
    try:
        # Retrieve the storage account
        storage_account = storage_client.storage_accounts.get(resource_group, storage_account_name)

        if storage_account.name == storage_account_name:
            return True
        else:
            return False
    except Exception as e:
        print("Exception occured in test case check if storage account exist and error is {}".format(e))
        return False