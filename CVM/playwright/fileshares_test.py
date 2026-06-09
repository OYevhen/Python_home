from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError, expect
from units import *
import pytest


# @pytest.mark.skip
def test_create_2ha_iscsi_ram_lun(page: Page, name="ilun2haram"):
    cvm = CVM(page)
    cvm.login(URL1)

    # check if appliance 145 exists, if not, add it
    page.get_by_role('link', name='Appliances').click()
    if not page.locator(f'p[title="{appliance2_name}"]').is_visible():
        cvm.add_appliance()

    page.get_by_role('link', name='Network').click()
    if page.locator('p.wizard_table__table_item_text[title="Up "]').count() != 6 or page.locator('p.wizard_table__table_item_text[title="Unassigned"]').count() == 4:
        cvm.configure_ha_networking()

    # check if pools exist, if not, create them
    page.get_by_role('link', name='Storage pools').click()
    if not page.locator(f'p[title="{appliance1_name}"]').is_visible():
        cvm.create_single_disk_pools()    
    
    page.get_by_role('link', name='Volumes').click()
    # if page.get_by_text("There are no volumes yet").is_visible():
    #     cvm.create_standard_volumes()
    if not page.locator('tr').filter(has=page.locator(f'p[title="{appliance1_name}"]')).locator(f'p[title="Standard"]').is_visible():
        cvm.create_standard_volumes()
    

    page.get_by_role('link', name='LUNs').click()

    if page.get_by_role("row", name=name).count() > 0:
        cvm.delete_iscsi_lun(name)

    expect(page.get_by_role("heading", name="LUNs", exact=True)).to_be_visible()
    # expect(page.get_by_text("There are no LUNs yet")).to_be_visible()
    # expect(page.get_by_text("Start sharing your storage resources to clients by creating a new one")).to_be_visible()

    page.get_by_role("button").filter(has_text="Create a new LUN").click(timeout=100000)