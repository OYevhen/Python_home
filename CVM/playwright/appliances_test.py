from playwright.sync_api import Page, expect
import pytest

# from SeniorTester.test_parametrize import page



@pytest.mark.skip  
def test_add_appliance(page: Page): 
    page.context.ignore_https_errors = True
    page.goto('https://172.16.6.144')
    page.locator('input[type="text"]').first.fill('user')
    page.locator('input[type="password"]').fill('rds123RDS!@#')
    page.locator('span.checkbox-custom').click()
    page.get_by_role('button', name='Sign in').click()

    page.get_by_role('link', name='Appliances').click()
    page.get_by_role('button', name='Add Appliance').click()
    
    expect(page.get_by_role("heading", name="Credentials")).to_be_visible(timeout=10000)   
    expect(page.get_by_text("Specify the appliance IP address and its administrator credentials")).to_be_visible() 
    expect(page.get_by_text("The newly added appliance will be linked to already connected partners.")).to_be_visible() 
    
    page.get_by_role("textbox").nth(0).fill("172.16.6.145")
    page.get_by_role("textbox").nth(1).fill("user")
    page.locator("input[type='password']").fill("rds123RDS!@#")
    page.get_by_role("button", name="Next").click()
    
    expect(page.get_by_role("heading", name="Summary")).to_be_visible(timeout=100000)   
    expect(page.locator('div.windowsAppliances__summary-name').nth(0)).to_contain_text("Appliance name")
    expect(page.locator('div.windowsAppliances__summary-description').nth(0)).to_contain_text("145")
    expect(page.locator('div.windowsAppliances__summary-name').nth(1)).to_contain_text("Storage capacity")
    expect(page.locator('div.windowsAppliances__summary-description').nth(1)).to_contain_text("987.51 GB")
    expect(page.locator('div.windowsAppliances__summary-name').nth(2)).to_contain_text("Storage pools")
    expect(page.locator('div.windowsAppliances__summary-description').nth(2)).to_contain_text("0")
    expect(page.locator('div.windowsAppliances__summary-name').nth(3)).to_contain_text("Volumes")
    expect(page.locator('div.windowsAppliances__summary-description').nth(3)).to_contain_text("0")
    
    page.get_by_role("button", name="Add appliance").first.click()
    
    expect(page.locator('p[title="145"]')).to_be_visible(timeout=100000)

@pytest.mark.skip   
def test_add_duplicated_appliance(page: Page): 
    page.context.ignore_https_errors = True
    page.goto('https://172.16.6.144')
    page.locator('input[type="text"]').first.fill('user')
    page.locator('input[type="password"]').fill('rds123RDS!@#')
    page.locator('span.checkbox-custom').click()
    page.get_by_role('button', name='Sign in').click()

    page.get_by_role('link', name='Appliances').click()
    page.get_by_role('button', name='Add Appliance').click()   
    page.get_by_role("textbox").nth(0).fill("172.16.6.144")
    page.get_by_role("textbox").nth(1).fill("user")
    page.locator("input[type='password']").fill("rds123RDS!@#")
    page.get_by_role("button", name="Next").click()

    expect(page.get_by_text("Duplicate hostname detected")).to_be_visible(timeout=10000)
    expect(page.get_by_text("The appliances have the same name.")).to_be_visible()
    expect(page.get_by_text("Partners must have unique hostnames.")).to_be_visible()
    expect(page.get_by_text("Rename the partner appliances hostname in settings.")).to_be_visible()
    
    page.get_by_role("button", name="Close").first.click()
    page.locator('button.modalwindow__close_icon').click()  #close by pressing 'x'



# @pytest.mark.skip    
def test_remove_appliance(page: Page):
    page.context.ignore_https_errors = True
    page.goto('https://172.16.6.144')
    page.locator('input[type="text"]').first.fill('user')
    page.locator('input[type="password"]').fill('rds123RDS!@#')
    page.locator('span.checkbox-custom').click()
    page.get_by_role('button', name='Sign in').click()

    page.get_by_role('link', name='Appliances').click()
    page.locator('p[title="145"]').click()
    page.get_by_role("button").filter(has_text="Remove appliance").click()

    expect(page.get_by_role("heading", name="Remove appliance")).to_be_visible()
    expect(page.get_by_text("The appliance")).to_be_visible()
    expect(page.get_by_text("will be removed from the infrastructure")).to_be_visible()
    expect(page.get_by_text("Client sessions to all LUNs and file shares on the removed appliance will remain connected with no impact.")).to_be_visible()
    expect(page.get_by_text("The synchronization of existing HA LUNs with the removed appliance will not be interrupted.")).to_be_visible()
    expect(page.get_by_text("Reconfiguring HA LUNs on the removed appliance or creating new HA LUNs synchronized with the removed appliance will no longer be possible.")).to_be_visible()
    expect(page.get_by_text("Remove appliance?")).to_be_visible()

    page.get_by_role("button", name="Remove").click()

    expect(page.locator('p[title="145"]')).to_have_count(0, timeout=100000)