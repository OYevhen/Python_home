from playwright.sync_api import Page, expect
import pytest
from units import *


# @pytest.mark.skip
def test_create_2ha_iscsi_lun(page: Page):
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
        # cvm.create_raw_volumes()

    page.get_by_role('link', name='LUNs').click()

    expect(page.get_by_role("heading", name="LUNs", exact=True)).to_be_visible()
    expect(page.get_by_text("There are no LUNs yet")).to_be_visible()
    expect(page.get_by_text("Start sharing your storage resources to clients by creating a new one")).to_be_visible()

    page.get_by_role("button").filter(has_text="Create a new LUN").click()

    expect(page.get_by_role("heading", level=2, name="Choose protocol")).to_be_visible()
    expect(page.get_by_text("Select a storage protocol based on performance and compatibility")).to_be_visible()
    expect(page.get_by_role("heading", level=3, name="iSCSI")).to_be_visible()
    expect(page.get_by_text("iSCSI is a recommended protocol for most HDD-based setups or medium-performance SSD-based setups.")).to_be_visible()
    expect(page.get_by_text("This option offers broader compatibility for storage clients.")).to_be_visible()
    expect(page.get_by_role("heading", level=3, name="NVMe-oF")).to_be_visible()
    expect(page.get_by_text("NVMe over Fabrics (NVMe-oF) is a recommended option for high-performance SSD or NVMe setups.")).to_be_visible()
    expect(page.get_by_text("Before you proceed, make sure that your clients are NVMe-oF compatible.")).to_be_visible()

    page.get_by_role("radio").nth(0).check()
    page.get_by_role("button", name="Next").click()

    expect(page.get_by_role("heading", level=2, name="Set LUN availability")).to_be_visible()
    expect(page.get_by_text("Choose the required LUN availability")).to_be_visible()
    expect(page.get_by_role("heading", level=3, name="High availability (two-way or three-way replication)")).to_be_visible()
    expect(page.get_by_text("Create a synchronously replicated LUN hosted on two or three identical appliances.")).to_be_visible()
    expect(page.get_by_text("The LUN stays accessible if one of the replication partners becomes unavailable.")).to_be_visible()
    expect(page.get_by_role("heading", level=3, name="Standalone")).to_be_visible()
    expect(page.get_by_text("Create a non-replicated iSCSI LUN hosted on a single appliance.")).to_be_visible()
    expect(page.get_by_text("The LUN will not be accessible if its host becomes unavailable.")).to_be_visible()

    page.get_by_role("radio").nth(0).check()
    page.get_by_role("button", name="Next").click()

    expect(page.get_by_role("heading", level=2, name="Select appliances")).to_be_visible()
    expect(page.get_by_text("Select two or three replication partners that should host the HA LUN")).to_be_visible()
    expect(page.get_by_text("All appliances must have identical hardware configurations, including CPU, RAM, storage, and networking")).to_be_visible()
    expect(page.locator('p.wizard_table__table_header_title[title="Appliances"]')).to_be_visible()
    expect(page.get_by_text("Status")).to_be_visible()
    expect(page.get_by_text("Software version")).to_be_visible()
    expect(page.get_by_text("RAW capacity")).to_be_visible()
    expect(page.get_by_text("License ID")).to_be_visible()

    page.get_by_text(f"{appliance1_name}").click()
    page.get_by_text(f"{appliance2_name}").click()
    
    expect(page.get_by_text("Allow adding partner with different storage configurations")).to_be_visible()
    page.locator("div.virtual_disk_wizard__info").hover()
    expect(page.locator("p.virtual_disk_wizard__info_tooltip").filter(has_text="This option allows creating a LUN")).to_be_visible()
    page.locator("label").filter(has_text="Allow adding partner with").locator("span").click()
    page.get_by_role("button", name="Next").click()

    expect(page.get_by_text("Connecting to appliances...")).to_be_visible()

    expect(page.get_by_role("heading", level=2, name="Select volumes")).to_be_visible()
    expect(page.get_by_text("Select one volume on each appliance to store the HA LUN data. Selected volumes must have identical storage configurations.")).to_be_visible()
    expect(page.get_by_text("Volumes have identical configurations")).to_be_visible()
    expect(page.get_by_text("Volume").nth(0)).to_be_visible()
    expect(page.get_by_text("State").nth(0)).to_be_visible()
    expect(page.get_by_text("Layout").nth(0)).to_be_visible()
    expect(page.get_by_text("Capacity").nth(0)).to_be_visible()
    expect(page.get_by_text("Free capacity").nth(0)).to_be_visible()
    expect(page.get_by_text("Type").nth(0)).to_be_visible()

    page.get_by_role("button", name="Next").click()

    expect(page.get_by_role("heading", level=2, name="Set failover strategy")).to_be_visible()
    expect(page.get_by_text("Select the preferred failover strategy. The default is “Heartbeat”. However, you can choose another method if you do not have a UPS unit at your disposal.")).to_be_visible()
    expect(page.get_by_role("heading", level=3, name="“Heartbeat” (Recommended)")).to_be_visible()
    expect(page.get_by_text("Appliances constantly communicate via “Heartbeat” networks.")).to_be_visible()
    expect(page.get_by_text("To minimize the chances of “split-brain” during blackouts, configure UPS to prevent the simultaneous shutdown of both appliances.")).to_be_visible()
    expect(page.get_by_role("heading", level=3, name="Node majority")).to_be_visible()
    expect(page.get_by_text("Two appliances replicate data synchronously and hold votes.")).to_be_visible()
    expect(page.get_by_text("A third appliance acts as a witness, providing a tie-breaking vote to prevent split-brain but does not store data.")).to_be_visible()
    expect(page.get_by_role("heading", level=3, name="File share witness")).to_be_visible()
    expect(page.get_by_text("SMB file share acts as an independent entity that provides a quorum majority in case of connection loss between appliances.")).to_be_visible()
    expect(page.get_by_text("The working SMB share witness excludes the possibility of a “split-brain” condition.")).to_be_visible()

    page.get_by_role("heading", level=3, name="Node majority").hover()
    expect(page.locator("div.markdown__wrapper.tooltip__text").get_by_text("Add a third appliance to use the Node witness failover strategy")).to_be_visible()
    
    page.get_by_role("heading", level=3, name="File share witness").hover()
    expect(page.locator("div.markdown__wrapper.tooltip__text").get_by_text("The feature will be provided in the next version")).to_be_visible()

    page.get_by_role("button", name="Next").click()