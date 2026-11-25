from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from config import USUARIO, CLAVE
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout_con_datos_validos(page: Page):
    # 1. TC-14
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(USUARIO, CLAVE)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    inventory_page.add_backpack()
    inventory_page.open_cart()
    cart_page.go_to_checkout()
    checkout_page.fill_info("Paula", "Tester", "12345")
    checkout_page.continue_button_checkout()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

def test_checkout_con_el_apellido_vacio(page: Page):
    # 1. TC-15
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(USUARIO, CLAVE)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    inventory_page.add_backpack()
    inventory_page.open_cart()
    cart_page.go_to_checkout()
    checkout_page.fill_info("Paula", "", "12345")
    checkout_page.continue_button_checkout()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    expect(checkout_page.error_message).to_have_text("Error: Last Name is required")

def test_completar_la_compra_con_el_boton_finish(page: Page):
    # 1. TC-16
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(USUARIO, CLAVE)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    inventory_page.add_backpack()
    inventory_page.open_cart()
    cart_page.go_to_checkout()
    checkout_page.fill_info("Paula", "Tester", "12345")
    checkout_page.continue_button_checkout()
    checkout_page.finish_button_checkout()
    expect(checkout_page.confirmation_message).to_have_text("Thank you for your order!")

def test_el_total_del_pedido_coincide_con_la_suma_de_los_productos(page: Page):
    # 1. TC-17
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(USUARIO, CLAVE)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    inventory_page.add_backpack()
    inventory_page.add_bike_light()
    inventory_page.open_cart()
    cart_page.go_to_checkout()
    checkout_page.fill_info("Paula", "Tester", "12345")
    checkout_page.continue_button_checkout()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    expect(checkout_page.item_total).to_have_text("Item total: $39.98")
    expect(checkout_page.tax).to_have_text("Tax: $3.20")
    expect(checkout_page.total).to_have_text("Total: $43.18")
