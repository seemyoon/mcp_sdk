import json
import gradio as gr

from textblob import TextBlob


def sentiment_analysis(text: str) -> str:
    """
    Analyze the sentiment of the given text.

    Args:
        text (str): The text to analyze

    Returns:
        str: A JSON string containing polarity, subjectivity, and assessment
    """
    blob = TextBlob(text)
    # TextBlob uses models under the hood, but TextBlob itself is not a model. It’s more like a wrapper or toolbox that makes it easy to use language models without writing complex code.
    sentiment = blob.sentiment

    result = {
        "polarity": round(sentiment.polarity, 2),  # -1 (negative) to 1 (positive)
        "subjectivity": round(sentiment.subjectivity, 2),  # 0 (objective) to 1 (subjective)
        "assessment": 'positive' if sentiment.polarity > 0 else "negative" if sentiment.polarity < 0 else 'neutral'
    }

    return json.dumps(result)


# Create the Gradio interface
demo = gr.Interface(
    fn=sentiment_analysis,
    inputs=gr.Textbox(placeholder="enter text to analyze..."),
    outputs=gr.Textbox(),  # Changed from gr.JSON() to gr.Textbox()
    title='text sentiment analysis',
    description='analyze the sentiment of text using TextBlob'
)

if __name__ == '__main__':
    demo.launch(mcp_server=True)
