# Imports the Google Cloud client library
from google.cloud import storage


class Bucket:

    def __init__(self):
        self.client = storage.Client()

    def get_all_buckets(self):
        buckets = self.client.list_buckets()
        b = []
        for bucket in buckets:
            b.append(bucket)
        return b

    def get_all_files(self, buckets):
        files = []
        for bucket in buckets:
            bucket_url = f"gs://{bucket.name}"
            for blob in bucket.list_blobs():
                files.append(bucket_url + "/" + blob.name)
        return files

    def create_bucket(self, bucket_name):
        return self.client.create_bucket(bucket_name)

    def delete_bucket(self, bucket_name):
        return self.client.bucket(bucket_name).delete(force=True)
    
    # def delete_file_in_bucket(self, bucket_name, file_name):
    #     blob = bucket.blob(file_name)
    #     return blob.delete()