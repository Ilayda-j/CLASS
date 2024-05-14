# Classroom Learning and Assessment Suite (CLAS)

The Classroom Learning and Assessment Suite is a set of AI-driven solutions that complement in-class learning with interactive study and assessment. Primarily ideated by faculty interested in leveraging AI platforms to enhance student learning, the suite creates new mechanisms for both students and faculty members in both supporting high quality learning assessments and streamlining grading of student submissions using generative AI-based platforms.

## Features
CLAS is suitable for users of diverse programming backgrounds - from no programming background to seasoned programmers. The Suite provides:

### **Prompting Guides**

* **[A curated prompt dictionary for self-study](https://github.com/vanderbilt-data-science/lo-achievement/wiki/Guide-to-Learning-Objective-Prompts)**: A set of prompts that have been engineering and evaluated on OpenAI GPT 3.5 and GPT4 to provide numerous types of assessments for students engaging in self-study with instructor provided materials
* **A curated prompt dictionary for student assessment**: Prompts targeted primarily towards instructors who want a generalized rubric for evaluating student submissions

### **Interface-Driven Programs**
No programming experience? No problem. 

* **[Student self-study using instructor assigned resources](https://huggingface.co/spaces/vanderbilt-dsi/selfstudy_learningobjectives_demo)**: A point-and-click interface with OpenAI generative AI. Upload your contextual coursework (book chapters, etc), and chat with your own customized tutor!
* **Hosted self- and in-class oral exam app**: Interested in using oral exams for assessment of student knowledge? Students - want to prepare for oral exams? Visit our point-and-click interface with OpenAI generative AI using your own coursework. You can upload questions provided by the instructor or ask the generative AI to assist in creating questions for you.

### **Customizable Tutoring Programs**
Ideated by Jesse Blocher (Ph.D.)

* **[Basic Interaction Exercise](https://huggingface.co/spaces/vanderbilt-dsi/clas-basic-interaction-app)**: The Basic Interaction Exercise is web-based Chat interface that allows students to interact with a chatbot tutor using instructor-designed prompts that are not visible to students. This is designed to get students to reflect on a recent project experience or in-class exercise.
* **Simulated Interaction: case study or client interaction**: The interface will embody a persona for students to  interact with, such as a client with a problem to be solved or a case study to examine. The goal is for students to gather information and provide recommendations, creating a dynamic learning experience.
* **Reading the Book**: This interface empowers students to independently study various texts, from poems to book chapters. Students simply upload a text PDF, and our AI chatbot engages you with insightful questions, offering constructive feedback.
* **Reading Quiz**: Teachers simply upload a text PDF, and our AI chatbot engages you with insightful questions, offering constructive feedback.

### **Google Colab Notebooks**
Want to evaluate students or want to customize your approach for interacting with generative AI?

* **[Instructor Grading Notebook](https://github.com/vanderbilt-data-science/lo-achievement/blob/main/instructor_intr_notebook.ipynb)**: Upload a zip file of the JSON output of your students' exploration and assessment, and get insight on student strengths and weaknesses on the topic as well as structured feedback for all students.
* **[Instructor Document Store Creation](https://github.com/vanderbilt-data-science/lo-achievement/blob/main/instructor_vector_store_creator.ipynb)**: Store all of your classroom content (pdfs, Youtube videos, website links) in a hosted location for easy accessibility for students working with generative AI platforms.
* **[Prompting with Inline Context](https://github.com/vanderbilt-data-science/lo-achievement/blob/main/prompt_with_context.ipynb)**: A customizable, programmatic way to interface with generative AI using Google Colab through direct copy/paste of text content
* **[Prompting with Vector Stores](https://github.com/vanderbilt-data-science/lo-achievement/blob/main/prompt_with_vector_store.ipynb)**: A customizable, programming way for self-study with generative AI using Google Colab through the creation of vector stores (better for larger corpuses of text)

**Use the repo!**
You can also directly clone/use the repo itself or use it as a package for development - this is great for experienced programmers or even those who would like to learn more about development with generative AI. The repo provides:
- Generative AI and LangChain integration to process sources and create assessments and answer keys
- Runs on Google Colab, with no additional installations needed
You can also develop locally as desired and we encourage PR contributions from the community!

## Getting Started

There are a variety of ways to use CLAS:
* **Navigate to the Wiki to explore prompts.** You can copy/paste/amend these in the interfaces provided by OpenAI, Google, Anthropic, etc.
* **Use Google Colab to interact with notebooks.** Click on the notebook you'd like to enter in the files list above. You will see a blue Open In Colab link in the page that opens. Click this button to start your session in Google Colab, making sure that you're logged in with your Google Account.** It will take a few minutes to spin up and automatically install the required packages.
* **Study through our hosted app.** Navigate to [CLAS on Huggingface](https://huggingface.co/spaces/vanderbilt-dsi/clas-basic-interaction-app). Follow the instructions to use the platform for self study.

## Contributing

To contribute to the project, please fork the repository and submit a pull request. Our community is supportive, and we provide training and classes if you're new to any of the frameworks used in the project. Everyone is welcome to contribute, as we believe participating in data science and AI projects is an excellent way to learn.

## Community Guidelines

We aim to create a welcoming and inclusive community where everyone can feel comfortable and valued, regardless of skill level, background, ability, or identity. To ensure a positive atmosphere, please adhere to our code of conduct and community guidelines.

## Meetings

- Sprint Planning & Retrospective: Mondays and Fridays at 10:30 am
- Demos: Fridays at 3 pm

## Additional Resources

- LangChain documentation
- Introduction to transformers and generative AI on our [YouTube channel](https://www.youtube.com/channel/UC8C2_3L5gR9qLmL7rmb2BdQ)
- AI Summer and AI Winter sessions (free and open to all)

## Reporting Issues

If you encounter a bug, please submit an issue and label it with "Bug." To escalate the issue, email [datascience@vanderbilt.edu](mailto:datascience@vanderbilt.edu).

## Contact Information

- Organization: Data Science Institute at Vanderbilt University
- Program: Data Science for Social Good
- Main Email: [datascience@vanderbilt.edu](mailto:datascience@vanderbilt.edu)
- Principal Investigators (PIs)
  - Jesse Spencer-Smith, Ph.D., Chief Data Scientist, Data Science Institute, Vanderbilt University
  - Jesse Blocher, Ph.D., Director of Graduate Studies, Data Science Institute, Vanderbilt University
  - Dr. Yaa Kumah-Crystal, Ph.D., Pediatric Endocrinologist and Professor, Vanderbilt University Medical Center
  - Charreau Bell, Ph.D., Senior Data Scientist, Data Science Institute, Vanderbilt University
- Staff Lead: [charreau.s.bell@vanderbilt.edu](mailto:charreau.s.bell@vanderbilt.edu)
- Project Manager (Fall 2023):
  - Catherine Dang, Undergraduate Student, Economics and Data Science, Vanderbilt University
- Code Developers (Fall 2023):
  - Chenyu Miao, Graduate Student, Data Science, Vanderbilt University
  - Yurui Xu, Undergraduate Student, Computer Science and Math, Vanderbilt University
  - Ilayda Koca, Undergraduate Student, Computer Science, Vanderbilt University
  - Lily Hofstetter, Computer Science and Cognitive Science, Undergraduate Student, Vanderbilt University
- Code Developers (past):
  - Katrina Rbeiz, Ph.D. Student, Psychology, Vanderbilt University
  - Minwoo Sohn, Graduate Student, Data Science, Vanderbilt University
  - Ricky Sun, Graduate Student, Data Science, Vanderbilt University
  - Eleanor Beers, Graduate Student, Data Science, Vanderbilt University
  - Kevin Chen, Undergraduate, Computer Science, Vanderbilt University
  - Adam Levav, Undergraduate, University of Maryland
  - Varun Koduvayur, Undergraduate
