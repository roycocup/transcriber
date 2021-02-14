from behave import *
import os
from libs import audioformatter as af

@given(u'we have a test file named "{file_name}"')
def step_impl(context, file_name):
    # because we need this to be an actual audio file, I'm going to use one in the root directory
    context.file_name = file_name
    if not os.path.isfile(file_name):
        raise FileNotFoundError(f"Testing file does not exist. Please create {context.file_name}")
    

@when(u'we run format command to type "{file_type}"')
def step_impl(context, file_type):
    context.file_type = file_type
    af.Audioformatter(context.file_name).format_to(file_type)

@then(u'we get a file named "{file_name}"')
def step_impl(context, file_name):
    if not os.path.isfile(file_name):
        raise FileNotFoundError("File was not created")
    else:
        os.remove(file_name)
    
@given(u'we have a file "test2.flac" with "2" channels')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given we have a file "test2.flac" with "2" channels')


@when(u'we run a format command to make channels "1"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we run a format command to make channels "1"')


@then(u'we have a file "test2.flac" with "1" channels')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then we have a file "test2.flac" with "1" channels')
