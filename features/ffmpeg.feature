Feature: Modify an audio file

    Scenario: modify a audio file from one type to another
        Given we have a test file named "test.mp3"
        When we run format command to type "flac"
        Then we get a file named "test.mp3.flac"
    
    @wip
    Scenario: modify the channels on a flac file 
        Given we have a file "test.flac" with "2" channels
        When we run a format command to make channels "1"
        Then we have a file "fake-test.flac" with "1" channels


