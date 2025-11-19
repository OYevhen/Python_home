from Seniortester.pages.like_a_button import LikeAButton

def test_button2_exist(browser):
    like_a_button = LikeAButton(browser)
    like_a_button.open()
    assert like_a_button.button_is_displayed

def test_button2_clicked(browser):
    like_a_button = LikeAButton(browser)
    like_a_button.open()
    like_a_button.button.click()
    assert like_a_button.result_text == "Submitted"