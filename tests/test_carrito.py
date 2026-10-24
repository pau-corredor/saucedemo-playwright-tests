from playwright.sync_api import Page, expect

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


