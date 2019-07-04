from behave import given, then

from pageObjects.login import Login

loginPage = Login.get_instance()

@given('User logs into application with "{user}" and "{passwd}"')
def step_impl(context, user, passwd):
    loginPage.mercuryLogin(user, passwd)


@then(u'User logs out from application')
def step_impl(context):
    loginPage.mercuryLogout()

