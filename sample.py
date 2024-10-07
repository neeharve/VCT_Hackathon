import boto3
import json

# Initialize the Bedrock Runtime client with a specific profile
client = boto3.client('bedrock-runtime', region_name='us-east-1')

def generate_text(prompt):
    body = json.dumps({
        "inputText": prompt,
        "textGenerationConfig": {
            "maxTokenCount": 100,
            "stopSequences": [],
            "temperature": 0.7,
            "topP": 1
        }
    })

    try:
        response = client.invoke_model(
            modelId='amazon.titan-text-lite-v1',
            body=body,
            contentType='application/json',
            accept='application/json'
        )
        response_body = json.loads(response['body'].read())
        print("Full response:", response_body)  # Add this line for debugging

        return response_body['results'][0]['outputText']
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
    
# Testing with a basic prompt 
# prompt = "Give me an overview of the Valorant Champions Tour"
# result = generate_text(prompt)
# if result:
#     print("Generated text:")
#     print(result)
# else:
#     print("Failed to generate text from the model.")

prompt = "Who are the top Valorant players?"
result = generate_text(prompt)
if result:
    print("Generated text:")
    print(result)
else:
    print("Failed to generate text from the model.")