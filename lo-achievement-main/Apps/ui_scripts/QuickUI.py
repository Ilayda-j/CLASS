###Autogenerated code from internal Makefile
### Sourced from file: Apps/ui_nbs/QuickUI.ipynb

#| to_script

import os
import openai
import gradio as gr
import pandas as pd
#| to_script

# The OpenAI API key provided by the instructor
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Instructor's prompt (invisible to students)
instructor_prompt = os.environ.get("SECRET_PROMPT")
#| to_script

# Adds a message from the user to the conversation history
def add_user_message(msg, history, messages):
    messages.append({"role": "user", "content": msg})
    return "", history + [[msg, None]], messages

# Generate a response from the chatbot
def get_tutor_reply(history, messages):
    completion = openai.chat.completions.create( 
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=150 # Change this 
    ) 
    # Extract the model's reply
    reply = completion.choices[0].message.content 
    # Updates the conversation history with the chatbot's response
    history[-1][1] = reply
    messages.append({"role": "assistant", "content": reply})
    return history, messages
#| to_script

# Saves the conversation history to a JSON file.
def save_chat_to_json(history):
    formatted_convo = pd.DataFrame(history, columns=['user', 'chatbot'])
    output_fname = f'tutoring_conversation.json'
    formatted_convo.to_json(output_fname, orient='records')
    return gr.update(value=output_fname, visible=True)
#| to_script

### User Interfaces ###
with gr.Blocks() as SimpleChat:
    gr.Markdown("""
        ## Chat with A Tutor
        Description here
        """)
    
    # Initialize the model with system message given by the instructor prompt
    system_msg = [{"role": "system", "content":  instructor_prompt}]
    messages = gr.JSON(visible=False, value = system_msg)
    
    with gr.Group():
        chatbot = gr.Chatbot(label="Simple Tutor")
        with gr.Row(equal_height=True):
            user_chat_input = gr.Textbox(show_label=False, scale=9)
            submit_btn = gr.Button("Enter", scale=1)
    with gr.Group():
        export_dialogue_button_json = gr.Button("Export your chat history as a .json file")
        file_download = gr.Files(label="Download here", file_types=['.json'], visible=False)
    
    # User submits a message by either click the submit button or press enter on keyboard
    submit_btn.click(
        fn=add_user_message, inputs=[user_chat_input, chatbot, messages], outputs=[user_chat_input, chatbot, messages], queue=False
    ).then(
        fn=get_tutor_reply, inputs=[chatbot, messages], outputs=[chatbot, messages], queue=True
    )
    user_chat_input.submit(
        fn=add_user_message, inputs=[user_chat_input, chatbot, messages], outputs=[user_chat_input, chatbot, messages], queue=False
    ).then(
        fn=get_tutor_reply, inputs=[chatbot, messages], outputs=[chatbot, messages], queue=True
    )
    export_dialogue_button_json.click(save_chat_to_json, chatbot, file_download, show_progress=True)
#| to_script
SimpleChat.queue().launch(server_name='0.0.0.0', server_port=7860)
