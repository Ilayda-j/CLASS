###Autogenerated code from internal Makefile
### Sourced from file: Apps/ui_nbs/BasicInteractionApp.ipynb

#| to_script
# Import the needed components
from ai_classroom_suite.UIBaseComponents import *
from ai_classroom_suite.BasicInteraction import *
from ai_classroom_suite.BasicInteraction import BasicInteractionDemo

# Launch the relevant component
BasicInteractionDemo.queue().launch(server_name='0.0.0.0', server_port=7860, show_error=True)
