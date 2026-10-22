from playwright.sync_api import Page, expect


def test_cerrar_sesion(page: Page):
    # 1. Entrar con standard_user (igual que en test_login.py)
    page.goto("https://www.saucedemo.com")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    # 2. Abrir el menú de la esquina superior izquierda
    page.locator("#react-burger-menu-btn").click()

    # 3. Hacer clic en Logout
    page.locator("#logout_sidebar_link").click()

    # 4. Verificar que volvió a la página de login
    expect(page).to_have_url("https://www.saucedemo.com/")