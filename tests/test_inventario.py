from playwright.sync_api import Page, expect
import re
from pages.login_page import LoginPage
from config import USUARIO, CLAVE
from pages.inventory_page import InventoryPage


def test_ordenar_productos(page: Page):
    # 1. Entrar con standard_user
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(USUARIO, CLAVE)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    inventory_page = InventoryPage(page)


    #2. Seleccionar Name(Z to A)

    inventory_page.sort_by("za")
    expect (inventory_page.item_names.first).to_have_text(
        "Test.allTheThings() T-Shirt (Red)"
    )

    # 2. Seleccionar Price(low to high)

    inventory_page.sort_by("lohi")
    expect(inventory_page.item_names.first).to_have_text(
        "Sauce Labs Onesie"
    )

    # 2. Seleccionar Price (high to low)

    inventory_page.sort_by("hilo")
    expect(inventory_page.item_names.first).to_have_text(
        "Sauce Labs Fleece Jacket"
    )
    # 3. Seleccionar Name (A to Z)

    inventory_page.sort_by("az")
    expect(inventory_page.item_names.first).to_have_text(
        "Sauce Labs Backpack"
    )

def test_agregar_un_producto_al_carrito_desde_la_lista(page: Page):
    # 1. TC-08
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(USUARIO, CLAVE)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    inventory_page = InventoryPage(page)
    inventory_page.add_backpack()
    inventory_page.add_bike_light()

    expect(page.locator('[data-test="remove-sauce-labs-backpack"]')).to_have_text("Remove")
    expect(inventory_page.cart_badge).to_have_text("2")

def test_las_imagenes_de_los_productos_son_las_correctas(page: Page):
    # 1. TC-09
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(USUARIO, CLAVE)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    expect(page.locator('[data-test="inventory-item-sauce-labs-backpack-img"]')).to_be_visible()
    expect(page.locator('[data-test="inventory-item-sauce-labs-backpack-img"]')).to_have_attribute(
        "src", re.compile("backpack")
    )
    expect(page.locator('[data-test="inventory-item-sauce-labs-bike-light-img"]')).to_be_visible()
    expect(page.locator('[data-test="inventory-item-sauce-labs-bike-light-img"]')).to_have_attribute(
        "src", re.compile("bike-light")
    )
    expect(page.locator('[data-test="inventory-item-sauce-labs-bolt-t-shirt-img"]')).to_be_visible()
    expect(page.locator('[data-test="inventory-item-sauce-labs-bolt-t-shirt-img"]')).to_have_attribute(
        "src", re.compile("bolt-shirt")
    )
    expect(page.locator('[data-test="inventory-item-sauce-labs-fleece-jacket-img"]')).to_be_visible()
    expect(page.locator('[data-test="inventory-item-sauce-labs-fleece-jacket-img"]')).to_have_attribute(
        "src", re.compile("sauce-pullover")
    )
    expect(page.locator('[data-test="inventory-item-sauce-labs-onesie-img"]')).to_be_visible()
    expect(page.locator('[data-test="inventory-item-sauce-labs-onesie-img"]')).to_have_attribute(
        "src", re.compile("red-onesie")
    )
    expect(page.locator('[data-test="inventory-item-test.allthethings()-t-shirt-(red)-img"]')).to_be_visible()
    expect(page.locator('[data-test="inventory-item-test.allthethings()-t-shirt-(red)-img"]')).to_have_attribute(
        "src", re.compile("red-tatt")
    )

def test_el_precio_de_un_producto_es_el_mismo_en_la_lista_el_detalle_y_el_carrito(page: Page):
    # 1. TC-10
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(USUARIO, CLAVE)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    precio_lista = page.locator('[data-test="inventory-item-price"]').first.inner_text()
    page.locator('[data-test="inventory-item-name"]').first.click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory-item.html?id=4")
    expect(page.locator('[data-test="inventory-item-price"]')).to_have_count(1)
    expect(page.locator('[data-test="inventory-item-price"]')).to_have_text(precio_lista)
    page.locator('[data-test="add-to-cart"]').click()
    page.locator('[data-test="shopping-cart-link"]').click()
    expect(page.locator('[data-test="inventory-item-price"]')).to_have_text(precio_lista)

def test_quitar_un_producto_desde_la_lista_y_desde_el_detalle(page: Page):
    # 1. TC-11
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(USUARIO, CLAVE)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    expect(page.locator('[data-test="remove-sauce-labs-backpack"]')).to_have_text("Remove")


    page.locator('[data-test="remove-sauce-labs-backpack"]').click()
    expect(page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')).to_have_text("Add to cart")
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_count(0)

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[data-test="inventory-item-name"]').first.click()
    page.locator('[data-test="remove"]').click()
    expect(page.locator('[data-test="add-to-cart"]')).to_have_text("Add to cart")
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_count(0)