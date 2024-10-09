import boto3
import json
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Flag to enable mock responses
USE_MOCK = False  # Set to True to use mock responses

def generate_text(prompt):
    try:
        # Initialize boto3 session (uses the active credentials)
        session = boto3.Session()
        client = session.client('bedrock-runtime', region_name='us-east-1')  # Replace with your region

        response = client.invoke_model(
            modelId='amazon.titan-text-lite-v1',  # Changed from ModelId to modelId
            body=json.dumps({"inputText": prompt}),  # Changed from Body to body and adjusted the input format
            contentType='application/json',  # Changed from ContentType to contentType
            accept='application/json'  # Added accept parameter
        )

        response_body = json.loads(response['body'].read())
        return response_body.get('results', [{}])[0].get('outputText', 'No response from model.')

    except NoCredentialsError:
        return "AWS credentials not found. Please configure your credentials."
    except PartialCredentialsError:
        return "Incomplete AWS credentials. Please check your configuration."
    except client.exceptions.AccessDeniedException:
        return "Access Denied: You don't have permission to access this model."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

def get_mock_response(user_input):
    # Define mock responses
    sample_responses = {
        "Hello": "Hi there! How can I assist you with Valorant today?",
        "What is Valorant?": "Valorant is a tactical first-person shooter developed by Riot Games.",
        "Thank you": "You're welcome! Feel free to ask me anything about Valorant.",
        # Add more sample interactions as needed
    }
    return sample_responses.get(user_input.strip(), "I'm sorry, I don't understand that. Can you please rephrase?")