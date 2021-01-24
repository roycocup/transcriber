from google.cloud import storage 

class GFiles:
    

    def __init__(self, bucket_name):
        self.bucket_name = bucket_name


    
    def upload(self, filename):
        client = storage.Client()
        bucket = client.bucket(self.bucket_name)
        blob = bucket.blob(filename)

        blob.upload_from_filename(filename)

        return bucket.blob(filename)

    def delete(self, filename):
        pass

