from playwright.sync_api import Page, expect


def test_wiki(page: Page):
    page.goto('https://www.wikipedia.org/')
    page.get_by_role('link', name = 'English').click()
    expect(page).to_have_title('Wikipedia, the free encyclopedia')
    expect(page.get_by_text('Welcome to Wikipedia, the free encyclopedia that anyone can edit.')).to_be_visible()

def test_wiki2(page: Page):
    page.goto('https://www.wikipedia.org/')
    page.get_by_role('link', name = 'English').click()
