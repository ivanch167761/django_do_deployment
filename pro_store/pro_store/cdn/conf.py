import os



AWS_ACCESS_KEY_ID=os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME='deeptest'
AWS_S3_ENDPOINT_URL="https://ams3.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETERS = {
        "CacheControl": "max-age=86400",
        "ACL": "public-read"
        }
AWS_LOCATION = "https://deeptest.ams3.digitaloceanspaces.com"
DEFAULT_FILE_STORAGE="pro_store.cdn.backends.MediaRootS3BotoStorage"
STATICFILES_STORAGE="pro_store.cdn.backends.StaticRootS3BotoStorage"
