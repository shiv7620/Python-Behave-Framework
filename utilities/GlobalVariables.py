import enum
import os
import json


envConfig = None
projectPath = None

# Enable only API testing in framework - To be enhanced to programmatically manage driver
SuiteType = "API" # or "UI" (any)


def load_settings():

    global envConfig, projectPath, SuiteType

    projectPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    with open(os.path.join(projectPath, 'resources/QAEnvironments.json')) as f:
        envConfig = json.load(f)


load_settings()
