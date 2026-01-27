from playwright.sync_api import expect


URL1 = "https://172.16.6.144/"
URL2 = "https://172.16.6.145/"
username = "user"
password = "rds123RDS!@#"

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
        self.page.get_by_role("textbox").nth(0).fill(f"{URL2.split('://')[1].rstrip('/')}")
        self.page.get_by_role("textbox").nth(1).fill(username)
        self.page.locator("input[type='password']").fill(password)
        self.page.get_by_role("button", name="Next").click()
        expect(self.page.get_by_role("heading", name="Summary")).to_be_visible(timeout=100000)   
        self.page.get_by_role("button", name="Add appliance").first.click()
        expect(self.page.locator('p[title="145"]')).to_be_visible(timeout=100000)

    def remove_appliance(self):
        self.page.get_by_role('link', name='Appliances').click()
        self.page.locator('p[title="145"]').click()
        self.page.get_by_role("button").filter(has_text="Remove appliance").click()
        self.page.get_by_role("button", name="Remove").click()
        expect(self.page.locator('p[title="145"]')).to_have_count(0, timeout=100000)

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
        expect(self.page.locator('p[title="144"]')).to_be_visible(timeout=100000)
        expect(self.page.locator('p[title="145"]')).to_be_visible(timeout=100000)

    def delete_single_disk_pools(self):
        self.page.get_by_role('link', name='Storage pools').click()
        self.page.locator('p[title="144"]').click()
        self.page.locator('p[title="145"]').click()
        self.page.get_by_role("button").filter(has_text="Delete pool(s)").click()
        self.page.get_by_role("button", name="Delete").click()
        expect(self.page.locator('p[title="144"]')).to_be_visible(timeout=100000)
        expect(self.page.locator('p[title="145"]')).to_be_visible(timeout=100000)
    
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
        
        expect(self.page.locator('tr').filter(has=self.page.locator('p[title="144"]')).locator('p[title="Standard"]')).to_be_visible(timeout=100000)
        expect(self.page.locator('tr').filter(has=self.page.locator('p[title="145"]')).locator('p[title="Standard"]')).to_be_visible(timeout=100000)