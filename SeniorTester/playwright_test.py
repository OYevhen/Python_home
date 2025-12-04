import re
from playwright.sync_api import Page, Route, expect, Dialog, BrowserContext


def test_wiki(page: Page):
    page.goto("https://www.wikipedia.org/")
    page.get_by_role('link', name='Русский').click()
    expect(page.get_by_text('Добро пожаловать в Википедию,')).to_be_visible()

def test_wiki2(page: Page):
    page.goto("https://www.wikipedia.org/")
    page.get_by_role('link', name='Русский').click()
    page.get_by_role('link', name='Содержание').click()
    page.locator('#ca-talk').click()
    expect(page.locator("#firstHeading")).to_have_text('Обсуждение Википедии:Содержание')

def test_request(page: Page):

    def change_request(route: Route):
        data = route.request.post_data
        if data:
            data = data.replace('User412', 'adsada')
        route.continue_(post_data=data)


    page.route(re.compile('profile/authenticate'), change_request)
    page.goto("http://gymlog.ru/profile/login/")
    page.locator('#email').fill('user412')
    page.locator('#password').fill('k9L-hL')
    page.get_by_role('button', name='Войти').click()
    page.pause()

def test_response(page: Page):

    def change_response(route: Route):
        response = route.fetch()
        data = response.text()
        data = data.replace('User412', 'Zhenya')
        route.fulfill(response=response, body=data)

    page.route(re.compile('profile/412'), change_response)
    page.goto("http://gymlog.ru/profile/login/")
    page.locator('#email').fill('user412')
    page.locator('#password').fill('k9L-hL')
    page.get_by_role('button', name='Войти').click()
    page.pause()

def test_alert(page: Page):
    page.goto('https://demoblaze.com/')

    def accept_alert(alert: Dialog):
        print(alert.message)
        alert.accept()

    page.on("dialog", accept_alert)
    page.get_by_role('link', name='Samsung galaxy s6').click()
    page.get_by_role('link', name='Add to cart').click()
    # page.get_by_role('link', name='Cart').click()
    page.wait_for_event('dialog')
    page.locator('#cartur').click()

def test_tabs(page: Page, context: BrowserContext):
    page.goto('https://nomads.com/')
    with context.expect_page() as new_tab_event:
        page.get_by_text('Get insured').click()
        new_tab = new_tab_event.value
    new_tab.get_by_role('link', name='Sign me up').click()

def test_iframe(page: Page):
    page.goto('https://www.qa-practice.com/elements/iframe/iframe_page')
    page.frame_locator('iframe').locator('.navbar-toggler-icon').click()

def test_select(page: Page):
    page.goto('https://hard.rozetka.com.ua/ua/monitors/c80089/21368=102240/')
    page.locator('#sort').select_option('cheap')
