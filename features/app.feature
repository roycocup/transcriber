Feature: Application gets a transcription for an audio file

    Scenario: User uploads a file via web interface
        Given user goes to index page
        When they upload a file
        Then a file exists in temp directory
        And a db entry exists with the name of the file