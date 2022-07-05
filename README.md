# serverless-python-dynamodb
CRUD example with serverless, DynamoDB and Python Lambda
We are using serverless architecture to create AWS Lambda and API Gateway. 
Four different Apis are created that perform CRUD operations to DynamoDB table.

Steps to Run 
1. Using below command, configure your AWS keys.
   aws configure
2. Using below command deploy this to AWS.
    serverless deploy
3. Test using curl commands.
    1. Create employee 
   `curl -X POST https://XXXXXXX.execute-api.us-east-1.amazonaws.com/employee 
    --data '{
    "name": "Suresh Mehta",
    "designation":"Admin",
    "phonenumber": "1234536"
     }' -H "Content-Type: application/json"`
    2. List all employees
`       curl https://XXXXXXX.execute-api.us-east-1.amazonaws.com/employee
    3. Replace the <id> part with a real id from your employee table
         curl https://XXXXXXX.execute-api.us-east-1.amazonaws.com/employee/<id>
    4. Update employee 
        # Replace the <id> part with a real id from your employee table
        curl -X PUT https://XXXXXXX.execute-api.us-east-1.amazonaws.com/employee/<id> --data '{
       "name": "Suresh Mehta",
       "designation":"Admin",
        "phonenumber": "1234536"
       }' -H "Content-Type: application/json"
    5. Delete employee
        # Replace the <id> part with a real id from your employee table
        curl -X DELETE https://XXXXXXX.execute-api.us-east-1.amazonaws.com/employee/<id>
    6. Added github actions to deploy to cloudfront. check .github actions folder
`

