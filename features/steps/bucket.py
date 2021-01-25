from behave import *
from libs import bucket

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