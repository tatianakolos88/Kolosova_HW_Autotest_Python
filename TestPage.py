from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml

class TestSearchLocators():
    dictloc = {}
    with open("Locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        dictloc[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        dictloc[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationHelper(BasePage):
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'Send {word} to element {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f'Element {locator} not found')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f'Exception while operation with {locator}')
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator

        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception(f'Exception with click')
            return False
        logging.debug(f'Clicked {element_name} button')
        return True

    def get_text_from_element(self, locator, description=None):

        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=10)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while get test from {element_name}')
            return None
        logging.debug(f'We find text {text} in field {element_name}')
        text = field.text

        return text

    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.dictloc["LOCATOR_LOGIN_FIELD"], word, description="Login form")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.dictloc["LOCATOR_PASS_FIELD"], word, description="Password form")

    def enter_title(self, word):
        self.enter_text_into_field(TestSearchLocators.dictloc["LOCATOR_TITLE_FIELD"], word, description="title form")

    def enter_description(self, word):
        self.enter_text_into_field(TestSearchLocators.dictloc["LOCATOR_DESCRIPTION_FIELD"], word, description="description form")

    def enter_content(self, word):
        self.enter_text_into_field(TestSearchLocators.dictloc["LOCATOR_CONTENT_FIELD"], word, description="post content form")

    def enter_name(self, word):
        self.enter_text_into_field(TestSearchLocators.dictloc["LOCATOR_CONTACT_NAME_FIELD"], word, description="name form")

    def enter_email(self, word):
        self.enter_text_into_field(TestSearchLocators.dictloc["LOCATOR_CONTACT_EMAIL_FIELD"], word, description="email form")

    def enter_contact_content(self, word):
        self.enter_text_into_field(TestSearchLocators.dictloc["LOCATOR_CONTACT_CONTENT_FIELD"], word,
                                   description="contact content form")

    def click_login_button(self):
        self.click_button(TestSearchLocators.dictloc["LOCATOR_LOGIN_BTN"], description="login")

    def click_to_do_new_post(self):
        self.click_button(TestSearchLocators.dictloc["LOCATOR_NEW_POST_BTN"], description="new post")

    def click_save_post_button(self):
        self.click_button(TestSearchLocators.dictloc["LOCATOR_SAVE_BTN"], description="save post")

    def click_contact_button(self):
        self.click_button(TestSearchLocators.dictloc["LOCATOR_CONTACT_BTN"], description="contact")

    def contact_us_save_button(self):
        self.click_button(TestSearchLocators.dictloc["LOCATOR_CONTACT_SAVE_BTN"], description="contact save")

    def get_title_text(self):
        return self.get_text_from_element(TestSearchLocators.dictloc["LOCATOR_TITLE_TEXT"], description="title")

    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.dictloc["LOCATOR_ERROR_FIELD"], description="error label")

    def get_profile_text(self):
        return self.get_text_from_element(TestSearchLocators.dictloc["LOCATOR_USER_PROFILE_NAME"], description="user profile name")

    def get_alert_text(self):
        logging.info("Get alert text")
        text = self.alert()
        logging.info(text)
        return text