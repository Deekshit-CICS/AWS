import json
import boto3


# This program is used to invoke another lamnda function.
# Invoking function using SDK is called synchronus invocation
# boto3 is used for invocation of this lambda function
# Make sure to attach "awslambdainvocation" policy to the role attached to invocing lambda function, which is nothing but the function in which current code is executed

# Create a Boto3 lambda client

lambda_client = boto3.client('lambda')
print("Invoking another lambda function.......")
# Define the parameters for the Lambda invocations
function_name = "TestFun"   # TestFun is the function which already exists
payload = {'type' : "write",'key2' : "value2"}

# Invoke the lambda function


response = lambda_client.invoke(
    FunctionName=function_name,
    InvocationType='RequestResponse',
    Payload=json.dumps(payload)
    )

# Extract the response from the incvocations
response_payload = response['Payload'].read().decode('utf8')
print(response_payload)


# handler function, this name should be same as the one mentioned in your lambda function
def lambda_handler(event, context):  
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
