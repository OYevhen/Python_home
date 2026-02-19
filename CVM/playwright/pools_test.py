import re
from playwright.sync_api import Page, expect
import pytest
from units import *


#@pytest.mark.skip
def test_create_single_disk_pools(page: Page):
    cvm = CVM(page)
    cvm.login(URL1)

    # check if appliance 145 exists, if not, add it
    page.get_by_role('link', name='Appliances').click()
    if not page.locator(f'p[title="{appliance2_name}"]').is_visible():
        cvm.add_appliance()
    
    # check if there is pools already, if yes, delete them
    page.get_by_role('link', name='Storage pools').click()
    if not page.get_by_text("There are no storage pools yet").is_visible():
        cvm.delete_pools()

    expect(page.get_by_role("heading", name="Storage pools", exact=True)).to_be_visible()
    expect(page.get_by_text("There are no storage pools yet")).to_be_visible()
    expect(page.get_by_text("Start building your storage infrastructure by creating a new one")).to_be_visible()

    page.get_by_role("button").filter(has_text="Create a new pool").click()

    expect(page.get_by_role("heading", name="Prerequisites")).to_be_visible(timeout=100000)
    expect(page.get_by_text("Learn supported storage configuration:")).to_be_visible()
    expect(page.get_by_text("StarWind CVM is installed on each server that is used to configure highly available storage.")).to_be_visible()
    expect(page.get_by_text("StarWind CVM is installed on a separate storage device available to the hypervisor host (e.g. RAID volume, SSD, HDD, etc.).")).to_be_visible()
    expect(page.get_by_text("The hypervisor hosts have all the drives connected through an HBA or RAID controller.")).to_be_visible()
    expect(page.get_by_text("HBA or RAID controller will be added via a DirectPath I/O passthrough device to a StarWind CVM.")).to_be_visible()
    expect(page.get_by_text("For VMware vSphere environments, the disks can be added to StarWind VM as Raw Device Mapping (RDM). The link to VMware documentation is below:Add an RDM Disk to a Virtual Machine")).to_be_visible()
    expect(page.get_by_text("Please contactsupport@starwind.comto get assistance, if you are uncertain about what configuration to use with your storage.")).to_be_visible()

    page.get_by_role("button", name="Next").click()

    expect(page.get_by_role("heading", name="Appliance")).to_be_visible(timeout=100000)
    expect(page.get_by_text("Select one or more storage nodes to create a storage pool")).to_be_visible()
    expect(page.locator('p.wizard_table__table_header_title[title="Appliances"]')).to_be_visible()
    expect(page.get_by_text("Status")).to_be_visible()
    expect(page.get_by_text("Available disks")).to_be_visible()
    expect(page.get_by_text("Available capacity")).to_be_visible()
    
    page.get_by_role("row", name="Appliances Status Available").locator("span").click()
    page.get_by_role("row", name="Appliances Status Available").locator("span").click()
    page.get_by_text(f"{appliance1_name}").click()
    page.get_by_text(f"{appliance2_name}").click()
    page.get_by_role("button", name="Next").click()

    expect(page.get_by_role("heading", name="Physical disks", exact=True)).to_be_visible(timeout=100000)
    expect(page.get_by_text("Select physical disks to include in storage pools on each appliance")).to_be_visible()
    expect(page.get_by_text("Total raw capacity of selected disks:").nth(0)).to_be_visible()
    expect(page.get_by_text("Total raw capacity of selected disks:").nth(1)).to_be_visible()

    page.get_by_role("cell").first.click()

    expect(page.get_by_text("Selected number of disks is not equal")).to_be_visible()
    
    page.get_by_role("cell").filter(has_text=re.compile(r"^$")).nth(2).click()

    expect(page.get_by_text("Total raw capacity of selected disks:7 GB").nth(0)).to_be_visible()
    expect(page.get_by_text("Total raw capacity of selected disks:7 GB").nth(1)).to_be_visible()
    expect(page.get_by_text("Selected number of disks is equal")).to_be_visible()

    page.get_by_role("button", name="Next").click()

    expect(page.get_by_role("heading", name="Profile", exact=True)).to_be_visible(timeout=100000)
    expect(page.get_by_text("Choose an optimal storage pool profile. Selected disks left unused will be assigned to hot spares.")).to_be_visible()
    expect(page.get_by_text("Storage pool profile", exact=True)).to_be_visible()
    expect(page.get_by_text("Usable capacity")).to_be_visible()
    expect(page.get_by_text("Fault tolerance")).to_be_visible()
    expect(page.get_by_text("Hot spares", exact=True)).to_be_visible()

    page.get_by_role("radio").nth(1).check()
    page.get_by_role("radio").nth(0).check()
    page.get_by_role("button", name="Next").click()

    expect(page.get_by_role("heading", name="Summary", exact=True)).to_be_visible(timeout=100000)
    expect(page.get_by_text("Review specified settings and create storage pools.")).to_be_visible()
    expect(page.get_by_text(f"{appliance1_name}")).to_be_visible()
    expect(page.locator('p.pool_summary_item__list_item_title').nth(0)).to_contain_text("Storage pool layout")
    expect(page.locator('p.pool_summary_item__list_item_value').nth(0)).to_contain_text("Single disk")
    expect(page.locator('p.pool_summary_item__list_item_title').nth(1)).to_contain_text("Raw capacity")
    expect(page.locator('p.pool_summary_item__list_item_value').nth(1)).to_contain_text("7 GB")
    expect(page.locator('p.pool_summary_item__list_item_title').nth(2)).to_contain_text("Usable capacity")
    expect(page.locator('p.pool_summary_item__list_item_value').nth(2)).to_contain_text("7  GB")
    expect(page.get_by_text(f"{appliance2_name}")).to_be_visible()
    expect(page.locator('p.pool_summary_item__list_item_title').nth(3)).to_contain_text("Storage pool layout")
    expect(page.locator('p.pool_summary_item__list_item_value').nth(3)).to_contain_text("Single disk")
    expect(page.locator('p.pool_summary_item__list_item_title').nth(4)).to_contain_text("Raw capacity")
    expect(page.locator('p.pool_summary_item__list_item_value').nth(4)).to_contain_text("7 GB")
    expect(page.locator('p.pool_summary_item__list_item_title').nth(5)).to_contain_text("Usable capacity")
    expect(page.locator('p.pool_summary_item__list_item_value').nth(5)).to_contain_text("7  GB")

    page.locator('button.modalwindow__close_icon').click()  #close by pressing 'x'

    expect(page.get_by_text("Close Wizard")).to_be_visible()
    expect(page.get_by_text("Are you sure you want to close the wizard? All changes will be discarded.")).to_be_visible()

    page.locator('button.modalwindow__close_icon').nth(2).click()  #close by pressing 'x'
    page.locator('button.modalwindow__close_icon').click()  #close by pressing 'x'
    page.get_by_role("button", name="No, cancel").click()
    page.get_by_role("button", name="Create").click()
    
    expect(page.locator(f'p[title="{appliance1_name}"]')).to_be_visible(timeout=100000)
    expect(page.locator(f'p[title="{appliance2_name}"]')).to_be_visible(timeout=100000)


#@pytest.mark.skip
def test_delete_single_disk_pools(page: Page):
    cvm = CVM(page)
    cvm.login(URL1)

    # check if pools exist, if not, create them
    page.get_by_role('link', name='Storage pools').click()
    if not page.locator(f'p[title="{appliance1_name}"]').is_visible() or not page.locator(f'p[title="{appliance2_name}"]').is_visible():
        cvm.create_single_disk_pools()

    page.get_by_role("row", name="Name Type State Layout").locator("span").click()
    page.get_by_role("row", name=f"{appliance1_name}").locator("span").click()
    page.get_by_role("row", name=f"{appliance2_name}").locator("span").click()
    page.get_by_role("row", name=f"{appliance2_name}").locator("span").click()
    page.get_by_role("row", name=f"{appliance1_name}").locator("span").click()
    page.get_by_role("button").filter(has_text="Delete pool(s)").click()

    expect(page.get_by_role("heading", name="Delete storage pools")).to_be_visible(timeout=100000)
    expect(page.get_by_text("Delete2selectedstorage pools")).to_be_visible()
    expect(page.get_by_text("This action will permanently destroy selected storage pools")).to_be_visible()


    page.get_by_role("button").nth(3).click()
    page.get_by_role("button").filter(has_text="Delete pool(s)").click()
    page.get_by_role("button", name="Cancel").click()
    page.get_by_role("button").filter(has_text="Delete pool(s)").click()
    page.get_by_role("button", name="Delete").click()

    expect(page.locator(f'p[title="{appliance1_name}"]')).to_have_count(0, timeout=100000)
    expect(page.locator(f'p[title="{appliance2_name}"]')).to_have_count(0, timeout=100000)
    expect(page.get_by_text("There are no storage pools yet")).to_be_visible()
    expect(page.get_by_text("Start building your storage infrastructure by creating a new one")).to_be_visible()
