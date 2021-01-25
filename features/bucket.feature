Feature: Accessing bucket storage on cloud

    Scenario: Able to create a bucket
        Given we have a client
        When when we create a bucket named "test-transcriber-rodderscode-co-uk"
        Then the bucket "test-transcriber-rodderscode-co-uk" exists


    Scenario: Able to delete a bucket
        Given we have a bucket named "test-transcriber-rodderscode-co-uk"
        When we delete the bucket named "test-transcriber-rodderscode-co-uk"
        Then the bucket "test-transcriber-rodderscode-co-uk" does not exist