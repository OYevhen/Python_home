from playwright.sync_api import Page, expect
import pytest
from units import *


# @pytest.mark.skip
def test_configure_ha_networking(page: Page):
    cvm = CVM(page)
    cvm.login(URL1)

    # check if appliance 145 exists, if not, add it
    page.get_by_role('link', name='Appliances').click()
    if not page.locator(f'p[title="{appliance2_name}"]').is_visible():
        cvm.add_appliance()

    page.get_by_role('link', name='Network').click()
    expect(page.get_by_role("heading", name="Network")).to_be_visible(timeout=10000)

    expect(page.get_by_role("heading", name="Network", exact=True)).to_be_visible()

    page.get_by_role("button").filter(has_text="Configure HA networking").click()

    expect(page.get_by_role("heading", name="Appliances", exact=True)).to_be_visible(timeout=100000)
    expect(page.get_by_text("Select appliances for network configuration. You can configure up to three appliances at a time")).to_be_visible()
    expect(page.locator('p.wizard_table__table_header_title[title="Appliance"]').first).to_be_visible()
    expect(page.get_by_text("Status", exact=True)).to_be_visible()
    expect(page.get_by_text("Software version")).to_be_visible()
    expect(page.get_by_text("License ID")).to_be_visible()
    expect(page.get_by_text("Adapters")).to_be_visible()




    page.get_by_role("row", name=f"{appliance1_name}").locator("span").click()
    page.get_by_role("row", name=f"{appliance2_name}").locator("span").click()
    page.get_by_role("row", name="Appliance Status Software").locator("span").click()
    page.get_by_role("row", name="Appliance Status Software").locator("span").click()
    page.get_by_role("button", name="Next").click()

    # To be continued...