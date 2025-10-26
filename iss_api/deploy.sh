gcloud functions deploy iss-position-api \
    --gen2 \
    --runtime python311 \
    --region us-west2 \
    --source . \
    --entry-point get_iss_position \
    --trigger-http \
    --allow-unauthenticated \
    --memory 256Mi