from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.menu_button = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("#logout_sidebar_link")
        self.add_backpack_button = page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')
        self.add_bike_light_button = page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]')
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.sort_dropdown = page.locator('[data-test="product-sort-container"]')
        self.item_names = page.locator('[data-test="inventory-item-name"]')

    def logout(self):
        self.menu_button.click()
        self.logout_link.click()

    def add_backpack(self):
        self.add_backpack_button.click()

    def add_bike_light(self):
        self.add_bike_light_button.click()

    def open_cart(self):
        self.cart_link.click()

    def sort_by(self, opcion):
        self.sort_dropdown.select_option(opcion)