import pandas as pd
from queries import description_query
from main import execute_gql_query, get_graphql_client
from transformers import pipeline

task = "question-answeringn"
model = "distilbert-base-cased-distilled-squad"
question_answerer = pipeline(task, model=model)

gql_client = get_graphql_client()
description_response = execute_gql_query(client=gql_client, query=description_query)
df = pd.DataFrame(description_response['rekts'])

conversation = '''Jeff: Can I train a 🤗 Transformers model on Amazon SageMaker? 
Philipp: Sure you can use the new Hugging Face Deep Learning Container. 
Jeff: ok.
Jeff: and how can I get started? 
Jeff: where can I find documentation? 
Philipp: ok, ok you can find everything here. https://huggingface.co/blog/the-partnership-amazon-sagemaker-and-hugging-face                                           
'''

response_summary = question_answerer(conversation)
summary = response_summary[0]['summary_text']
