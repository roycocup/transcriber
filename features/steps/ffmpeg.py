from behave import *


@given(u'we have a file named "test.mp3"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given we have a file named "test.mp3"')


@when(u'we run format command to type "flac"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we run format command to type "flac"')


@then(u'we get a file named "test2.flac"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then we get a file named "test2.flac"')