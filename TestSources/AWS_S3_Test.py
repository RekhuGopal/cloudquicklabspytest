def aws_s3_check_if_buckets_exist(s3):
    try:
      response = s3.list_buckets()
      buckets =[]
      for bucket in response['Buckets'] :
        buckets += {bucket["Name"]}
    except Exception as e:
        print("error occured while invoking aws_s3_check_if_buckets_exist and error is {}".format(e))
        return False
    else:
        if buckets :
            return True
        else :
            return False