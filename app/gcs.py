import datetime
from flask import Flask, render_template
from google.cloud import storage

app = Flask(__name__)

# Initialize GCS Client (It will look for GOOGLE_APPLICATION_CREDENTIALS env var)
storage_client = storage.Client()
BUCKET_NAME = 'your-private-bucket-name'

def get_gcs_url(blob_name):
    """Generates a short-lived signed URL for a private GCS object."""
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(blob_name)

    url = blob.generate_signed_url(
        version="v4",
        expiration=datetime.timedelta(minutes=15),  # URL expires in 15 mins
        method="GET",
    )
    return url

# Register it so you can use it in your HTML like url_for
@app.context_processor
def utility_processor():
    return dict(gcs_url=get_gcs_url)