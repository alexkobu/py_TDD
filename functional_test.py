from selenium import webdriver
from seleniu.webdriver.common.keys import Keys
import time
import unittests

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        # Do header and title mention To-Do list
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # enter new-item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do Item'
        )

        # input "Buy peacock featehers"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )
        
        self.fail('Finish the test!')

        [...rest of comments as before]

if __name__ = '__main__':
    unittests.main(warnings='ignore')
    

#browser = webdriver.Firefox()


#browser.get('http://localhost:8000')

#assert 'Django' in browser.title

#assert 'To-Do' in browser.title, "Browser title was " + browser.title

#browser.quit()

