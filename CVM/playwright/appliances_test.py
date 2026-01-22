from playwright.sync_api import Page, expect


def test_add_appliance(page: Page): 
    page.context.ignore_https_errors = True
    page.goto('https://172.16.6.144')
    page.locator('input[type="text"]').first.fill('user')
    page.locator('input[type="password"]').fill('rds123RDS!@#')
    page.locator('span.checkbox-custom').click()
    expect(page.get_by_role('button', name='Sign in')).to_be_enabled()
    page.get_by_role('button', name='Sign in').click()

    # page.get_by_role('link', name='Appliances').click()
    # page.get_by_role('button', name='Add Appliance').click()
    # expect(page.get_by_role('button', name='Close')).to_be_clickable()
    # expect(page.get_by_role('button', name='Next')).to_be_disabled()
    # page.get_by_label('IP address').fill('172.16.6.145')
    # page.get_by_label('Administrator username').fill('user')
    # page.get_by_label('Administrator password').fill('rds123RDS!@#')
    # expect(page.get_by_role('button', name='Next')).to_be_clickable()
    # page.get_by_role('button', name='Next').click()
    # expect(page.get_by_text('Summary')).to_be_visible()
    # expect(page.get_by_role('button', name='Back')).to_be_clickable()
    # expect(page.get_by_role('button', name='Add appliance')).to_be_clickable()
    # page.get_by_role('button', name='Add appliance').click()
    # page.wait_for_timeout(5000)
    # page.get_by_label('Login').click()
    # page.get_by_label('Login').fill('user', force=True)


    # page.goto('https://172.16.6.144', wait_until='domcontentloaded')
    # page.wait_for_timeout(1000)
    
    # MUI inputs - find input within the parent container
