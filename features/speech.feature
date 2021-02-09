Feature: Ability to transcribe a sound file

    Scenario: Transcribe a mp3 file
        Given we have a test file in "test-transcriber-rodderscode-co-uk"
        When we ask for a transcription
        Then we get a transcription json