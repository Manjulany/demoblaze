from behave import *
from features.pages.SignupPage import SignupPage


@given(u'clicks on the Sing up button')
def click_open_signup(context):
    context.signin_page = SignupPage(context.driver)
    context.signin_page.click_on_signup()


@when(u'fills in the Username and Password')
def fill_in_signup_info(context):
    context.signin_page.enter_singup_credential()


@then(u'user clicks on the Sign up button')
def complete_signup(context):
    context.signin_page.click_signup_submit()


@then(u'new user is created')
def verify_singup(context):
    context.signin_page.verify_alert()
