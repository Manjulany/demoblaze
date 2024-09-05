from behave import *
from features.pages.LoginPage import LoginPage
from features.pages.HomePage import HomePage
from features.pages.ProductPage import ProductPage
from features.pages.CartPage import CartPage
from features.pages.SignupPage import SignupPage


@given(u'the user logs into demoblaze and navigates to home page')
def login_open_homepage(context):
    context.signup = SignupPage(context)
    context.login_page = LoginPage(context.driver)
    context.login_page.click_on_signup()
    context.login_page.enter_login_credential()
    context.login_page.click_login_submit()


@when(u'user clicks open the product and add each product to the cart')
def add_product_cart(context):
    context.home_page = HomePage(context.driver)
    context.product_page = ProductPage(context.driver)
    # loop through until all the given add items from testdata json file is added
    for item in context.add_item:
        print("add item:", item)
        context.home_page.open_item(item)
        context.product_page.add_product_to_cart()
        context.home_page.click_on_home()


@then(u'verifies the cart for added products')
def verify_cart_products(context):
    context.cart_page = CartPage(context.driver)
    context.cart_page.click_on_cart()
    for item in context.add_item:
        context.cart_page.verify_product(item)


@then(u'remove some products and verify the list')
def remove_cart_item(context):
    # loop through until all the given remove items are removed
    for item in context.removal_item:
        print("removal item:", item)
        context.cart_page.remove_cart_item(item)
