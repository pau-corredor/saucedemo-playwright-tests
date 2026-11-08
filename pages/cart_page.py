from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.item_names = page.locator('[data-test="inventory-item-name"]')
        self.remove_backpack_button = page.locator('[data-test="remove-sauce-labs-backpack"]')

    def remove_backpack(self):
        self.remove_backpack_button.click()