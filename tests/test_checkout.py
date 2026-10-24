from playwright.sync_api import Page, expect

def test_checkout_con_datos_validos(page: Page):
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

def test_checkout_con_el_apellido_vacio(page: Page):
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

def test_completar_la_compra_con_el_boton_finish(page: Page):
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
