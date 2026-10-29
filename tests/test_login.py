from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_login_valido(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_login_usuario_bloqueado(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("locked_out_user", "secret_sauce")
    expect(login_page.error_message).to_have_text(
        "Epic sadface: Sorry, this user has been locked out."
    )


def test_login_credenciales_incorrectas(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("usuario1", "secret_sauce")
    expect(login_page.error_message).to_have_text(
        "Epic sadface: Username and password do not match any user in this service"
    )


def test_login_username_vacio(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("", "secret_sauce")
    expect(login_page.error_message).to_have_text(
        "Epic sadface: Username is required"
    )


def test_login_password_vacio(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "")
    expect(login_page.error_message).to_have_text(
        "Epic sadface: Password is required"
    )