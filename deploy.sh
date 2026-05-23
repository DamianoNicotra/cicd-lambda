#!/bin/bash
set -e

echo "Deploying Lambda with SAM..."
sam deploy --stack-name cicd-lambda \
  --capabilities CAPABILITY_IAM \
  --guided
