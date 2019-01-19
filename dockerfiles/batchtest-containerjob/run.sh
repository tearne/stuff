#!/bin/bash

S3_UPLOAD_DIR=${1}
MY_APPLICATION="stage/bin/main"

if [ -z "${S3_UPLOAD_DIR}" ]; then
  echo "S3_UPLOAD_DIR not set."
  exit 1
fi

echo "running: $MY_APPLICATION"
$MY_APPLICATION

echo "Uploading results to $S3_UPLOAD_DIR"
aws s3 cp out.txt $S3_UPLOAD_DIR/$OUT_FILE
