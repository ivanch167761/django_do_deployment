from storages.backends.s3boto3 import S3Boto3Storage
import os
import ssl

class StaticRootS3BotoStorage(S3Boto3Storage):
    ssl._create_default_https_context = ssl._create_unverified_context
    if os.environ.get("DEV") != 1:
        location = "static"
    else:
        location = "static_dev"
class MediaRootS3BotoStorage(S3Boto3Storage):
    ssl._create_default_https_context = ssl._create_unverified_context
    if os.environ.get("DEV") != 1:
        location = "media"
    else:
        location = "media_dev"
