from playwright.sync_api import Page, expect


def test_login_valido(page: Page):
    page.goto("https://www.saucedemo.com")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_login_usuario_bloqueado(page: Page):
    page.goto("https://www.saucedemo.com")
    page.locator("#user-name").fill("locked_out_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    expect(page.locator('[data-test="error"]')).to_have_text(
        "Epic sadface: Sorry, this user has been locked out."
    )


def test_login_credenciales_incorrectas(page: Page):
    page.goto("https://www.saucedemo.com")
    page.locator("#user-name").fill("usuario_inexistente")
    page.locator("#password").fill("clave_incorrecta")
    page.locator("#login-button").click()
    expect(page.locator('[data-test="error"]')).to_have_text(
        "Epic sadface: Username and password do not match any user in this service"
    )


def test_login_username_vacio(page: Page):
    page.goto("https://www.saucedemo.com")
    page.locator("#login-button").click()
    expect(page.locator('[data-test="error"]')).to_have_text(
        "Epic sadface: Username is required"
    )


def test_login_password_vacio(page: Page):
    page.goto("https://www.saucedemo.com")
    page.locator("#user-name").fill("standard_user")
    page.locator("#login-button").click()
    expect(page.locator('[data-test="error"]')).to_have_text(
        "Epic sadface: Password is required"
    )