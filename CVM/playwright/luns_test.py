from playwright.sync_api import Page, expect
import pytest
from units import *


# @pytest.mark.skip
def test_create_standard_volumes(page: Page):
    cvm = CVM(page)
    cvm.login(URL1)

    # check if appliance 145 exists, if not, add it
    page.get_by_role('link', name='Appliances').click()
    if not page.locator(f'p[title="{appliance2_name}"]').is_visible():
        cvm.add_appliance()

    page.get_by_role('link', name='Network').click()
    if not page.locator('p.wizard_table__table_item_text[title="Up"]').count() != 6:
        cvm.configure_ha_networking()

    # check if pools exist, if not, create them
    page.get_by_role('link', name='Storage pools').click()
    if page.get_by_text("There are no storage pools yet").is_visible():
        cvm.create_single_disk_pools()    
    
    page.get_by_role('link', name='Volumes').click()
    if page.get_by_text("There are no volumes yet").is_visible():
        cvm.create_standard_volumes()
        cvm.create_raw_volumes()

    page.get_by_role('link', name='LUNs').click()

    expect(page.get_by_role("heading", name="LUNs", exact=True)).to_be_visible()
    expect(page.get_by_text("There are no LUNs yet")).to_be_visible()
    expect(page.get_by_text("Start sharing your storage resources to clients by creating a new one")).to_be_visible()
    # expect(page.get_by_role("head").filter(has_text="Create a new LUN")).to_be_visible()

    # page.get_by_role("button").filter(has_text="Create a new LUN").click()


    # розібратись з Волюмами