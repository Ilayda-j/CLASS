# **Duplication and Deployment Instructions for Huggingface Spaces** 

This README contains duplication and deployment instructions for CLAS applications deployed with Huggingface Spaces. These apps allow students to interact with a chatbot tutor which provides quiz questions, feedback, and academic guidance on the subject.  

After the conversation is over, a JSON file with chat history will be available for download. 

## **How to duplicate the Huggingface Space**

An instructor must duplicate a Space if they wish to build from an existing demo to make changes or incorporate specific environment variables. 

If you want to duplicate a Space, click the three dots at the top right of the space and click Duplicate this Space. Once you do this, you will be able to change the following attributes:

**Owner**: The duplicated Space can be under your account or any organization in which you have write access
**Space name**
**Visiblity**: The Space is private by default. Read more about private repositories here.
**Hardware**: You can choose the hardware on which the Space will be running. Read more about hardware upgrades here.
**Storage**: If the original repo uses persistent storage, you will be prompted to choose a storage tier. Read more about persistent storage here.
**Secrets and variables**: If the original repo has set some secrets and variables, you’ll be able to set them while duplicating the repo.

If the Space requires utilizes environment variables, the duplicate workflow will auto-populate the public Variables from the source Space, and give you a warning about setting up the Secrets. The duplicated Space will use a free CPU hardware by default, but you can later upgrade if needed.

## **How to manage Huggingface Secrets**

Repository Secrets store values including access tokens, API keys, or any sensitive value or credentials. Secrets are private and their value cannot be retrieved once set. They will not be added to Spaces duplicated from your repository. 

Commonly used secret variables may include "OPENAI_API_KEY", "SECRET_PROMPT", and "PIPLOC." Instructions for inputting values into these variables are below.

1. The input for the "OPENAI_API_KEY" secret can be the instructor's personal OpenAI API key. If you do not already have an API key, navigate to the API section of the OpenAI website. Click to generate a new API key and save this value in a secure location.
2. The input for "SECRET_PROMPT" includes the persona and prompt given to the chatbot tutor to guide its interaction with students.
3. The input for "PIPLOC" allows the app to access other files in the CLAS project. The input is a value in the following form: git+https://ghusername:ghpersonalaccesstoken@github.com/vanderbilt-data-science/lo-achievement.git with "ghusername" replaced by your personal Github username and "ghpersonalaccesstoken" replaced by your Github personal access token.
