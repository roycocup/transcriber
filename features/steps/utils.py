from libs import bucket
import os


def create_test_file(filename):
    with open(filename, 'w') as f:
        text_str = "Lorem in exercitation nisi veniam quis elit cupidatat consequat commodo."
        f.write(text_str)
    
def delete_test_file(filename):
    if os.path.isfile(filename):
        os.remove(filename)


def create_test_bucket(bucket_name):
    try:
        bucket.Bucket().create_bucket(bucket_name)
    except:
        pass

def delete_test_bucket(bucket_name):
    try:
        bucket.Bucket().delete_bucket(bucket_name)
    except:
        pass

def get_all_buckets():
    return bucket.Bucket().get_all_buckets()