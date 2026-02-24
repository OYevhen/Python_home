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
        self.page.get_by_text("GB").nth(0).click()
        self.page.get_by_text("GB").nth(2).click()
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("button", name="Create").click()
        expect(self.page.locator(f'p[title="{appliance1_name}"]')).to_be_visible(timeout=100000)
        expect(self.page.locator(f'p[title="{appliance2_name}"]')).to_be_visible(timeout=100000)

    def delete_pools(self):
        self.page.get_by_role('link', name='Storage pools').click()
        self.page.locator("#checkbox").click()
        # if self.page.get_by_role("button", name="Delete pool(s)").is_disabled():
        #     self.page.get_by_role('link', name='Volumes').click()
        #     self.delete_volumes()
        #     self.page.get_by_role('link', name='Storage pools').click()
        self.page.get_by_role("button").filter(has_text="Delete pool(s)").click()
        self.page.get_by_role("button", name="Delete").click()
        expect(self.page.get_by_text("There are no storage pools yet")).to_be_visible(timeout=100000)
    
    def create_standard_volumes(self):
        self.page.get_by_role("button").filter(has_text="Create a new volume").click()
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_text("Single Disk").nth(0).click()
        self.page.get_by_text("Single Disk").nth(1).click()
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
        self.page.locator(".checkbox-custom").nth(0).click()
        self.page.locator(".checkbox-custom").nth(1).click()
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
        self.page.locator(".checkbox-custom").nth(0).click()
        self.page.locator(".checkbox-custom").nth(1).click()
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("textbox").nth(0).fill("bvol")
        self.page.get_by_role("textbox").nth(1).fill("2")
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("button", name="Create").click()
        expect(self.page.locator('tr').filter(has=self.page.locator(f'p[title="{appliance1_name}"]')).locator('p[title="Backup repository"]')).to_be_visible(timeout=100000)
        expect(self.page.locator('tr').filter(has=self.page.locator(f'p[title="{appliance2_name}"]')).locator('p[title="Backup repository"]')).to_be_visible(timeout=100000)  

    def delete_volumes(self):
        self.page.locator("#checkbox").click()
        # if self.page.get_by_role("button", name="Delete volume(s)").is_disabled():
        #     self.page.get_by_role('link', name='LUNs').click()
        #     self.delete_luns()
        #     self.page.get_by_role('link', name='Volumes').click() 
        self.page.get_by_role("button").filter(has_text="Delete volume(s)").click()
        self.page.get_by_role("button", name="Delete").click()
        expect(self.page.get_by_text("There are no volumes yet")).to_be_visible(timeout=100000) 

    def configure_ha_networking(self):
        self.page.get_by_role('link', name='Network').click()
        self.page.get_by_role("button", name="Configure HA networking").click()
        self.page.get_by_role("row", name="Appliance Status Software").locator("span").click()
        self.page.get_by_role("button", name="Next").click()

        self.page.get_by_role("textbox").first.fill(f"20.20.180.{appliance1_name}")
        self.page.get_by_role("textbox").nth(1).fill("24")
        self.page.get_by_role("checkbox").first.click()
        self.page.get_by_role("textbox").nth(2).fill(f"10.10.180.{appliance1_name}")
        self.page.get_by_role("textbox").nth(3).fill("24")
        self.page.get_by_role("checkbox").nth(3).click()
        self.page.get_by_role("textbox").nth(4).fill(f"20.20.180.{appliance2_name}")
        self.page.get_by_role("textbox").nth(5).fill("24")
        self.page.get_by_role("checkbox").nth(4).click()
        self.page.locator(f"div:nth-child(7) > .dropdown > .dropdown_content > .wizard_table__container > #wizard_table > .wizard_table__table_tbody_wrapper > tr:nth-child(2) > td:nth-child(5) > .wizard_table__table_item_text_wrapper > .table_input__wrapper > .table_input__container").fill(f"10.10.180.{appliance2_name}")
        self.page.locator(f"div:nth-child(7) > .dropdown > .dropdown_content > .wizard_table__container > #wizard_table > .wizard_table__table_tbody_wrapper > tr:nth-child(2) > td:nth-child(6) > .wizard_table__table_item_text_wrapper > .table_input__wrapper > .table_input__container").fill("24")
        self.page.locator("input[name=\"eth2\"]").nth(3).click()
        self.page.get_by_role("spinbutton").fill("9000")

        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("button", name="Yes, continue").nth(1).click(timeout=1000000)
        self.page.get_by_role("button", name="Yes, continue").click()
        self.page.get_by_role("button", name="Configure", exact=True).click()
        expect(self.page.locator('p.wizard_table__table_item_text[title="Up "]')).to_have_count(6, timeout=100000)

    def configure_ha_networking_repeat(self):
        self.page.get_by_role('link', name='Network').click()
        self.page.get_by_role("button", name="Configure HA networking").click()
        self.page.get_by_role("row", name="Appliance Status Software").locator("span").click()
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("spinbutton").fill("9000")
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("button", name="Yes, continue").nth(1).click(timeout=100000)
        self.page.get_by_role("button", name="Yes, continue").click()
        self.page.get_by_role("button", name="Configure", exact=True).click()
        # expect(page.locator('p.wizard_table__table_item_text[title="Up"]')).to_have_count(6, timeout=1000000) #too slow
        expect(self.page.locator('p.wizard_table__table_item_text[title="9000"]')).to_have_count(4, timeout=1000000)

    def create_2ha_nvme_tcp(self, name="nlun2hatcp"):
        self.page.get_by_role("button").filter(has_text="Create a new LUN").click(timeout=100000)
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_text(f"{appliance1_name}", exact=True).click()
        self.page.get_by_text(f"{appliance2_name}", exact=True).click()
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("button", name="Yes, continue").nth(1).click()
        self.page.get_by_role("button", name="Yes, continue").click()
        self.page.get_by_role("textbox").nth(0).fill("nlun2hatcp")
        self.page.get_by_text("Data").nth(2).click()
        self.page.get_by_text("Data").nth(3).click()
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("button", name="Create LUN").click()
        expect(self.page.get_by_role("row", name="nlun2hatcp")).to_be_visible(timeout=1000000)

    def select_lun_until_delete_enabled(self, name, max_attempts=240, wait_ms=500):
        lun_row_creating = self.page.locator("tr:visible") \
            .filter(has=self.page.locator(f'p[title="{name}"]')) \
            .filter(has=self.page.locator('p.wizard_table__table_item_text[title="Creating"]'))
        expect(lun_row_creating).to_have_count(0, timeout=120000)

        lun_row_online = self.page.locator("tr:visible") \
            .filter(has=self.page.locator(f'p[title="{name}"]')) \
            .filter(has=self.page.locator('p.wizard_table__table_item_text[title="Online"]')) \
            .first
        expect(lun_row_online).to_be_visible(timeout=120000)

        lun_row = lun_row_online
        delete_button_locators = [
            self.page.get_by_role("button", name="Delete LUN(s)"),
            self.page.get_by_role("button", name="Delete LUN"),
            self.page.get_by_role("button").filter(has_text="Delete LUN"),
            self.page.get_by_role("button").filter(has_text="Delete"),
        ]

        for _ in range(max_attempts):
            if lun_row_creating.count() > 0:
                self.page.wait_for_timeout(wait_ms)
                continue

            if lun_row.count() == 0:
                self.page.wait_for_timeout(wait_ms)
                continue

            if lun_row.locator('input[type="checkbox"]').count() > 0:
                lun_row.locator('input[type="checkbox"]').first.click(force=True)
            else:
                lun_row.locator("span").first.click()

            for locator in delete_button_locators:
                candidate = locator.first
                if candidate.count() > 0 and candidate.is_enabled():
                    return candidate

            self.page.wait_for_timeout(wait_ms)

        fallback_delete = self.page.get_by_role("button").filter(has_text="Delete").first
        expect(fallback_delete).to_be_enabled(timeout=60000)
        return fallback_delete

    def delete_iscsi_lun(self, name):
        self.page.get_by_role("row", name=name).click()
        self.page.get_by_role("button").filter(has_text="Delete LUN(s)").click()
        self.page.locator("span").first.click()
        self.page.get_by_role("button", name="Delete").click()
        expect(self.page.get_by_text("There are no LUNs yet")).to_be_visible(timeout=100000)

    def delete_nvme_lun(self, name="nlun2hatcp"):
        delete_lun_button = self.select_lun_until_delete_enabled(name)
        delete_lun_button.click()
        self.page.get_by_role("button", name="Delete").click()
        expect(self.page.locator("tr:visible").filter(has_text=name)).to_have_count(0, timeout=100000)