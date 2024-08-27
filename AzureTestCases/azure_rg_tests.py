def azure_check_if_rg_exists(resource_client, resource_group_name):
    try:
        # Retrieve the resource group
        resource_group = resource_client.resource_groups.get(resource_group_name)

        if resource_group.name == resource_group_name:
            return True
        else:
            return False
    except Exception as e:
        print("Exception occured in test case check if RG exist and error is {}".format(e))
        return False