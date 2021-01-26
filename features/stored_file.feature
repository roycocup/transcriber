Feature: Files can be created, updated and deleted from storage

    Scenario: We can upload files to storage
        Given we have a bucket named "test-transcriber-rodderscode-co-uk"
        When we upload a file named "test-file.mp3" to "test-transcriber-rodderscode-co-uk"
        Then the file "test-file.mp3" exists on "test-transcriber-rodderscode-co-uk"

    Scenario: We can delete existing file
        Given we have a file named "test-file.mp3" exists in "test-transcriber-rodderscode-co-uk"
        When we delete the file named "test-file.mp3" in "test-transcriber-rodderscode-co-uk"
        Then the file "test-file.mp3" does not exist on "test-transcriber-rodderscode-co-uk"