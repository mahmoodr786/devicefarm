import os

def lambda_handler(event, context):
    # Define the path to the HTML file
    file_path = os.path.join(os.path.dirname(__file__), 'index.html')
    
    # Load the HTML file content
    with open(file_path, 'r') as file:
        html_content = file.read()
    
    # Return the HTML content as a response
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html',
        },
        'body': html_content
    }
