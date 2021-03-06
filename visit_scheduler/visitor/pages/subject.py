from selenium.common.exceptions import NoSuchElementException

from .basepage import BasePage
from ..locators import SubjectLocators
from lesson_schedule.schemes import Subject


class SubjectPage(BasePage):

    def open_meeting(self, subject: Subject):
        """
        Open MEET for subject.
        """
        if not subject.meet_url_name:
            self.logger.warning(f"Failed open meet for subject. Subject {subject.name!r} doesn't have 'meet_url_name'")
            return

        resources = self.browser.find_elements(*SubjectLocators.RESOURCES)
        for r in resources:
            try:
                resource_name_el = r.find_element(*SubjectLocators.RESOURCE_NAME)
            except NoSuchElementException:
                continue

            resource_name: str = resource_name_el.text
            if resource_name.lower().strip('. ') == subject.meet_url_name.lower().strip('. '):
                self.logger.debug(f'Found meet url for subject: {subject.name}')
                resource_name_el.click()
                break
        else:
            self.logger.warning(f'Not found meet url for subject: {subject.name}')
