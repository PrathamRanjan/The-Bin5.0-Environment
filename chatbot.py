
from openai import OpenAI
from dash import html, dcc
from dash.dependencies import Input, Output,State

# Assuming you have imported 'app' from app.py which is the Dash instance
from app import app
import requests
api_key= "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"

# Define the layout for the chatbot page
layout = html.Div([
    html.H2(" Sustainability Chatbot", className="chatbot-header"),
    dcc.Textarea(
        id='chat-history',
        className='chat-history',
        value='Start a conversation with the bot...',
        readOnly=True,
        style={'width': '100%', 'height': '300px'}
    ),
    html.Div([
        dcc.Input(
            id='chat-input',
            className='chat-input',
            type='text',
            placeholder='Type your message here...',
            style={'width': '90%', 'margin-right': '10px'}
        ),
        html.Button('Send', id='send-button', n_clicks=0)
    ], className='input-group')
], className='chatbot-container')
@app.callback(
    [Output('chat-history', 'value'), Output('chat-input', 'value')],
    [Input('send-button', 'n_clicks')],
    [State('chat-input', 'value'), State('chat-history', 'value')]
)
def update_chat(n_clicks, user_input, chat_history):
    if n_clicks > 0 and user_input:
        payload = {
            "model": "gpt-3.5-turbo-instruct",
            "prompt": f"Based on {user_input} generate a suitable response while keeping in mind sustainability and responsible recycling, for questions unrelated to sustainability, recycling, environmental and personal care please response with please ask me questions related to the topic",
            "temperature": 0.5,
            "max_tokens": 150
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"  # Ensure this is the correct key
        }

        try:
            response = requests.post("https://api.openai.com/v1/completions", headers=headers, json=payload)
            response.raise_for_status()  # This will raise an error for bad status
            response_data = response.json()
            answer = response_data['choices'][0]['text']
            new_chat_history = f"{chat_history}\nUser: {user_input}\nBot: {answer.strip()}\n"
        except requests.exceptions.RequestException as e:
            answer = "Sorry, I am unable to respond at this moment."
            new_chat_history = f"{chat_history}\nUser: {user_input}\nBot: {answer}\n"

        return new_chat_history, ''  
    return chat_history, user_input


