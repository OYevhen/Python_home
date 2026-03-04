from playwright.sync_api import expect

URL1 = "https://172.16.6.147/"
URL2 = "https://172.16.6.148/"
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

        self.page.get_by_role("textbox").first.fill(f"14.14.14.{appliance1_name}")
        self.page.get_by_role("textbox").nth(1).fill("24")
        self.page.locator("#ens224").nth(0).check()
        self.page.get_by_role("textbox").nth(2).fill(f"15.15.15.{appliance1_name}")
        self.page.get_by_role("textbox").nth(3).fill("24")
        self.page.locator("#ens256").nth(1).check()
        self.page.get_by_role("textbox").nth(4).fill(f"14.14.14.{appliance2_name}")
        self.page.get_by_role("textbox").nth(5).fill("24")
        self.page.locator("#ens224").nth(2).check()
        self.page.locator(f"div:nth-child(7) > .dropdown > .dropdown_content > .wizard_table__container > #wizard_table > .wizard_table__table_tbody_wrapper > tr:nth-child(2) > td:nth-child(5) > .wizard_table__table_item_text_wrapper > .table_input__wrapper > .table_input__container").fill(f"15.15.15.{appliance2_name}")
        self.page.locator(f"div:nth-child(7) > .dropdown > .dropdown_content > .wizard_table__container > #wizard_table > .wizard_table__table_tbody_wrapper > tr:nth-child(2) > td:nth-child(6) > .wizard_table__table_item_text_wrapper > .table_input__wrapper > .table_input__container").fill("24")
        self.page.locator("#ens256").nth(3).check()
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


    def create_2ha_iscsi_ram_lun(self, name="ilun2haram"):
        self.page.get_by_role("button").filter(has_text="Create a new LUN").click(timeout=100000)
        self.page.get_by_role("radio").nth(0).check()
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
        self.page.get_by_role("textbox").nth(0).fill(name)
        self.page.locator("input.MuiInputBase-input").nth(1).fill("1")
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("button", name="Create LUN").click()
        expect(self.page.get_by_role("row", name=name)).to_be_visible(timeout=1000000)

    def create_2ha_nvme_tcp_lun(self, name="nlun2hatcp"):
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
        self.page.get_by_role("textbox").nth(0).fill(name)
        self.page.get_by_text("Data").nth(2).click()
        self.page.get_by_text("Data").nth(3).click()
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("button", name="Create LUN").click()
        expect(self.page.get_by_role("row", name="nlun2hatcp")).to_be_visible(timeout=1000000)

    def delete_iscsi_lun(self, name):
        self.page.get_by_role("row", name=name).click()
        self.page.get_by_role("button").filter(has_text="Delete LUN(s)").click()
        self.page.locator("span").first.click()
        self.page.get_by_role("button", name="Delete").click()
        expect(self.page.get_by_text("There are no LUNs yet")).to_be_visible(timeout=100000)

    def delete_nvme_lun(self, name="nlun2hatcp"):
        lun_row = self.page.locator("tr:visible").filter(has_text=name).first
        expect(lun_row).to_be_visible(timeout=120000)

        delete_lun_button = self.page.get_by_role("button").filter(has_text="Delete LUN").first
        try_again_state = self.page.get_by_text("Try again after another LUN is created", exact=True)
        select_lun_state = self.page.get_by_text("Select a LUN to proceed", exact=True)

        for _ in range(240):
            checkbox = lun_row.locator('input[type="checkbox"]').first
            if checkbox.count() > 0:
                if not checkbox.is_checked():
                    checkbox.click(force=True)
            else:
                lun_row.locator("span").first.click()

            if delete_lun_button.count() > 0 and delete_lun_button.is_enabled():
                break

            if delete_lun_button.count() > 0:
                delete_lun_button.hover()
                if try_again_state.count() > 0:
                    self.page.wait_for_timeout(1000)
                elif select_lun_state.count() > 0:
                    self.page.wait_for_timeout(300)

            self.page.wait_for_timeout(500)

        expect(delete_lun_button).to_be_enabled(timeout=60000)
        delete_lun_button.click()
        self.page.get_by_role("button", name="Delete").click()
        expect(self.page.locator("tr:visible").filter(has_text=name)).to_have_count(0, timeout=100000)