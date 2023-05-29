import json
import CURD

print('Loading function')

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    print("ARN of Current function is: ",context.invoked_function_arn)
    
    keys = list(event.keys())
    print(keys)
    
    # based on the first key, this script decides which acction to be performed on dynamoddb
    if (event['type'] == "write"):
        CURD.WriteTable(keys[1], event[keys[1]])
        return {
        'status_code': 200,
        'body': json.dumps('Write opertion is Successful')
        }  
   