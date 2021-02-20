Feature: Ability to transcribe a sound file

    Scenario: Transcribe a mp3 file
        Given we have a test file in "test-transcriber-rodderscode-co-uk"
        When we ask for a transcription
        Then we get a transcription json

    Scenario: Transcribe an mp3 file asyncronously
        Given we have a test file in "test-transcriber-rodderscode-co-uk"
        When we ask for a transcription asyncronously
        Then we get a token
        Then if we wait 
        Then we get a transcription json
    