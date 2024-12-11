# The Snowpark package is required for Python Worksheets. 
# You can add more packages by selecting them using the Packages control and then importing them.

import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col

# Load huggingface transformers lib
from transformers import pipeline


def main(session: snowpark.Session): 
    # This statement downloads the model to ~/.cache
    pipe = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-sentiment-latest")
    # Run the model on a statement
    result = pipe("I love PyCharm! It's my favorite Python IDE.")
    print(result)

    return result
