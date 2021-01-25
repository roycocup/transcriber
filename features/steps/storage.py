from behave import *
from libs import bucket
from libs import gfiles
import os

sut = bucket.Bucket()

@given(u'we have a client')
def step_impl(context):
    assert(sut is not None)
    

@when(u'when we create a bucket named "{bucket_name}"')
def step_impl(context, bucket_name):
    sut.create_bucket(bucket_name)
    

@then(u'the bucket "{bucket_name}" exists')
def step_impl(context, bucket_name):
    if not find_bucket(bucket_name): 
        raise Exception(u'Bucket {bucket_name} not found')
    sut.delete_bucket(bucket_name)


def find_bucket(bucket_name):
    found = False
    for bucket in sut.get_all_buckets():
        if bucket.name == bucket_name:
            return True
    return False


@given(u'we have a bucket named "{bucket_name}"')
def step_impl(context, bucket_name):
    sut.create_bucket(bucket_name)


@when(u'we delete the bucket named "{bucket_name}"')
def step_impl(context, bucket_name):
    sut.delete_bucket(bucket_name)


@then(u'the bucket "{bucket_name}" does not exist')
def step_impl(context,bucket_name):
    if find_bucket(bucket_name):
        raise Exception(f'bucket {bucket_name} still exists') 
    
@given(u'the bucket "{bucket_name}" does not exist')
def step_impl(context, bucket_name):
    if find_bucket(bucket_name):
        raise Exception(f'bucket {bucket_name} still exists') 


def _create_test_file(filename):
    with open(filename, 'w') as f:
        text_str = "Lorem in exercitation nisi veniam quis elit cupidatat consequat commodo."
        f.write(text_str)
    
def _delete_test_file(filename):
    if os.path.isfile(filename):
        os.remove(filename)

@when(u'we upload a file named "{file_name}" to "{bucket_name}"')
def step_impl(context, file_name, bucket_name):
    _create_test_file(file_name)
    gfile = gfiles.GFiles(bucket_name)
    gfile.upload(file_name)


@then(u'the file "{file_name}" exists on "{bucket_name}"')
def step_impl(context, file_name, bucket_name):
    gfile = gfiles.GFiles(bucket_name)
    stored_file = gfile.get_file_by_name(file_name)
    _delete_test_file(file_name)
    sut.delete_bucket(bucket_name)
    if not stored_file:
        raise Exception('File is not present')

