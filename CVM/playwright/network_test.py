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

    expect(page.get_by_role("heading", name="Set network channels", exact=True)).to_be_visible(timeout=100000)
    expect(page.get_by_text("Set interfaces to carry storage traffic, configure them with unique IP addresses, and specify subnet masks")).to_be_visible()
    expect(page.get_by_text("Ensure interfaces are connected to client hosts directly or through redundant switches")).to_be_visible()
    page.locator("div.icon_tooltip__icon.icon_tooltip__icon--question").hover()
    expect(page.get_by_text("Management adapters: Used for heartbeat (monitoring the health of appliances).")).to_be_visible()
    expect(page.get_by_text("Data adapters: Used for client network connections and heartbeat.")).to_be_visible()
    expect(page.get_by_text("Replication adapters: Used for synchronous data replication between appliances.")).to_be_visible()
    expect(page.get_by_text("Show sample network diagram")).to_be_visible()
    expect(page.get_by_text("Network channel configuration is failed.")).to_be_visible()
    expect(page.get_by_text("Assign at least two interfaces on each node, one per role (one for “Data” and one for “Replication”).")).to_be_visible()
    expect(page.locator("div.windowsVirtualDisks__settings_appliance-title").filter(has_text=f"{appliance1_name}")).to_be_visible()
    expect(page.locator("table").nth(0).locator("p.wizard_table__table_header_title[title='Interface']")).to_be_visible()
    expect(page.locator("table").nth(0).locator("p.wizard_table__table_header_title[title='Adapter model']")).to_be_visible()
    expect(page.locator("table").nth(0).locator("p.wizard_table__table_header_title[title='Bandwidth']")).to_be_visible()
    expect(page.locator("table").nth(0).locator("p.wizard_table__table_header_title[title='MAC address']")).to_be_visible()
    expect(page.locator("table").nth(0).locator("p.wizard_table__table_header_title[title='IP address']")).to_be_visible()
    expect(page.locator("table").nth(0).locator("p.wizard_table__table_header_title[title='Netmask']")).to_be_visible()
    expect(page.locator("table").nth(0).locator("p.wizard_table__table_header_title[title='Link status']")).to_be_visible()
    expect(page.locator("table").nth(0).locator("p.wizard_table__table_header_title[title='Data']")).to_be_visible()
    expect(page.locator("table").nth(0).locator("p.wizard_table__table_header_title[title='Replication']")).to_be_visible()
    expect(page.locator("div.windowsVirtualDisks__settings_appliance-title").filter(has_text=f"{appliance2_name}")).to_be_visible()
    expect(page.locator("table").nth(1).locator("p.wizard_table__table_header_title[title='Interface']")).to_be_visible()
    expect(page.locator("table").nth(1).locator("p.wizard_table__table_header_title[title='Adapter model']")).to_be_visible()
    expect(page.locator("table").nth(1).locator("p.wizard_table__table_header_title[title='Bandwidth']")).to_be_visible()
    expect(page.locator("table").nth(1).locator("p.wizard_table__table_header_title[title='MAC address']")).to_be_visible()
    expect(page.locator("table").nth(1).locator("p.wizard_table__table_header_title[title='IP address']")).to_be_visible()
    expect(page.locator("table").nth(1).locator("p.wizard_table__table_header_title[title='Netmask']")).to_be_visible()
    expect(page.locator("table").nth(1).locator("p.wizard_table__table_header_title[title='Link status']")).to_be_visible()
    expect(page.locator("table").nth(1).locator("p.wizard_table__table_header_title[title='Data']")).to_be_visible()
    expect(page.locator("table").nth(1).locator("p.wizard_table__table_header_title[title='Replication']")).to_be_visible()
    expect(page.get_by_text("Cluster MTU size:")).to_be_visible()
    expect(page.get_by_text("Acceptable size 1500-9000")).to_be_visible()

    page.get_by_role("spinbutton").fill("99000")
    page.get_by_role("textbox").nth(0).fill(f"14.14.14.{appliance1_name}")

    expect(page.get_by_text("Indicate a valid value in range of 1500-9000")).to_be_visible()

    page.get_by_role("textbox").nth(1).fill("24")
    page.get_by_role("textbox").nth(2).fill(f"15.15.15.{appliance1_name}")
    page.get_by_role("textbox").nth(3).fill("24")
    page.get_by_role("textbox").nth(4).fill(f"14.14.14.{appliance2_name}")
    page.get_by_role("textbox").nth(5).fill("24")
    page.get_by_role("textbox").nth(6).fill(f"15.15.15.{appliance2_name}")
    page.get_by_role("textbox").nth(7).fill("24")
    page.locator("#ens224").nth(1).click()
    page.locator("#ens256").nth(0).click()
    page.locator("#ens224").nth(0).click()
    page.locator("#ens256").nth(1).click()
    page.locator("#ens224").nth(2).click()
    page.locator("#ens256").nth(3).click()
    page.get_by_role("spinbutton").fill("9000")
    page.get_by_role("button", name="Next").click()
