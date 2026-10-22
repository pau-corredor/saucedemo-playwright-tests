from playwright.sync_api import Page, expect

def test_ordenar_productos(page: Page):
    # 1. Entrar con standard_user
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    #2. Selecionar Name(Z to A)

    page.locator('[data-test="product-sort-container"]').select_option("za")
    expect(page.locator('[data-test="inventory-item-name"]').first).to_have_text(
        "Test.allTheThings() T-Shirt (Red)"
    )

    # 2. Selecionar Price(low to high)

    page.locator('[data-test="product-sort-container"]').select_option("lohi")
    expect(page.locator('[data-test="inventory-item-name"]').first).to_have_text(
        "Sauce Labs Onesie"
    )

    # 2. Selecionar Price (high to low)

    page.locator('[data-test="product-sort-container"]').select_option("hilo")
    expect(page.locator('[data-test="inventory-item-name"]').first).to_have_text(
        "Sauce Labs Fleece Jacket"
    )
    # 3. Selecionar Name (A to Z)

    page.locator('[data-test="product-sort-container"]').select_option("az")
    expect(page.locator('[data-test="inventory-item-name"]').first).to_have_text(
        "Sauce Labs Backpack"
    )