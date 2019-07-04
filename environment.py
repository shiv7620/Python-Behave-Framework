from utilities.GlobalVariables import envConfig, SuiteType
from pageObjects.application import app

# All these methods will be executed before or after feature and scenario

def before_feature(context, feature):
    print("Starting feature")

def before_all(context):
    print("Starting Framework")

def after_all(context):

    app.close_driver()

def before_scenario(context, scenario):

    print("Starting new scenario = ", scenario.name)

    if scenario.filename.find('features/ui/') >= 0:

        print("Scenario for UI Testing")
        app.load_website(envConfig['webAppURL'])

def after_scenario(context, scenario):

    print("Finishing Test = ", scenario.name)

