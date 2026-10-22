from playwright.sync_api import Page, expect
import re

def test_agregar_un_producto_al_carrito_desde_la_lista(page: Page):
    # 1. TC-08
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    page.locator("#add-to-cart-sauce-labs-backpack").click()
    page.locator("#add-to-cart-sauce-labs-bike-light").click()

    expect(page.locator('[data-test="remove-sauce-labs-backpack"]')).to_have_text("Remove")
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text("2")

def test_las_imagenes_de_los_productos_son_las_correctas(page: Page):
    # 1. TC-09
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
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
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    precio_lista = page.locator('[data-test="inventory-item-price"]').first.inner_text()
    page.locator ('[data-test="inventory-item-name"]').first.click()
    expect(page.locator('[data-test="inventory-item-price"]')).to_have_text(precio_lista)
    page.locator('[data-test="add-to-cart"]').click()
    page.locator('[data-test="shopping-cart-link"]').click()
    expect(page.locator('[data-test="inventory-item-price"]')).to_have_text(precio_lista)

def test_quitar_un_producto_desde_la_lista_y_desde_el_detalle(page: Page):
    # 1. TC-11
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
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

def test_ver_en_el_carrito_los_productos_agregados(page: Page):
    # 1. TC-12
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]').click()
    page.locator('[data-test="shopping-cart-link"]').click()
    expect(page.locator('[data-test="inventory-item-name"]')).to_have_text(
        ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
    )

def test_quitar_un_product_desde_el_carrito(page: Page):
    # 1. TC-13
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[data-test="shopping-cart-link"]').click()
    page.locator('[data-test="remove-sauce-labs-backpack"]').click()
    expect(page.locator('[data-test="inventory-item-name"]')).to_have_count(0)
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_count(0)

def test_Checkout_con_datos_validos(page: Page):
    # 1. TC-14
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[data-test="shopping-cart-link"]').click()
    page.locator('[data-test="checkout"]').click()
    page.locator('[data-test="firstName"]').fill("Paula")
    page.locator('[data-test="lastName"]').fill("Tester")
    page.locator('[data-test="postalCode"]').fill("12345")
    page.locator('[data-test="continue"]').click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

def test_Checkout_con_el_apellido_vacío(page: Page):
    # 1. TC-15
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[data-test="shopping-cart-link"]').click()
    page.locator('[data-test="checkout"]').click()
    page.locator('[data-test="firstName"]').fill("Paula")
    page.locator('[data-test="lastName"]').fill("")
    page.locator('[data-test="postalCode"]').fill("12345")
    page.locator('[data-test="continue"]').click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    expect(page.locator('[data-test="error"]')).to_have_text("Error: Last Name is required")

def test_completar_la_compra_con_el_boton_Finish(page: Page):
    # 1. TC-16
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[data-test="shopping-cart-link"]').click()
    page.locator('[data-test="checkout"]').click()
    page.locator('[data-test="firstName"]').fill("Paula")
    page.locator('[data-test="lastName"]').fill("Tester")
    page.locator('[data-test="postalCode"]').fill("12345")
    page.locator('[data-test="continue"]').click()
    page.locator('[data-test="finish"]').click()
    expect(page.locator('[data-test="complete-header"]')).to_have_text("Thank you for your order!")

def test_el_total_del_pedido_coincide_con_la_suma_de_los_productos(page: Page):
    # 1. TC-17
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]').click()
    page.locator('[data-test="shopping-cart-link"]').click()
    page.locator('[data-test="checkout"]').click()
    page.locator('[data-test="firstName"]').fill("Paula")
    page.locator('[data-test="lastName"]').fill("Tester")
    page.locator('[data-test="postalCode"]').fill("12345")
    page.locator('[data-test="continue"]').click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    expect(page.locator('[data-test="subtotal-label"]')).to_have_text("Item total: $39.98")
    expect(page.locator('[data-test="tax-label"]')).to_have_text("Tax: $3.20")
    expect(page.locator('[data-test="total-label"]')).to_have_text("Total: $43.18")

