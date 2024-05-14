# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/prompt_interaction_base.ipynb.

# %% auto 0
__all__ = ['SYSTEM_TUTOR_TEMPLATE', 'HUMAN_RESPONSE_TEMPLATE', 'HUMAN_RETRIEVER_RESPONSE_TEMPLATE', 'DEFAULT_ASSESSMENT_MSG',
           'DEFAULT_LEARNING_OBJS_MSG', 'DEFAULT_CONDENSE_PROMPT_TEMPLATE', 'DEFAULT_QUESTION_PROMPT_TEMPLATE',
           'DEFAULT_COMBINE_PROMPT_TEMPLATE', 'create_model', 'set_openai_key', 'create_base_tutoring_prompt',
           'get_tutoring_prompt', 'get_tutoring_answer', 'create_tutor_mdl_chain', 'get_direct_answer',
           'update_conversation_history']

# %% ../nbs/prompt_interaction_base.ipynb 3
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI

from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chains import LLMChain, ConversationalRetrievalChain, RetrievalQAWithSourcesChain
from langchain.chains.base import Chain
from langchain.schema.messages import SystemMessage, HumanMessage
from langchain.prompts.chat import ChatPromptValue

from getpass import getpass

import os

# %% ../nbs/prompt_interaction_base.ipynb 6
def create_model(openai_mdl='gpt-3.5-turbo-16k', temperature=0.1, **chatopenai_kwargs):
    llm = ChatOpenAI(model_name = openai_mdl, temperature=temperature, **chatopenai_kwargs)

    return llm

# %% ../nbs/prompt_interaction_base.ipynb 7
def set_openai_key():
    os.environ["OPENAI_API_KEY"] = getpass()

    return

# %% ../nbs/prompt_interaction_base.ipynb 11
# Create system prompt template
SYSTEM_TUTOR_TEMPLATE = ("You are a world-class tutor helping students to perform better on oral and written exams though interactive experiences. " +
                         "When assessing and evaluating students, you always ask one question at a time, and wait for the student's response before " +
                         "providing them with feedback. Asking one question at a time, waiting for the student's response, and then commenting " +
                         "on the strengths and weaknesses of their responses (when appropriate) is what makes you such a sought-after, world-class tutor.")

# Create a human response template
HUMAN_RESPONSE_TEMPLATE = ("I'm trying to better understand the text provided below. {assessment_request} The learning objectives to be assessed are: " +
                           "{learning_objectives}. Although I may request more than one assessment question, you should " +
                           "only provide ONE question in you initial response. Do not include the answer in your response. " +
                           "If I get an answer wrong, provide me with an explanation of why it was incorrect, and then give me additional " +
                           "chances to respond until I get the correct choice. Explain why the correct choice is right. " +
                           "The text that you will base your questions on is as follows: {context}.")

HUMAN_RETRIEVER_RESPONSE_TEMPLATE = ("I want to master the topics based on the excerpts of the text below. Given the following extracted text from long documents, {assessment_request} The learning objectives to be assessed are: " +
                           "{learning_objectives}. Although I may request more than one assessment question, you should " +
                           "only provide ONE question in you initial response. Do not include the answer in your response. " +
                           "If I get an answer wrong, provide me with an explanation of why it was incorrect, and then give me additional " +
                           "chances to respond until I get the correct choice. Explain why the correct choice is right. " +
                           "The extracted text from long documents are as follows: {summaries}.")

def create_base_tutoring_prompt(system_prompt=None, human_prompt=None):

    #setup defaults using defined values
    if system_prompt == None:
        system_prompt = PromptTemplate(template = SYSTEM_TUTOR_TEMPLATE,
                          input_variables = [])
    
    if human_prompt==None:
        human_prompt = PromptTemplate(template = HUMAN_RESPONSE_TEMPLATE,
                           input_variables=['assessment_request', 'learning_objectives', 'context'])

    # Create prompt messages
    system_tutor_msg = SystemMessagePromptTemplate(prompt=system_prompt)
    human_tutor_msg = HumanMessagePromptTemplate(prompt= human_prompt)

    # Create ChatPromptTemplate
    chat_prompt = ChatPromptTemplate.from_messages([system_tutor_msg, human_tutor_msg])

    return chat_prompt

# %% ../nbs/prompt_interaction_base.ipynb 15
DEFAULT_ASSESSMENT_MSG = 'Please design a 5 question short answer quiz about the provided text.'
DEFAULT_LEARNING_OBJS_MSG = 'Identify and comprehend the important topics and underlying messages and connections within the text'

def get_tutoring_prompt(context, chat_template=None, assessment_request = None, learning_objectives = None, **kwargs):

    # set defaults
    if chat_template is None:
        chat_template = create_base_tutoring_prompt()
    else:
        if not all([prompt_var in chat_template.input_variables
                    for prompt_var in ['context', 'assessment_request', 'learning_objectives']]):
            raise KeyError('''It looks like you may have a custom chat_template. Either include context, assessment_request, and learning objectives
                           as input variables or create your own tutoring prompt.''')

    if assessment_request is None and 'assessment_request':
        assessment_request = DEFAULT_ASSESSMENT_MSG
    
    if learning_objectives is None:
        learning_objectives = DEFAULT_LEARNING_OBJS_MSG
    
    # compose final prompt
    tutoring_prompt = chat_template.format_prompt(context=context,
                                                assessment_request = assessment_request,
                                                learning_objectives = learning_objectives,
                                                **kwargs)
    
    return tutoring_prompt


# %% ../nbs/prompt_interaction_base.ipynb 19
def get_tutoring_answer(context, tutor_mdl, chat_template=None,
                        assessment_request=None,
                        learning_objectives=None,
                        return_dict=False,
                        call_kwargs=None,
                        input_kwargs=None):
    
    if call_kwargs is None:
        call_kwargs = {}
    if input_kwargs is None:
        input_kwargs = {}
    
    # set defaults
    if assessment_request is None:
            assessment_request = DEFAULT_ASSESSMENT_MSG
    if learning_objectives is None:
        learning_objectives = DEFAULT_LEARNING_OBJS_MSG
    
    common_inputs = {'assessment_request':assessment_request, 'learning_objectives':learning_objectives}
    
    # get answer based on interaction type
    if isinstance(tutor_mdl, ChatOpenAI):
        human_ask_prompt = get_tutoring_prompt(context, chat_template, assessment_request, learning_objectives)
        tutor_answer = tutor_mdl(human_ask_prompt.to_messages())

        if not return_dict:
            final_answer = tutor_answer.content
    
    elif isinstance(tutor_mdl, Chain):
        if isinstance(tutor_mdl, RetrievalQAWithSourcesChain):
            if 'question' not in input_kwargs.keys():
                common_inputs['question'] = assessment_request
            final_inputs = {**common_inputs, **input_kwargs}
            
        elif isinstance(tutor_mdl, ConversationalRetrievalChain):
            if 'question' not in input_kwargs.keys() or not input_kwargs['question']:
                system_human_question = get_tutoring_prompt(context, chat_template, assessment_request, learning_objectives)
                question = [msg for msg in system_human_question.messages if isinstance(msg, HumanMessage)]
                question = question[0].content if question else question.to_string()
                input_kwargs['question'] = question

            if 'chat_history' not in input_kwargs.keys():
                input_kwargs['chat_history'] = []
            final_inputs = {**input_kwargs}
        else:
            common_inputs['context'] = context
            final_inputs = {**common_inputs, **input_kwargs}
         
        # get answer
        tutor_answer = tutor_mdl(final_inputs, **call_kwargs)
        final_answer = tutor_answer

        if not return_dict:
            final_answer = final_answer['answer']
    
    else:
        raise NotImplementedError(f"tutor_mdl of type {type(tutor_mdl)} is not supported.")

    return final_answer

# %% ../nbs/prompt_interaction_base.ipynb 20
DEFAULT_CONDENSE_PROMPT_TEMPLATE = ("Given the following conversation and a follow up message, combine the chat history and follow up message into " +
    "a concise standalone message in the original language. The created standalone message should: 1) Ensure that the overarching task and characteristics of the interaction are always contained in the summary. For example, "+
    "if the user asks that 5 questions should be asked, this instruction should always be in the summary until the 5 question task is completed. Additionally, if the instructions contain information "+
    "about your role - e.g., that you are an exceptional Socratic tutor and great at helping students better understand information, then this should also always be in the summary message, "+
    "2) concisely summarize the key points of the history of the conversation while taking into account the goal and of the follow up message, "+
    "3) provide suitable context from the conversation to inform the follow up message, and 4) be written in a way that emphasizes the new follow up message, " +
    "but again always keeping in mind any overarching tasks (until they are completed) and characteristics of the interaction. " + 
                                    "\n\nChat History:\n{chat_history}\nFollow Up message: {question}\nStandalone message:")

DEFAULT_QUESTION_PROMPT_TEMPLATE  = ("Use the following portion of a long document to see if any of the text is relevant to creating a response to the question." +
                                     "\nReturn any relevant text verbatim.\n{context}\nQuestion: {question}\nRelevant text, if any:")

DEFAULT_COMBINE_PROMPT_TEMPLATE = ("Given the following extracted parts of a long document and the given prompt, create a final answer with references ('SOURCES'). "+
                                   "If you don't have a response, just say that you are unable to come up with a response. "+
                                   "\nSOURCES:\n\nQUESTION: {question}\n=========\n{summaries}\n=========\nFINAL ANSWER:'")

def create_tutor_mdl_chain(kind='llm', mdl=None, prompt_template = None, **kwargs):
    
    #Validate parameters
    if mdl is None:
        mdl = create_model()
    kind = kind.lower()
    
    #Create model chain
    if kind == 'llm':
        if prompt_template is None:
            prompt_template = create_base_tutoring_prompt()
        mdl_chain = LLMChain(llm=mdl, prompt=prompt_template, **kwargs)
    elif kind == 'conversational':
        if prompt_template is None:
            prompt_template = PromptTemplate.from_template(DEFAULT_CONDENSE_PROMPT_TEMPLATE)
            prompt_template = create_base_tutoring_prompt(human_prompt=prompt_template)
        mdl_chain = ConversationalRetrievalChain.from_llm(mdl, condense_question_prompt = prompt_template, **kwargs)
        #mdl_chain = ConversationalRetrievalChain.from_llm(mdl, **kwargs)
    elif kind == 'retrieval_qa':
        if prompt_template is None:

            #Create custom human prompt to take in summaries
            human_prompt = PromptTemplate(template = HUMAN_RETRIEVER_RESPONSE_TEMPLATE,
                           input_variables=['assessment_request', 'learning_objectives', 'summaries'])
            prompt_template = create_base_tutoring_prompt(human_prompt=human_prompt)
            
        #Create the combination prompt and model
        question_template = PromptTemplate.from_template(DEFAULT_QUESTION_PROMPT_TEMPLATE)
        #mdl_chain = RetrievalQAWithSourcesChain.from_llm(llm=mdl, question_prompt=question_template, combine_prompt = prompt_template, **kwargs)
        mdl_chain = RetrievalQAWithSourcesChain.from_chain_type(llm=mdl, **kwargs)
    else:
        raise NotImplementedError(f"Model kind {kind} not implemented")
    
    return mdl_chain

# %% ../nbs/prompt_interaction_base.ipynb 24
def get_direct_answer(mdl, human_prompt=' ', system_prompt=' ', return_dict=False):

    # get answer based on interaction type
    if isinstance(mdl, ChatOpenAI):
        human_ask_prompt = ChatPromptValue(messages=[HumanMessage(content=human_prompt),
                                                       SystemMessage(content=system_prompt)])
        mdl_answer = mdl(human_ask_prompt.to_messages())

        if not return_dict:
            final_answer = mdl_answer.content

    else:
        raise NotImplementedError(f"mdl of type {type(mdl)} is not supported.")

    return final_answer

# %% ../nbs/prompt_interaction_base.ipynb 45
def update_conversation_history(chat_history, question, answer):
    chat_history.append((question, answer))

    return chat_history 