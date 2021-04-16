# Virtual Environment
"""It is an environment which is and works the same as the python system interpreter but is isolated from the
    the rest of the environments on the system. It helps in keeping all the modules installed for a particular
    environment and their proper versions safe for future use.

    INSTALL: pip install virtualenv
    CREATE NEW VE: virtualenv myProjectEnvName
    ACTIVATE: .\myProjectEnvName\Scripts\activate.ps1
    DEACTIVATE: deactivate"""


'''1. 'pip freeze' command: returns all the packages installed in the virtual env along with their versions
   2. 'pip freeze > requirements.txt' command saves the output of pip freeze in a file named requirements.txt 
        and saves it in the same directory.
   3. Anyone can take this requirements.txt file and recreate the environment using the command
      'pip install -r requirements.txt' '''
