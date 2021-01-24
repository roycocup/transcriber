from libs.bucket import Bucket
import time

bucket = Bucket()

buckets = bucket.get_all_buckets()

all_files = bucket.get_all_files(buckets)

print(all_files)



