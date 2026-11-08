from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from config import USUARIO, CLAVE
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_ver_en_el_carrito_los_productos_agregados(page: Page):
    # 1. TC-12
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(USUARIO, CLAVE)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    inventory_page.add_backpack()
    inventory_page.add_bike_light()
    inventory_page.open_cart()
    expect(cart_page.item_names).to_have_text(
        ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
    )

def test_quitar_un_producto_desde_el_carrito(page: Page):
    # 1. TC-13
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(USUARIO, CLAVE)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    inventory_page.add_backpack()
    inventory_page.open_cart()
    cart_page.remove_backpack()
    expect(cart_page.item_names).to_have_count(0)
    expect(inventory_page.cart_badge).to_have_count(0)


