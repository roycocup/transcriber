from behave import *
import os
import shutil
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
    
@given(u'we have a file "{file_name}" with "{num_channels}" channels')
def step_impl(context, file_name, num_channels):
    context.file_name = file_name
    if not os.path.isfile(file_name): raise FileNotFoundError()
    res_num_channels = af.Audioformatter(context.file_name).probe_channels()
    if res_num_channels != num_channels: raise Exception("Incorrect number of channels")


@when(u'we run a format command to make channels "{num_channels}"')
def step_impl(context, num_channels):
    # make a duplicate file for testing
    context.fake_file_name = "fake-"+context.file_name
    shutil.copy(src=context.file_name, dst=context.fake_file_name)
    af.Audioformatter(context.fake_file_name).change_channels(num_channels)
    


@then(u'we have a file "{file_name}" with "{num_channels}" channels')
def step_impl(context, file_name, num_channels):
    if not os.path.isfile(context.fake_file_name): raise FileNotFoundError()
    res_num_channels = af.Audioformatter(context.fake_file_name).probe_channels()
    os.remove(context.fake_file_name)
    if res_num_channels != num_channels: raise Exception("Incorrect number of channels")
