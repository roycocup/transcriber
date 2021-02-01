from behave import *
from features.steps.utils import *
from libs import bucket
from libs import gfiles
import os

@given(u'we have a client')
def step_impl(context):
    b = bucket.Bucket()
    assert(b is not None)
    

@when(u'when we create a bucket named "{bucket_name}"')
def step_impl(context, bucket_name):
    try:
        create_test_bucket(bucket_name)
    except Exception as error:
        print("Bucket probably already exists - ", error)
    

@then(u'the bucket "{bucket_name}" exists')
def step_impl(context, bucket_name):
    if not find_bucket(bucket_name): 
        raise Exception(u'Bucket {bucket_name} not found')
    delete_test_bucket(bucket_name)


def find_bucket(bucket_name):
    found = False
    for bucket in get_all_buckets():
        if bucket.name == bucket_name:
            return True
    return False


@given(u'we have a bucket named "{bucket_name}"')
def step_impl(context, bucket_name):
    context.bucket_name = bucket_name
    try:
        create_test_bucket(bucket_name)
    except:
        pass


@when(u'we delete the bucket named "{bucket_name}"')
def step_impl(context, bucket_name):
    delete_test_bucket(bucket_name)


@then(u'the bucket "{bucket_name}" does not exist')
def step_impl(context,bucket_name):
    if find_bucket(bucket_name):
        raise Exception(f'bucket {bucket_name} still exists') 
    
@given(u'the bucket "{bucket_name}" does not exist')
def step_impl(context, bucket_name):
    if find_bucket(bucket_name):
        raise Exception(f'bucket {bucket_name} still exists') 


@when(u'we upload a file named "{file_name}" to "{bucket_name}"')
def step_impl(context, file_name, bucket_name):
    create_test_file(file_name)
    gfile = gfiles.GFiles(bucket_name)
    context.response = gfile.upload(file_name)


@then(u'the file "{file_name}" exists on "{bucket_name}"')
def step_impl(context, file_name, bucket_name):
    gfile = gfiles.GFiles(bucket_name)
    stored_file = gfile.get_file_by_name(file_name)
    delete_test_file(file_name)
    delete_test_bucket(bucket_name)
    if not stored_file:
        raise Exception('File is not present')



@given(u'we have a file named "{file_name}" exists in "{bucket_name}"')
def step_impl(context, file_name, bucket_name):
    create_test_bucket(bucket_name)
    create_test_file(file_name)
    gfile = gfiles.GFiles(bucket_name)
    gfile.upload(file_name)


@when(u'we delete the file named "{file_name}" in "{bucket_name}"')
def step_impl(context, file_name, bucket_name):
    gfile = gfiles.GFiles(bucket_name)
    gfile.delete(file_name)


@then(u'the file "{file_name}" does not exist on "{bucket_name}"')
def step_impl(context, file_name, bucket_name):
    gfile = gfiles.GFiles(bucket_name)
    try:
        found = gfile.get_file_by_name(file_name)
        if found: raise FileExistsError("File should not exist in bucket but does")
    except:
        pass
    delete_test_file(file_name)
    delete_test_bucket(bucket_name)
    
    
@then(u'the uri for the file is "{uri}"')
def step_impl(context, uri):
    delete_test_bucket(context.bucket_name)
    if context.response is None:
        raise Exception("Response should not be empty")
    link = "gs://" + context.response.bucket.name + "/" + context.response.name
    if link != uri:
        raise Exception("Expected " + uri + " but got " + link)