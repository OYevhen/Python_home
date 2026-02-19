from playwright.sync_api import Page, expect
from units import *
import pytest


#@pytest.mark.skip
def test_create_2ha_iscsi_ram(page: Page):
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

    page.get_by_role('link', name='LUNs').click()

    if not page.get_by_text("There are no LUNs yet").is_visible():
        cvm.delete_luns()

    expect(page.get_by_role("heading", name="LUNs", exact=True)).to_be_visible()
    expect(page.get_by_text("There are no LUNs yet")).to_be_visible()
    expect(page.get_by_text("Start sharing your storage resources to clients by creating a new one")).to_be_visible()

    page.get_by_role("button").filter(has_text="Create a new LUN").click(timeout=100000)

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

    expect(page.get_by_role("heading", level=2, name="Select volumes")).to_be_visible(timeout=100000)
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

    expect(page.get_by_role("heading", level=2, name="Set network channels")).to_be_visible()
    expect(page.get_by_text("Set interfaces to carry storage traffic, configure them with unique IP addresses, and specify subnet masks")).to_be_visible()
    expect(page.get_by_text("Assign and configure at least two interfaces on each node, one per role (one for Data and one for Replication)")).to_be_visible()
    expect(page.get_by_text("Ensure interfaces are connected to client hosts directly or through redundant switches")).to_be_visible()
    expect(page.get_by_role("button", name="Show sample network diagram")).to_be_visible()
    expect(page.get_by_text("Network channel configuration is failed.")).to_be_visible()
    expect(page.get_by_text("Assign at least two interfaces on each node, one per role (one for “Data” and one for “Replication”).")).to_be_visible()

    page.locator(".icon_tooltip__icon").hover()
    expect(page.locator("ul.wizards_network__info_block_tooltip_list li").filter(has_text="Management adapters: Used for heartbeat (monitoring the health of appliances).")).to_be_visible()
    expect(page.locator("ul.wizards_network__info_block_tooltip_list li").filter(has_text="Data adapters: Used for client network connections and heartbeat.")).to_be_visible()
    expect(page.locator("ul.wizards_network__info_block_tooltip_list li").filter(has_text="Replication adapters: Used for synchronous data replication between appliances.")).to_be_visible()
    
    expect(page.get_by_text("Interface").nth(0)).to_be_visible()
    expect(page.get_by_text("Link status").nth(0)).to_be_visible()
    expect(page.get_by_text("Adapter model").nth(0)).to_be_visible()
    expect(page.get_by_text("IP address").nth(0)).to_be_visible()
    expect(page.get_by_text("Management").nth(0)).to_be_visible()
    expect(page.get_by_text("Data").nth(0)).to_be_visible()
    expect(page.get_by_text("Replication").nth(0)).to_be_visible()

    page.get_by_role("checkbox").nth(4).click()
    page.locator("input[name=\"eth2\"]").nth(2).click()
    page.locator("input[name=\"eth1\"]").nth(4).click()
    page.locator("input[name=\"eth2\"]").nth(5).click()

    expect(page.get_by_text("Network channel configuration is failed.")).not_to_be_visible()
    expect(page.get_by_text("Assign at least two interfaces on each node, one per role (one for “Data” and one for “Replication”).")).not_to_be_visible()

    page.locator("input[name=\"eth2\"]").nth(1).click()

    expect(page.get_by_text("Network channel configuration is failed.")).to_be_visible()
    expect(page.get_by_text("Assign at least two interfaces on each node, one per role (one for “Data” and one for “Replication”).")).to_be_visible()

    page.locator("input[name=\"eth2\"]").nth(2).click()
    page.get_by_role("button", name="Next").click()

    expect(page.get_by_text("Testing network settings...")).to_be_visible()

    expect(page.get_by_role("heading", name="Non-redundant configuration", level=2).nth(0)).to_be_visible(timeout=100000)
    expect(page.get_by_text("Only 1 Replication network is configured. Configure more Replication networks to eliminate a single point of failure.")).to_be_visible()
    expect(page.get_by_text("We recommended assigning at least two data network interfaces to eliminate a single point of failure.").nth(0)).to_be_visible()
    expect(page.get_by_text("Acknowledge and continue?").nth(0)).to_be_visible()

    page.get_by_role("button", name="Yes, continue").nth(1).click()

    expect(page.get_by_role("heading", name="Non-redundant configuration", level=2)).to_be_visible()
    expect(page.get_by_text("Only 1 Data network is configured. Configure more Data networks to eliminate a single point of failure.")).to_be_visible()
    expect(page.get_by_text("We recommended assigning at least two data network interfaces to eliminate a single point of failure.")).to_be_visible()
    expect(page.get_by_text("Acknowledge and continue?")).to_be_visible()

    page.get_by_role("button", name="Yes, continue").click()

    expect(page.get_by_role("heading", level=2, name="Specify LUN settings")).to_be_visible()
    expect(page.get_by_text("Specify the HA LUN settings")).to_be_visible()
    expect(page.get_by_text("VMFS6 Datastore")).to_be_visible()
    expect(page.locator("p.checkbox-label-msg").filter(has_text="Create VMFS 6 Datastore (with 512 block size)")).to_have_class("checkbox-label-msg  disabled")

    page.locator("div.virtual_disk_wizard__caption-tooltip").hover()
    expect(page.locator("div.virtual_disk_wizard__caption-tooltip").get_by_text("Connect all appliances to the same vCenter Server by installing the StarWind plugin in Settings.")).to_be_visible()

    page.locator("input.MuiInputBase-input").nth(0).click()
    page.locator("input.MuiInputBase-input").nth(1).click()
    expect(page.get_by_text("LUN name can not be empty")).to_be_visible()
    page.locator("input.MuiInputBase-input").nth(0).fill("!@#")
    page.locator("input.MuiInputBase-input").nth(1).click()
    expect(page.get_by_text("Must start with a Latin letter or number")).to_be_visible()
    page.locator("input.MuiInputBase-input").nth(0).fill("ilun2haram")
    expect(page.get_by_text("A minimum of 1 GB is required")).to_be_visible()
    page.locator("input.MuiInputBase-input").nth(1).fill("2")
    page.locator("input.MuiInputBase-input").nth(0).click()
    expect(page.get_by_text("Available space:")).to_be_visible()
    page.locator("input.MuiInputBase-input").nth(1).fill("1")

    page.get_by_role("button", name="Next").click()

    expect(page.get_by_role("heading", level=2, name="Journal type")).to_be_visible()
    expect(page.get_by_text("Select the preferred synchronization journal type.")).to_be_visible()
    expect(page.get_by_role("heading", level=3, name="RAM-based journal")).to_be_visible()
    expect(page.get_by_text("The synchronization journal is stored in RAM. Delivers the highest I/O performance. If desynchronization occurs, RAM-based journaling takes over. Full sync may be triggered by power loss on all nodes, improper shutdowns, interrupted sync, or write errors.")).to_be_visible()
    expect(page.get_by_role("heading", level=3, name="Disk-based failure journal")).to_be_visible()
    expect(page.get_by_text("The synchronization journal is stored on disk. Offers high I/O performance while nodes are synchronized. If desynchronization occurs, disk-based journaling takes over. Fast sync is not guaranteed after events like simultaneous node resets.")).to_be_visible()
    expect(page.get_by_role("heading", level=3, name="Disk-based continuous journal")).to_be_visible()
    expect(page.get_by_text("The synchronization journal is stored on a separate disk. Provides full-time protection and fast synchronization in all cases. Offers the lowest I/O performance due to frequent writes. SSD or NVMe is recommended to reduce performance impact.")).to_be_visible()

    page.get_by_role("radio").nth(1).check()
    page.get_by_role("radio").nth(2).check()
    page.get_by_role("radio").nth(0).check()
    page.get_by_role("button", name="Next").click()

    expect(page.get_by_role("heading", level=2, name="Review summary")).to_be_visible()
    expect(page.locator("div.ha__summary-name").nth(0)).to_contain_text("Protocol")
    expect(page.locator("div.ha__summary-description").nth(0)).to_contain_text("iSCSI")
    expect(page.locator("div.ha__summary-name").nth(1)).to_contain_text("LUN Availability")
    expect(page.locator("div.ha__summary-description").nth(1)).to_contain_text("High availability (two-way replication)")
    expect(page.locator("div.ha__summary-name").nth(2)).to_contain_text("Appliances")
    expect(page.locator("div.ha__summary-description").nth(2)).to_contain_text(f"{appliance1_name}{appliance2_name}")
    expect(page.locator("div.ha__summary-name").nth(3)).to_contain_text("Volumes")
    expect(page.locator("div.ha__summary-description").nth(3)).to_contain_text("svolsvol")
    expect(page.locator("div.ha__summary-name").nth(4)).to_contain_text("Failover strategy")
    expect(page.locator("div.ha__summary-description").nth(4)).to_contain_text("Heartbeat")

    expect(page.locator("div.ha__summary-name").nth(5)).to_contain_text("Management IP addresses")
    expect(page.locator("div.ha__summary-description").nth(5)).to_contain_text(f"172.16.6.{appliance2_name}, 172.16.6.{appliance1_name}")
    expect(page.locator("div.ha__summary-name").nth(6)).to_contain_text("Data IP addresses")
    expect(page.locator("div.ha__summary-description").nth(6)).to_contain_text(f"14.14.14.{appliance2_name}, 14.14.14.{appliance1_name}")
    expect(page.locator("div.ha__summary-name").nth(7)).to_contain_text("Replication IP addresses")
    expect(page.locator("div.ha__summary-description").nth(7)).to_contain_text(f"15.15.15.{appliance2_name}, 15.15.15.{appliance1_name}")
    expect(page.locator("div.ha__summary-name").nth(8)).to_contain_text("LUN")
    expect(page.locator("div.ha__summary-description").nth(8)).to_contain_text("ilun2haram")
    expect(page.locator("div.ha__summary-name").nth(9)).to_contain_text("LUN size")
    expect(page.locator("div.ha__summary-description").nth(9)).to_contain_text("1 GB")
    expect(page.locator("div.ha__summary-name").nth(10)).to_contain_text("Journal type")
    expect(page.locator("div.ha__summary-description").nth(10)).to_contain_text("RAM-based")

    page.locator('button.modalwindow__close_icon').click()  #close by pressing 'x'

    expect(page.get_by_text("Close Wizard")).to_be_visible()
    expect(page.get_by_text("Are you sure you want to close the wizard? All changes will be discarded.")).to_be_visible()

    page.locator('button.modalwindow__close_icon').nth(2).click()  #close by pressing 'x'
    page.locator('button.modalwindow__close_icon').click()  #close by pressing 'x'
    page.get_by_role("button", name="No, cancel").click()
    page.get_by_role("button", name="Create LUN").click()

    expect(page.get_by_role("row", name="ilun2haram")).to_be_visible(timeout=1000000)

#@pytest.mark.skip
def test_create_2ha_iscsi_disk(page: Page):
    pass

#@pytest.mark.skip
def test_create_2ha_iscsi_continuous(page: Page):
    pass

def test_create_2ha_nvme(page: Page):
    cvm = CVM(page)
    cvm.login(URL1)

    # check if appliance 145 exists, if not, add it
    page.get_by_role('link', name='Appliances').click()
    if not page.locator(f'p[title="{appliance2_name}"]').is_visible():
        cvm.add_appliance()

    page.get_by_role('link', name='Network').click(timeout=100000)
    if page.locator('p.wizard_table__table_item_text[title="Unassigned"]').count() == 4:    #page.locator('p.wizard_table__table_item_text[title="Up"]').count() != 6 or 
        cvm.configure_ha_networking()

    # check if pools exist, if not, create them
    page.get_by_role('link', name='Storage pools').click()
    if page.get_by_text("There are no storage pools yet").is_visible():
        cvm.create_single_disk_pools()    
    
    page.get_by_role('link', name='Volumes').click()
    if page.get_by_text("There are no volumes yet").is_visible():
        cvm.create_raw_volumes()

    if not page.locator('tr').filter(has=page.locator(f'p[title="{appliance1_name}"]')).locator(f'p[title="Raw"]').is_visible():
        cvm.create_raw_volumes()
    
    page.get_by_role('link', name='LUNs').click()

    if not page.get_by_text("There are no LUNs yet").is_visible():
        cvm.delete_luns()

    expect(page.get_by_role("heading", name="LUNs", exact=True)).to_be_visible()
    expect(page.get_by_text("There are no LUNs yet")).to_be_visible()
    expect(page.get_by_text("Start sharing your storage resources to clients by creating a new one")).to_be_visible()

    page.get_by_role("button").filter(has_text="Create a new LUN").click(timeout=100000)

    expect(page.get_by_role("heading", level=2, name="Choose protocol")).to_be_visible()
    expect(page.get_by_text("Select a storage protocol based on performance and compatibility")).to_be_visible()
    expect(page.get_by_role("heading", level=3, name="iSCSI")).to_be_visible()
    expect(page.get_by_text("iSCSI is a recommended protocol for most HDD-based setups or medium-performance SSD-based setups.")).to_be_visible()
    expect(page.get_by_text("This option offers broader compatibility for storage clients.")).to_be_visible()
    expect(page.get_by_role("heading", level=3, name="NVMe-oF")).to_be_visible()
    expect(page.get_by_text("NVMe over Fabrics (NVMe-oF) is a recommended option for high-performance SSD or NVMe setups.")).to_be_visible()
    expect(page.get_by_text("Before you proceed, make sure that your clients are NVMe-oF compatible.")).to_be_visible()

    page.get_by_role("radio").nth(1).check()
    page.get_by_role("button", name="Next").click()

    expect(page.get_by_role("heading", level=2, name="Set LUN availability")).to_be_visible()
    expect(page.get_by_text("Choose the required LUN availability")).to_be_visible()
    expect(page.get_by_role("heading", level=3, name="High availability (two-way or three-way replication)")).to_be_visible()
    expect(page.get_by_text("Create a synchronously replicated LUN hosted on two or three identical appliances.")).to_be_visible()
    expect(page.get_by_text("The LUN stays accessible if one of the replication partners becomes unavailable.")).to_be_visible()
    expect(page.get_by_role("heading", level=3, name="Standalone")).to_be_visible()
    expect(page.get_by_text("Create a non-replicated LUN hosted on a single appliance.")).to_be_visible()
    expect(page.get_by_text("The LUN will not be accessible if its host becomes unavailable.")).to_be_visible()

    page.get_by_role("button", name="Next").click()

    expect(page.get_by_role("heading", level=2, name="Select appliances")).to_be_visible()
    expect(page.get_by_text("Select two replication partners that should host the HA LUN")).to_be_visible()
    expect(page.get_by_text("All appliances must have identical hardware configurations, including CPU, RAM, storage, and networking")).to_be_visible()
    expect(page.locator('p.wizard_table__table_header_title[title="Appliances"]')).to_be_visible()
    expect(page.get_by_text("Status")).to_be_visible()
    expect(page.get_by_text("Software version")).to_be_visible()
    expect(page.get_by_text("RAW capacity")).to_be_visible()
    expect(page.get_by_text("License ID")).to_be_visible()

    page.get_by_text(f"{appliance1_name}").click()
    page.get_by_text(f"{appliance2_name}").click()
    
    page.get_by_role("button", name="Next").click()

    expect(page.get_by_text("Connecting to appliances...")).to_be_visible()

    expect(page.get_by_role("heading", level=2, name="Select volumes")).to_be_visible(timeout=100000)
    expect(page.get_by_text("Select one volume on each appliance to store the HA LUN data. Selected volumes must have identical storage configurations.")).to_be_visible()
    expect(page.get_by_text("Volumes have identical configurations")).to_be_visible()
    expect(page.get_by_text("Volume").nth(0)).to_be_visible()
    expect(page.get_by_text("State").nth(0)).to_be_visible()
    expect(page.get_by_text("Layout").nth(0)).to_be_visible()
    expect(page.get_by_text("Capacity").nth(0)).to_be_visible()
    expect(page.get_by_text("Free capacity").nth(0)).to_be_visible()
    expect(page.get_by_text("Type").nth(0)).to_be_visible()

    page.get_by_role("button", name="Next").click()

    expect(page.get_by_text("Gathering information, please wait...")).to_be_visible()

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
    expect(page.locator("div.markdown__wrapper.tooltip__text").get_by_text("The feature will be provided in the next version").nth(0)).to_be_visible()    
    page.get_by_role("heading", level=3, name="File share witness").hover()
    expect(page.locator("div.markdown__wrapper.tooltip__text").get_by_text("The feature will be provided in the next version").nth(1)).to_be_visible()

    page.get_by_role("button", name="Next").click()

    expect(page.get_by_role("heading", level=2, name="Set network channels")).to_be_visible()
    expect(page.get_by_text("Set interfaces to carry storage traffic, configure them with unique IP addresses, and specify subnet masks")).to_be_visible()
    expect(page.get_by_text("Assign and configure at least two interfaces on each node, one per role (one for Data and one for Replication)")).to_be_visible()
    expect(page.get_by_text("Ensure interfaces are connected to client hosts directly or through redundant switches")).to_be_visible()
    expect(page.get_by_role("button", name="Show sample network diagram")).to_be_visible()
    # expect(page.get_by_text("Network channel configuration is failed.")).to_be_visible()
    # expect(page.get_by_text("Assign at least two interfaces on each node, one per role (one for “Data” and one for “Replication”).")).to_be_visible()

    page.locator(".icon_tooltip__icon").hover()
    expect(page.locator("ul.wizards_network__info_block_tooltip_list li").filter(has_text="Management adapters: Used for heartbeat (monitoring the health of appliances).")).to_be_visible()
    expect(page.locator("ul.wizards_network__info_block_tooltip_list li").filter(has_text="Data adapters: Used for client network connections and heartbeat.")).to_be_visible()
    expect(page.locator("ul.wizards_network__info_block_tooltip_list li").filter(has_text="Replication adapters: Used for synchronous data replication between appliances.")).to_be_visible()
    
    expect(page.get_by_text("Interface").nth(0)).to_be_visible()
    expect(page.get_by_text("Link status").nth(0)).to_be_visible()
    expect(page.get_by_text("Adapter model").nth(0)).to_be_visible()
    expect(page.get_by_text("IP address").nth(0)).to_be_visible()
    expect(page.get_by_text("Management").nth(0)).to_be_visible()
    expect(page.get_by_text("Data").nth(0)).to_be_visible()
    expect(page.get_by_text("Replication").nth(0)).to_be_visible()

    # page.get_by_role("checkbox").nth(4).click()
    # page.locator("input[name=\"eth2\"]").nth(2).click()
    # page.locator("input[name=\"eth1\"]").nth(4).click()
    # page.locator("input[name=\"eth2\"]").nth(5).click()

    # expect(page.get_by_text("Network channel configuration is failed.")).not_to_be_visible()
    # expect(page.get_by_text("Assign at least two interfaces on each node, one per role (one for “Data” and one for “Replication”).")).not_to_be_visible()

    page.locator("input[name=\"eth2\"]").nth(1).click()

    expect(page.get_by_text("Network channel configuration is failed.")).to_be_visible()
    expect(page.get_by_text("Assign at least two interfaces on each node, one per role (one for “Data” and one for “Replication”).")).to_be_visible()

    page.locator("input[name=\"eth2\"]").nth(2).click()
    page.get_by_role("button", name="Next").click()

    expect(page.get_by_text("Testing network settings...")).to_be_visible()

    expect(page.get_by_role("heading", name="Non-redundant configuration", level=2).nth(0)).to_be_visible(timeout=100000)
    expect(page.get_by_text("Only 1 Replication network is configured. Configure more Replication networks to eliminate a single point of failure.")).to_be_visible()
    expect(page.get_by_text("We recommended assigning at least two data network interfaces to eliminate a single point of failure.").nth(0)).to_be_visible()
    expect(page.get_by_text("Acknowledge and continue?").nth(0)).to_be_visible()

    page.get_by_role("button", name="Yes, continue").nth(1).click()

    expect(page.get_by_role("heading", name="Non-redundant configuration", level=2)).to_be_visible()
    expect(page.get_by_text("Only 1 Data network is configured. Configure more Data networks to eliminate a single point of failure.")).to_be_visible()
    expect(page.get_by_text("We recommended assigning at least two data network interfaces to eliminate a single point of failure.")).to_be_visible()
    expect(page.get_by_text("Acknowledge and continue?")).to_be_visible()

    page.get_by_role("button", name="Yes, continue").click()

    expect(page.get_by_role("heading", level=2, name="Specify LUN settings")).to_be_visible()
    expect(page.get_by_text("Specify the NVMe-oF device name, transport type, and interfaces to create listeners for carrying storage traffic between clients")).to_be_visible()
    expect(page.get_by_text("Select at least one network interface on each node to create a listener. A Data network interface is recommended for simplified configuration")).to_be_visible()
    expect(page.get_by_text("Management and selected Data adapters are used for the purpose of a heartbeat to monitor the health of nodes")).to_be_visible()
    expect(page.get_by_text("Ensure interfaces are connected to client hosts directly or through redundant switches")).to_be_visible()
    expect(page.get_by_text("For switchless SR-IOV RDMA connectivity, you can use Replication adapters to create a listener")).to_be_visible()

    page.get_by_role("textbox").nth(0).click()
    page.get_by_text("TCP").click()
    expect(page.get_by_text("LUN name can not be empty")).to_be_visible()
    page.get_by_text("RDMA", exact=True).hover()
    expect(page.get_by_text("This type of transport requires one Data and one Replication network interface with RDMA capabilities.")).to_be_visible()
    
    page.get_by_text("Data").nth(2).click()
    page.get_by_text("Data").nth(3).click()

    expect(page.get_by_text("Selected number of network interfaces is equal")).to_be_visible()

    page.get_by_text("Replication").nth(2).click()

    expect(page.get_by_text("Selected number of network interfaces is not equal")).to_be_visible()

    page.get_by_text("Replication").nth(2).click()
    page.get_by_role("textbox").nth(0).fill("nlun2hatcp")
    page.get_by_role("button", name="Next").click()

    expect(page.get_by_role("heading", level=2, name="Review summary")).to_be_visible()
    expect(page.locator("div.ha__summary-name").nth(0)).to_contain_text("Protocol")
    expect(page.locator("div.ha__summary-description").nth(0)).to_contain_text("NVMe-oF")
    expect(page.locator("div.ha__summary-name").nth(1)).to_contain_text("LUN Availability")
    expect(page.locator("div.ha__summary-description").nth(1)).to_contain_text("High availability (two-way replication)")
    expect(page.locator("div.ha__summary-name").nth(2)).to_contain_text("Appliances")
    expect(page.locator("div.ha__summary-description").nth(2)).to_contain_text(f"{appliance1_name}{appliance2_name}")
    expect(page.locator("div.ha__summary-name").nth(3)).to_contain_text("Volumes")
    expect(page.locator("div.ha__summary-description").nth(3)).to_contain_text("rvolrvol")
    expect(page.locator("div.ha__summary-name").nth(4)).to_contain_text("Management IP addresses")
    expect(page.locator("div.ha__summary-description").nth(4)).to_contain_text(f"172.16.6.{appliance2_name}, 172.16.6.{appliance1_name}")
    expect(page.locator("div.ha__summary-name").nth(5)).to_contain_text("Data IP addresses")
    expect(page.locator("div.ha__summary-description").nth(5)).to_contain_text(f"14.14.14.{appliance2_name}, 14.14.14.{appliance1_name}")
    expect(page.locator("div.ha__summary-name").nth(6)).to_contain_text("Replication IP addresses")
    expect(page.locator("div.ha__summary-description").nth(6)).to_contain_text(f"15.15.15.{appliance2_name}, 15.15.15.{appliance1_name}")
    expect(page.locator("div.ha__summary-name").nth(7)).to_contain_text("Failover strategy")
    expect(page.locator("div.ha__summary-description").nth(7)).to_contain_text("Heartbeat")
    expect(page.locator("div.ha__summary-name").nth(8)).to_contain_text("LUN")
    expect(page.locator("div.ha__summary-description").nth(8)).to_contain_text("nlun2hatcp")
    expect(page.locator("div.ha__summary-name").nth(9)).to_contain_text("LUN size")
    expect(page.locator("div.ha__summary-description").nth(9)).to_contain_text("2 GB")
    expect(page.locator("div.ha__summary-name").nth(10)).to_contain_text("Transport type")
    expect(page.locator("div.ha__summary-description").nth(10)).to_contain_text("TCP")
    expect(page.locator("div.ha__summary-name").nth(11)).to_contain_text("Service port")
    expect(page.locator("div.ha__summary-description").nth(11)).to_contain_text("8009")
    expect(page.locator("div.ha__summary-name").nth(12)).to_contain_text("Transport IP addresses")
    expect(page.locator("div.ha__summary-description").nth(12)).to_contain_text(f"14.14.14.{appliance1_name}, 14.14.14.{appliance2_name}")


    page.locator('button.modalwindow__close_icon').click()  #close by pressing 'x'

    expect(page.get_by_text("Close Wizard")).to_be_visible()
    expect(page.get_by_text("Are you sure you want to close the wizard? All changes will be discarded.")).to_be_visible()

    page.locator('button.modalwindow__close_icon').nth(2).click()  #close by pressing 'x'
    page.locator('button.modalwindow__close_icon').click()  #close by pressing 'x'
    page.get_by_role("button", name="No, cancel").click()
    page.get_by_role("button", name="Create LUN").click()

    expect(page.get_by_role("row", name="nlun2hatcp")).to_be_visible(timeout=1000000)