from playwright.sync_api import expect


URL1 = "https://172.16.6.164/"
URL2 = "https://172.16.6.165/"
username = "user"
password = "rds123RDS!@#"
appliance1_name = f"{URL1.split('.')[-1].rstrip('/')}"
appliance2_name = f"{URL2.split('.')[-1].rstrip('/')}"


class CVM:

    def __init__(self, page):
        self.page = page

    def login(self, URL):
        self.page.context.ignore_https_errors = True
        self.page.goto(URL)
        self.page.locator('input[type="text"]').first.fill(username)
        self.page.locator('input[type="password"]').fill(password)
        self.page.get_by_role('button', name='Sign in').click()

    def add_appliance(self):
        self.page.get_by_role('link', name='Appliances').click()
        self.page.get_by_role('button', name='Add Appliance').click()
        self.page.get_by_role("textbox").nth(0).fill(f'{URL2.removeprefix("https://").removesuffix("/")}')   
        self.page.get_by_role("textbox").nth(1).fill(username)
        self.page.locator("input[type='password']").fill(password)
        self.page.get_by_role("button", name="Next").click()
        expect(self.page.get_by_role("heading", name="Summary")).to_be_visible(timeout=100000)   
        self.page.get_by_role("button", name="Add appliance").first.click()
        expect(self.page.locator(f'p[title="{appliance2_name}"]')).to_be_visible(timeout=100000)

    def remove_appliance(self):
        self.page.get_by_role('link', name='Appliances').click()
        self.page.locator(f'p[title="{appliance2_name}"]').click()
        self.page.get_by_role("button").filter(has_text="Remove appliance").click()
        self.page.get_by_role("button", name="Remove").click()
        expect(self.page.locator(f'p[title="{appliance2_name}"]')).to_have_count(0, timeout=100000)

    def create_single_disk_pools(self):
        self.page.get_by_role('link', name='Storage pools').click()
        self.page.get_by_role("button").filter(has_text="Create a new pool").click()
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("row", name="Appliances Status Available").locator("span").click()
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("row", name="sda HDD SAS 931.51 GB 32:0:1:").locator("span").click()
        if not self.page.get_by_role("row", name="sdi HDD SAS 931.51 GB 33:0:6:").is_visible():
            self.page.locator(".buttonMin__wrapper.buttonMin__wrapper--arrow_right").click()
        self.page.get_by_role("row", name="sdi HDD SAS 931.51 GB 33:0:6:").locator("span").click()
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("button", name="Create").click()
        expect(self.page.locator(f'p[title="{appliance1_name}"]')).to_be_visible(timeout=100000)
        expect(self.page.locator(f'p[title="{appliance2_name}"]')).to_be_visible(timeout=100000)

    def delete_single_disk_pools(self):
        self.page.get_by_role('link', name='Storage pools').click()
        self.page.locator(f'p[title="{appliance1_name}"]').click()
        self.page.locator(f'p[title="{appliance2_name}"]').click()
        self.page.get_by_role("button").filter(has_text="Delete pool(s)").click()
        self.page.get_by_role("button", name="Delete").click()
        expect(self.page.locator(f'p[title="{appliance1_name}"]')).to_be_visible(timeout=100000)
        expect(self.page.locator(f'p[title="{appliance2_name}"]')).to_be_visible(timeout=100000)
    
    def create_standard_volumes(self):
        self.page.get_by_role("button").filter(has_text="Create a new volume").click()
        self.page.get_by_role("button", name="Next").click()
        self.page.locator(".checkbox-custom").first.click()
        self.page.locator("tr:nth-child(2) > .wizard_table__table_body_checkbox_wrapper > .checkbox-label > .checkbox-custom").click()
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("textbox").nth(0).fill("svol")
        self.page.get_by_role("textbox").nth(1).fill("2")
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("button", name="Create").click()
        
        expect(self.page.locator('tr').filter(has=self.page.locator(f'p[title="{appliance1_name}"]')).locator('p[title="Standard"]')).to_be_visible(timeout=100000)
        expect(self.page.locator('tr').filter(has=self.page.locator(f'p[title="{appliance2_name}"]')).locator('p[title="Standard"]')).to_be_visible(timeout=100000)

    def create_raw_volumes(self):
        self.page.get_by_role("button").filter(has_text="Create a new volume").click()
        self.page.get_by_role("radio").nth(1).check()
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("button", name="Next").click()
        self.page.locator(".checkbox-custom").first.click()
        self.page.locator("tr:nth-child(2) > .wizard_table__table_body_checkbox_wrapper > .checkbox-label > .checkbox-custom").click()
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("textbox").nth(0).fill("rvol")
        self.page.get_by_role("textbox").nth(1).fill("2")
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("button", name="Create").click()
        expect(self.page.locator('tr').filter(has=self.page.locator(f'p[title="{appliance1_name}"]')).locator('p[title="Raw"]')).to_be_visible(timeout=100000)
        expect(self.page.locator('tr').filter(has=self.page.locator(f'p[title="{appliance2_name}"]')).locator('p[title="Raw"]')).to_be_visible(timeout=100000)    

    def create_backup_volumes(self):
        self.page.get_by_role("button").filter(has_text="Create a new volume").click()
        self.page.get_by_role("radio").nth(2).check()
        self.page.get_by_role("button", name="Next").click()
        self.page.locator(".checkbox-custom").first.click()
        self.page.locator("tr:nth-child(2) > .wizard_table__table_body_checkbox_wrapper > .checkbox-label > .checkbox-custom").click()
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("textbox").nth(0).fill("bvol")
        self.page.get_by_role("textbox").nth(1).fill("2")
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("button", name="Create").click()
        expect(self.page.locator('tr').filter(has=self.page.locator(f'p[title="{appliance1_name}"]')).locator('p[title="Backup repository"]')).to_be_visible(timeout=100000)
        expect(self.page.locator('tr').filter(has=self.page.locator(f'p[title="{appliance2_name}"]')).locator('p[title="Backup repository"]')).to_be_visible(timeout=100000)  

    def configure_ha_networking(self):
        self.page.get_by_role('link', name='Network').click()
        self.page.get_by_role("button", name="Configure HA networking").click()
        self.page.get_by_role("row", name="Appliance Status Software").locator("span").click()
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("textbox").nth(0).fill(f"14.14.14.{appliance1_name}")
        self.page.get_by_role("textbox").nth(1).fill("24")
        self.page.get_by_role("checkbox").first.check()
        self.page.get_by_role("textbox").nth(2).fill(f"15.15.15.{appliance1_name}")
        self.page.get_by_role("textbox").nth(3).fill("24")
        self.page.get_by_role("checkbox").nth(3).check()
        self.page.get_by_role("textbox").nth(4).fill(f"14.14.14.{appliance2_name}")
        self.page.get_by_role("textbox").nth(5).fill("24")
        self.page.get_by_role("checkbox").nth(4).check()
        self.page.get_by_role("textbox").nth(6).fill(f"15.15.15.{appliance2_name}")
        self.page.get_by_role("textbox").nth(7).fill("24")
        self.page.locator("input[name=\"eth2\"]").nth(3).click()
        self.page.get_by_role("spinbutton").click()
        self.page.get_by_role("spinbutton").fill("9000")
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("button", name="Yes, continue").nth(1).click()
        self.page.get_by_role("button", name="Yes, continue").click()
        self.page.get_by_role("button", name="Configure", exact=True).click()
        expect(self.page.locator('p.wizard_table__table_item_text[title="Up"]')).to_have_count(6, timeout=100000)