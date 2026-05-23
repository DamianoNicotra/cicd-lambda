import json
import os
import datetime

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            'message': 'CI/CD pipeline working!',
            'timestamp': datetime.datetime.utcnow().isoformat(),
            'environment': os.environ.get('ENVIRONMENT', 'dev')
        })
    }
