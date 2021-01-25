Feature: Accessing bucket storage on cloud

    Scenario: Able to create a bucket
        Given we have a client
        When when we create a bucket named "test-transcriber-rodderscode-co-uk"
        Then the bucket "test-transcriber-rodderscode-co-uk" exists


    Scenario: Able to delete a bucket
        Given we have a bucket named "test-transcriber-rodderscode-co-uk"
        When we delete the bucket named "test-transcriber-rodderscode-co-uk"
        Then the bucket "test-transcriber-rodderscode-co-uk" does not exist


    Scenario: Able to get a list of buckets
        Given the bucket "test1-transcriber-rodderscode-co-uk" does not exist
        And the bucket "test2-transcriber-rodderscode-co-uk" does not exist
        When when we create a bucket named "test1-transcriber-rodderscode-co-uk"
        And when we create a bucket named "test2-transcriber-rodderscode-co-uk"
        Then the bucket "test1-transcriber-rodderscode-co-uk" exists
        And the bucket "test2-transcriber-rodderscode-co-uk" exists

    