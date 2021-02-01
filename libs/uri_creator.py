class UriCreator():

    @staticmethod
    def get_uri(bucket_name, file_name):
        return "gs://" + bucket_name + "/" + file_name