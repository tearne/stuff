#!/bin/bash

WORD="DIR"
TXT_FILE="wordcount.sh"
OUT_FILE="result.txt"

if [ -z "${JOB_DIR}" ]; then
  echo "JOB_DIR not set."
  exit 1
fi
cd $JOB_DIR

if [ -z "${S3_JOB_DIR}" ]; then
  usage "S3_JOB_DIR not set, unable to determine S3 location to download job."
fi
OUT_PATH="${S3_JOB_DIR}/${AWS_BATCH_JQ_NAME}_${AWS_BATCH_JOB_ID}"

grep -o "$WORD" $TXT_FILE | grep -c "$WORD" >> $OUT_FILE

echo "results upload path = $OUT_PATH"
aws s3 cp $OUT_FILE $OUT_PATH/$OUT_FILE
