from google.cloud import storage 

class GFiles:
    
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
    
    def upload(self, filename):
        bucket = self._get_bucket()
        blob = bucket.blob(filename)
        blob.upload_from_filename(filename)

        return bucket.blob(filename)

    def delete(self, filename):
        bucket = self._get_bucket()
        blob = bucket.blob(filename)
        blob.delete()

    def _get_bucket(self):
        client = storage.Client()
        return client.bucket(self.bucket_name)
    
    def get_file_by_name(self, filename):
        bucket = self._get_bucket()
        return bucket.blob(filename)

