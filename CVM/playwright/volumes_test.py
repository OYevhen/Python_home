from playwright.sync_api import Page, expect
import pytest
from units import *


@pytest.mark.skip
def test_create_standard_volumes(page: Page):
    cvm = CVM(page)
    cvm.login(URL1)

    # check if appliance 145 exists, if not, add it
    page.get_by_role('link', name='Appliances').click()
    if not page.locator(f'p[title="{appliance2_name}"]').is_visible():
        cvm.add_appliance()

    # check if pools exist, if not, create them
    page.get_by_role('link', name='Storage pools').click()
    if page.get_by_text("There are no storage pools yet").is_visible():
        cvm.create_single_disk_pools()    
    
    page.get_by_role('link', name='Volumes').click()

    expect(page.get_by_role("heading", name="Volumes", exact=True)).to_be_visible()
    expect(page.get_by_text("There are no volumes yet")).to_be_visible()
    expect(page.get_by_text("Start sharing your storage resources to clients by creating a new one")).to_be_visible()

    page.get_by_role("button").filter(has_text="Create a new volume").click()

    expect(page.get_by_role("heading", name="Select file system type")).to_be_visible(timeout=100000)
    expect(page.get_by_text("Choose the preferred file system type for the new volume")).to_be_visible()
    expect(page.get_by_text("Standard")).to_be_visible()
    expect(page.get_by_text("XFS volume used for creating iSCSI LUNs, file shares, and VTL devices")).to_be_visible()
    expect(page.get_by_text("Raw")).to_be_visible()
    expect(page.get_by_text("Unformatted volume used for creating NVMe-oF LUNs")).to_be_visible()
    expect(page.get_by_text("Backup repository", exact=True)).to_be_visible()
    expect(page.get_by_text("XFS volume with reflink (data block sharing) and CRC enabled, used for creating hardened backup repositories")).to_be_visible()

    page.get_by_role("radio").nth(1).check()
    page.get_by_role("radio").nth(2).check()
    page.get_by_role("radio").nth(0).check()

    page.get_by_role("button", name="Next").click()

    expect(page.get_by_role("heading", name="Select storage pool", exact=True)).to_be_visible()
    expect(page.get_by_text("Select a storage pool with at least 2 GB of free capacity to create a volume.")).to_be_visible()
    expect(page.get_by_text("Name")).to_be_visible()
    expect(page.get_by_text("Type", exact=True)).to_be_visible()
    expect(page.get_by_text("State")).to_be_visible()
    expect(page.get_by_text("Layout")).to_be_visible()
    expect(page.get_by_text("Free capacity", exact=True)).to_be_visible()

    page.get_by_role("button", name="Next").click()
    page.locator(".checkbox-custom").nth(0).click()
    page.locator(".checkbox-custom").nth(1).click() # page.locator("tr:nth-child(2) > .wizard_table__table_body_checkbox_wrapper > .checkbox-label > .checkbox-custom").click()
    page.locator(".checkbox-custom").nth(1).click() # page.locator("tr:nth-child(2) > .wizard_table__table_body_checkbox_wrapper > .checkbox-label > .checkbox-custom").click()
    page.locator(".checkbox-custom").nth(0).click()
    page.locator(".checkbox-custom").nth(1).click() # page.locator("tr:nth-child(2) > .wizard_table__table_body_checkbox_wrapper > .checkbox-label > .checkbox-custom").click()
    page.locator(".checkbox-custom").nth(0).click()
    page.get_by_role("button", name="Next").click()

    expect(page.get_by_role("heading", name="Specify volume settings", exact=True)).to_be_visible()
    expect(page.get_by_text("Set the volume name and size")).to_be_visible()
    expect(page.get_by_text("Only Latin letters, numbers, and dashes are allowed")).to_be_visible()
    expect(page.get_by_text("At least 2 GB (up to ")).to_be_visible()

    page.get_by_role("textbox").nth(0).fill("svol")
    page.get_by_text("GB", exact=True).click()
    page.get_by_text("MB", exact=True).click()
    page.get_by_text("MB", exact=True).click()
    page.get_by_text("TB", exact=True).click()
    page.get_by_text("TB", exact=True).click()
    page.get_by_text("GB", exact=True).click()
    page.get_by_role("textbox").nth(1).fill("2")
    page.get_by_role("button", name="Next").click()

    expect(page.get_by_role("heading", name="Summary")).to_be_visible(timeout=100000)
    expect(page.get_by_text("Review your settings before creating a volume")).to_be_visible()
    expect(page.locator('span.windowsVolumes__summary-titleName').filter(has_text=f"{appliance1_name}")).to_be_visible()
    expect(page.locator('div.windowsVolumes__summary-name').nth(0)).to_contain_text("Storage pool")
    expect(page.locator('span.windowsVolumes__summary-description_dotted_text').filter(has_text=f"{appliance1_name}:")).to_be_visible()
    expect(page.locator('div.windowsVolumes__summary-name').nth(1)).to_contain_text("Volume name")
    expect(page.locator('div.windowsVolumes__summary-description').nth(1)).to_contain_text("svol")
    expect(page.locator('div.windowsVolumes__summary-name').nth(2)).to_contain_text("Size")
    expect(page.locator('div.windowsVolumes__summary-description').nth(2)).to_contain_text("2 GB")
    expect(page.locator('div.windowsVolumes__summary-name').nth(3)).to_contain_text("Filesystem settings")
    expect(page.locator('div.windowsVolumes__summary-description').nth(3)).to_contain_text("Standard")
    expect(page.locator('span.windowsVolumes__summary-titleName').filter(has_text=f"{appliance2_name}")).to_be_visible()
    expect(page.locator('div.windowsVolumes__summary-name').nth(4)).to_contain_text("Storage pool")
    expect(page.locator('span.windowsVolumes__summary-description_dotted_text').filter(has_text=f"{appliance2_name}:")).to_be_visible()
    expect(page.locator('div.windowsVolumes__summary-name').nth(5)).to_contain_text("Volume name")
    expect(page.locator('div.windowsVolumes__summary-description').nth(5)).to_contain_text("svol")
    expect(page.locator('div.windowsVolumes__summary-name').nth(6)).to_contain_text("Size")
    expect(page.locator('div.windowsVolumes__summary-description').nth(6)).to_contain_text("2 GB")
    expect(page.locator('div.windowsVolumes__summary-name').nth(7)).to_contain_text("Filesystem settings")
    expect(page.locator('div.windowsVolumes__summary-description').nth(7)).to_contain_text("Standard")

    page.locator('button.modalwindow__close_icon').click()  #close by pressing 'x'

    expect(page.get_by_text("Close Wizard")).to_be_visible()
    expect(page.get_by_text("Are you sure you want to close the wizard? All changes will be discarded.")).to_be_visible()

    page.locator('button.modalwindow__close_icon').nth(2).click()  #close by pressing 'x'
    page.locator('button.modalwindow__close_icon').click()  #close by pressing 'x'
    page.get_by_role("button", name="No, cancel").click()
    page.get_by_role("button", name="Create").click()
    
    expect(page.locator('tr').filter(has=page.locator(f'p[title="{appliance1_name}"]')).locator(f'p[title="Standard"]')).to_be_visible(timeout=100000)
    expect(page.locator('tr').filter(has=page.locator(f'p[title="{appliance2_name}"]')).locator(f'p[title="Standard"]')).to_be_visible(timeout=100000)

@pytest.mark.skip
def test_delete_standard_volumes(page: Page):
    cvm = CVM(page)
    cvm.login(URL1)

    page.get_by_role('link', name='Volumes').click()
    if not page.locator('tr').filter(has=page.locator(f'p[title="{appliance1_name}"]')).locator(f'p[title="Standard"]').is_visible() or not page.locator('tr').filter(has=page.locator(f'p[title="{appliance2_name}"]')).locator(f'p[title="Standard"]').is_visible():
        cvm.create_standard_volumes()

    page.locator('tr').filter(has=page.locator(f'p[title="{appliance1_name}"]')).filter(has=page.locator(f'p[title="Standard"]')).locator('span.checkbox-custom').click()
    page.locator('tr').filter(has=page.locator(f'p[title="{appliance2_name}"]')).filter(has=page.locator(f'p[title="Standard"]')).locator('span.checkbox-custom').click()
    page.get_by_role("button").filter(has_text="Delete volume(s)").click()

    expect(page.get_by_role("heading", name="Delete volumes")).to_be_visible()
    expect(page.locator('div.confirm_wizardNew__warning_bl_item', has_text="svol")).to_have_count(2)
    expect(page.get_by_text("Delete2selectedvolumes")).to_be_visible()
    expect(page.get_by_text("This action will permanently delete the selected volumes")).to_be_visible()


    page.get_by_role("button").nth(3).click()
    page.get_by_role("button").filter(has_text="Delete volume(s)").click()
    page.get_by_role("button", name="Cancel").click()
    page.get_by_role("button").filter(has_text="Delete volume(s)").click()
    page.get_by_role("button", name="Delete").click()


    expect(page.locator('tr').filter(has=page.locator(f'p[title="{appliance1_name}"]')).locator(f'p[title="Standard"]')).not_to_be_visible(timeout=100000)
    expect(page.locator('tr').filter(has=page.locator(f'p[title="{appliance2_name}"]')).locator(f'p[title="Standard"]')).not_to_be_visible(timeout=100000)


# @pytest.mark.skip
def test_create_raw_volumes(page: Page):
    cvm = CVM(page)
    cvm.login(URL1)

    # check if appliance 145 exists, if not, add it
    page.get_by_role('link', name='Appliances').click()
    if not page.locator(f'p[title="{appliance2_name}"]').is_visible():
        cvm.add_appliance()

    # check if pools exist, if not, create them
    page.get_by_role('link', name='Storage pools').click()
    if not page.locator(f'p[title="{appliance1_name}"]').is_visible() or not page.locator(f'p[title="{appliance2_name}"]').is_visible():
        expect(page.get_by_text("There are no volumes yet")).to_be_visible()
        expect(page.get_by_text("Start sharing your storage resources to clients by creating a new one")).to_be_visible()
        cvm.create_single_disk_pools()    
    
    page.get_by_role('link', name='Volumes').click()

    expect(page.get_by_role("heading", name="Volumes", exact=True)).to_be_visible()

    page.get_by_role("button").filter(has_text="Create a new volume").click()

    expect(page.get_by_role("heading", name="Select file system type")).to_be_visible(timeout=100000)
    expect(page.get_by_text("Choose the preferred file system type for the new volume")).to_be_visible()
    # expect(page.get_by_text("Standard")).to_be_visible()
    # expect(page.get_by_text("Standard")).to_be_visible()
    expect(page.get_by_text("XFS volume used for creating iSCSI LUNs, file shares, and VTL devices")).to_be_visible()
    expect(page.get_by_text("Raw")).to_be_visible()
    expect(page.get_by_text("Unformatted volume used for creating NVMe-oF LUNs")).to_be_visible()
    expect(page.get_by_text("Backup repository", exact=True)).to_be_visible()
    expect(page.get_by_text("XFS volume with reflink (data block sharing) and CRC enabled, used for creating hardened backup repositories")).to_be_visible()

    page.get_by_role("radio").nth(1).check()
    page.get_by_role("radio").nth(2).check()
    page.get_by_role("radio").nth(1).check()
    page.get_by_role("button", name="Next").click()

    expect(page.get_by_role("heading", name="Select storage pool", exact=True)).to_be_visible()
    expect(page.get_by_text("Select a storage pool with at least 2 GB of free capacity to create a volume.")).to_be_visible()
    expect(page.get_by_text("Name").nth(0)).to_be_visible()
    expect(page.get_by_text("Type", exact=True).nth(0)).to_be_visible()
    expect(page.get_by_text("State").nth(0)).to_be_visible()
    expect(page.get_by_text("Layout").nth(0)).to_be_visible()
    expect(page.get_by_text("Free capacity", exact=True).nth(0)).to_be_visible()

    page.locator(".checkbox-custom").nth(0).click()
    page.locator(".checkbox-custom").nth(1).click()
    page.get_by_role("button", name="Next").click()

    expect(page.get_by_role("heading", name="Specify volume settings", exact=True)).to_be_visible()
    expect(page.get_by_text("Set the volume name and size")).to_be_visible()
    expect(page.get_by_text("Only Latin letters, numbers, and dashes are allowed")).to_be_visible()
    expect(page.get_by_text("At least 2 GB (up to ")).to_be_visible()

    page.get_by_role("textbox").nth(0).fill("rvol")
    page.get_by_text("GB", exact=True).click()
    page.get_by_text("MB", exact=True).click()
    page.get_by_text("MB", exact=True).click()
    page.get_by_text("TB", exact=True).click()
    page.get_by_text("TB", exact=True).click()
    page.get_by_text("GB", exact=True).click()
    page.get_by_role("textbox").nth(1).fill("2")
    page.get_by_role("button", name="Next").click()

    expect(page.get_by_role("heading", name="Summary")).to_be_visible(timeout=100000)
    expect(page.get_by_text("Review your settings before creating a volume")).to_be_visible()
    expect(page.locator('span.windowsVolumes__summary-titleName').filter(has_text=f"{appliance1_name}")).to_be_visible()
    expect(page.locator('div.windowsVolumes__summary-name').nth(0)).to_contain_text("Storage pool")
    expect(page.locator('span.windowsVolumes__summary-description_dotted_text').filter(has_text=f"{appliance1_name}:")).to_be_visible()
    expect(page.locator('div.windowsVolumes__summary-name').nth(1)).to_contain_text("Volume name")
    expect(page.locator('div.windowsVolumes__summary-description').nth(1)).to_contain_text("rvol")
    expect(page.locator('div.windowsVolumes__summary-name').nth(2)).to_contain_text("Size")
    expect(page.locator('div.windowsVolumes__summary-description').nth(2)).to_contain_text("2 GB")
    expect(page.locator('div.windowsVolumes__summary-name').nth(3)).to_contain_text("Filesystem settings")
    expect(page.locator('div.windowsVolumes__summary-description').nth(3)).to_contain_text("Raw")
    expect(page.locator('span.windowsVolumes__summary-titleName').filter(has_text=f"{appliance2_name}")).to_be_visible()
    expect(page.locator('div.windowsVolumes__summary-name').nth(4)).to_contain_text("Storage pool")
    expect(page.locator('span.windowsVolumes__summary-description_dotted_text').filter(has_text=f"{appliance2_name}:")).to_be_visible()
    expect(page.locator('div.windowsVolumes__summary-name').nth(5)).to_contain_text("Volume name")
    expect(page.locator('div.windowsVolumes__summary-description').nth(5)).to_contain_text("rvol")
    expect(page.locator('div.windowsVolumes__summary-name').nth(6)).to_contain_text("Size")
    expect(page.locator('div.windowsVolumes__summary-description').nth(6)).to_contain_text("2 GB")
    expect(page.locator('div.windowsVolumes__summary-name').nth(7)).to_contain_text("Filesystem settings")
    expect(page.locator('div.windowsVolumes__summary-description').nth(7)).to_contain_text("Raw")

    page.locator('button.modalwindow__close_icon').click()  #close by pressing 'x'

    expect(page.get_by_text("Close Wizard")).to_be_visible()
    expect(page.get_by_text("Are you sure you want to close the wizard? All changes will be discarded.")).to_be_visible()

    page.locator('button.modalwindow__close_icon').nth(2).click()  #close by pressing 'x'
    page.locator('button.modalwindow__close_icon').click()  #close by pressing 'x'
    page.get_by_role("button", name="No, cancel").click()
    page.get_by_role("button", name="Create").click()
    
    expect(page.locator('tr').filter(has=page.locator(f'p[title="{appliance1_name}"]')).locator(f'p[title="Raw"]')).to_be_visible(timeout=100000)
    expect(page.locator('tr').filter(has=page.locator(f'p[title="{appliance2_name}"]')).locator(f'p[title="Raw"]')).to_be_visible(timeout=100000)    


@pytest.mark.skip
def test_delete_raw_volumes(page: Page):
    cvm = CVM(page)
    cvm.login(URL1)

    page.get_by_role('link', name='Volumes').click()
    if not page.locator('tr').filter(has=page.locator(f'p[title="{appliance1_name}"]')).locator(f'p[title="Raw"]').is_visible() or not page.locator('tr').filter(has=page.locator(f'p[title="{appliance2_name}"]')).locator(f'p[title="Raw"]').is_visible():
        cvm.create_raw_volumes()

    page.locator('tr').filter(has=page.locator(f'p[title="{appliance1_name}"]')).filter(has=page.locator(f'p[title="Raw"]')).locator('span.checkbox-custom').click()
    page.locator('tr').filter(has=page.locator(f'p[title="{appliance2_name}"]')).filter(has=page.locator(f'p[title="Raw"]')).locator('span.checkbox-custom').click()
    page.get_by_role("button").filter(has_text="Delete volume(s)").click()

    expect(page.get_by_role("heading", name="Delete volumes")).to_be_visible()
    expect(page.locator('div.confirm_wizardNew__warning_bl_item', has_text="rvol")).to_have_count(2)
    expect(page.get_by_text("Delete2selectedvolumes")).to_be_visible()
    expect(page.get_by_text("This action will permanently delete the selected volumes")).to_be_visible()


    page.get_by_role("button").nth(3).click()
    page.get_by_role("button").filter(has_text="Delete volume(s)").click()
    page.get_by_role("button", name="Cancel").click()
    page.get_by_role("button").filter(has_text="Delete volume(s)").click()
    page.get_by_role("button", name="Delete").click()


    expect(page.locator('tr').filter(has=page.locator(f'p[title="{appliance1_name}"]')).locator(f'p[title="Raw"]')).not_to_be_visible(timeout=100000)
    expect(page.locator('tr').filter(has=page.locator(f'p[title="{appliance2_name}"]')).locator(f'p[title="Raw"]')).not_to_be_visible(timeout=100000)


@pytest.mark.skip
def test_create_backup_volumes(page: Page):
    cvm = CVM(page)
    cvm.login(URL1)

    # check if appliance 145 exists, if not, add it
    page.get_by_role('link', name='Appliances').click()
    if not page.locator(f'p[title="{appliance2_name}"]').is_visible():
        cvm.add_appliance()

    # check if pools exist, if not, create them
    page.get_by_role('link', name='Storage pools').click()
    if not page.locator(f'p[title="{appliance1_name}"]').is_visible() or not page.locator(f'p[title="{appliance2_name}"]').is_visible():
        expect(page.get_by_text("There are no volumes yet")).to_be_visible()
        expect(page.get_by_text("Start sharing your storage resources to clients by creating a new one")).to_be_visible()
        cvm.create_single_disk_pools()    
    
    page.get_by_role('link', name='Volumes').click()

    expect(page.get_by_role("heading", name="Volumes", exact=True)).to_be_visible()

    page.get_by_role("button").filter(has_text="Create a new volume").click()

    expect(page.get_by_role("heading", name="Select file system type")).to_be_visible(timeout=100000)
    expect(page.get_by_text("Choose the preferred file system type for the new volume")).to_be_visible()
    expect(page.get_by_text("Standard")).to_be_visible()
    expect(page.get_by_text("XFS volume used for creating iSCSI LUNs, file shares, and VTL devices")).to_be_visible()
    expect(page.get_by_text("Raw")).to_be_visible()
    expect(page.get_by_text("Unformatted volume used for creating NVMe-oF LUNs")).to_be_visible()
    expect(page.get_by_text("Backup repository", exact=True)).to_be_visible()
    expect(page.get_by_text("XFS volume with reflink (data block sharing) and CRC enabled, used for creating hardened backup repositories")).to_be_visible()

    page.get_by_role("radio").nth(1).check()
    page.get_by_role("radio").nth(2).check()
    page.get_by_role("button", name="Next").click()

    expect(page.get_by_role("heading", name="Select storage pool", exact=True)).to_be_visible()
    expect(page.get_by_text("Select a storage pool with at least 2 GB of free capacity to create a volume.")).to_be_visible()
    expect(page.get_by_text("Name")).to_be_visible()
    expect(page.get_by_text("Type", exact=True)).to_be_visible()
    expect(page.get_by_text("State")).to_be_visible()
    expect(page.get_by_text("Layout")).to_be_visible()
    expect(page.get_by_text("Free capacity", exact=True)).to_be_visible()

    page.get_by_role("button", name="Next").click()
    page.locator(".checkbox-custom").nth(0).click()
    page.locator(".checkbox-custom").nth(1).click()
    page.locator(".checkbox-custom").nth(1).click()
    page.locator(".checkbox-custom").nth(0).click()
    page.locator(".checkbox-custom").nth(1).click()
    page.locator(".checkbox-custom").nth(0).click()
    page.get_by_role("button", name="Next").click()

    expect(page.get_by_role("heading", name="Specify volume settings", exact=True)).to_be_visible()
    expect(page.get_by_text("Set the volume name and size")).to_be_visible()
    expect(page.get_by_text("Only Latin letters, numbers, and dashes are allowed")).to_be_visible()
    expect(page.get_by_text("At least 2 GB (up to ")).to_be_visible()

    page.get_by_role("textbox").nth(0).fill("bvol")
    page.get_by_text("GB", exact=True).click()
    page.get_by_text("MB", exact=True).click()
    page.get_by_text("MB", exact=True).click()
    page.get_by_text("TB", exact=True).click()
    page.get_by_text("TB", exact=True).click()
    page.get_by_text("GB", exact=True).click()
    page.get_by_role("textbox").nth(1).fill("2")
    page.get_by_role("button", name="Next").click()

    expect(page.get_by_role("heading", name="Summary")).to_be_visible(timeout=100000)
    expect(page.get_by_text("Review your settings before creating a volume")).to_be_visible()
    expect(page.locator('span.windowsVolumes__summary-titleName').filter(has_text="144")).to_be_visible()
    expect(page.locator('div.windowsVolumes__summary-name').nth(0)).to_contain_text("Storage pool")
    expect(page.locator('span.windowsVolumes__summary-description_dotted_text').filter(has_text="144:")).to_be_visible()
    expect(page.locator('div.windowsVolumes__summary-name').nth(1)).to_contain_text("Volume name")
    expect(page.locator('div.windowsVolumes__summary-description').nth(1)).to_contain_text("bvol")
    expect(page.locator('div.windowsVolumes__summary-name').nth(2)).to_contain_text("Size")
    expect(page.locator('div.windowsVolumes__summary-description').nth(2)).to_contain_text("2 GB")
    expect(page.locator('div.windowsVolumes__summary-name').nth(3)).to_contain_text("Filesystem settings")
    expect(page.locator('div.windowsVolumes__summary-description').nth(3)).to_contain_text("Backup repository")
    expect(page.locator('span.windowsVolumes__summary-titleName').filter(has_text="145")).to_be_visible()
    expect(page.locator('div.windowsVolumes__summary-name').nth(4)).to_contain_text("Storage pool")
    expect(page.locator('span.windowsVolumes__summary-description_dotted_text').filter(has_text="145:")).to_be_visible()
    expect(page.locator('div.windowsVolumes__summary-name').nth(5)).to_contain_text("Volume name")
    expect(page.locator('div.windowsVolumes__summary-description').nth(5)).to_contain_text("bvol")
    expect(page.locator('div.windowsVolumes__summary-name').nth(6)).to_contain_text("Size")
    expect(page.locator('div.windowsVolumes__summary-description').nth(6)).to_contain_text("2 GB")
    expect(page.locator('div.windowsVolumes__summary-name').nth(7)).to_contain_text("Filesystem settings")
    expect(page.locator('div.windowsVolumes__summary-description').nth(7)).to_contain_text("Backup repository")

    page.locator('button.modalwindow__close_icon').click()  #close by pressing 'x'

    expect(page.get_by_text("Close Wizard")).to_be_visible()
    expect(page.get_by_text("Are you sure you want to close the wizard? All changes will be discarded.")).to_be_visible()

    page.locator('button.modalwindow__close_icon').nth(2).click()  #close by pressing 'x'
    page.locator('button.modalwindow__close_icon').click()  #close by pressing 'x'
    page.get_by_role("button", name="No, cancel").click()
    page.get_by_role("button", name="Create").click()
    
    expect(page.locator('tr').filter(has=page.locator(f'p[title="{appliance1_name}"]')).locator('p[title="Backup repository"]')).to_be_visible(timeout=100000)
    expect(page.locator('tr').filter(has=page.locator(f'p[title="{appliance2_name}"]')).locator('p[title="Backup repository"]')).to_be_visible(timeout=100000)  


@pytest.mark.skip
def test_delete_backup_volumes(page: Page):
    cvm = CVM(page)
    cvm.login(URL1)

    page.get_by_role('link', name='Volumes').click()
    if not page.locator('tr').filter(has=page.locator(f'p[title="{appliance1_name}"]')).locator('p[title="Backup repository"]').is_visible() or not page.locator('tr').filter(has=page.locator(f'p[title="{appliance2_name}"]')).locator('p[title="Backup repository"]').is_visible():
        cvm.create_backup_volumes()

    page.locator('tr').filter(has=page.locator(f'p[title="{appliance1_name}"]')).filter(has=page.locator('p[title="Backup repository"]')).locator('span.checkbox-custom').click()
    page.locator('tr').filter(has=page.locator(f'p[title="{appliance2_name}"]')).filter(has=page.locator('p[title="Backup repository"]')).locator('span.checkbox-custom').click()
    page.get_by_role("button").filter(has_text="Delete volume(s)").click()

    expect(page.get_by_role("heading", name="Delete volumes")).to_be_visible()
    expect(page.locator('div.confirm_wizardNew__warning_bl_item', has_text="bvol")).to_have_count(2)
    expect(page.get_by_text("Delete2selectedvolumes")).to_be_visible()
    expect(page.get_by_text("This action will permanently delete the selected volumes")).to_be_visible()


    page.get_by_role("button").nth(3).click()
    page.get_by_role("button").filter(has_text="Delete volume(s)").click()
    page.get_by_role("button", name="Cancel").click()
    page.get_by_role("button").filter(has_text="Delete volume(s)").click()
    page.get_by_role("button", name="Delete").click()


    expect(page.locator('tr').filter(has=page.locator(f'p[title="{appliance1_name}"]')).locator('p[title="Backup repository"]')).not_to_be_visible(timeout=100000)
    expect(page.locator('tr').filter(has=page.locator(f'p[title="{appliance2_name}"]')).locator('p[title="Backup repository"]')).not_to_be_visible(timeout=100000)