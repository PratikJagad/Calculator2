import json

def lambda_handler(event, context):

    data = json.loads(event['body'])
    if data['operation'] == 'sub':
        print("in subtraction")
        result = int(data['a']) - int(data['b'])
    elif data['operation'] == 'mul':
        print("in multiplication")
        result = int(data['a']) * int(data['b'])  
    elif data['operation'] == 'div':
        print("in division")
        if int(data['b']) == 0:
            result = "Division by zero is not allowed"
        else:
            result = int(data['a']) / int(data['b'])
    elif data['operation'] == 'add':
        print("in addition")
        result = int(data['a']) + int(data['b'])
    else:
        result = "Invalid operation"
    
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
