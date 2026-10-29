from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_cerrar_sesion(page: Page):
    # 1. Entrar con standard_user (igual que en test_login.py)
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    # 2. Abrir el menú de la esquina superior izquierda
    inventory_page = InventoryPage(page)

    # 3. Hacer clic en Logout
    inventory_page.logout()

    # 4. Verificar que volvió a la página de login
    expect(page).to_have_url("https://www.saucedemo.com/")