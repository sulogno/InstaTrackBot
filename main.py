from selenium import webdriver
from time import sleep
from getpass import getpass
from selenium.webdriver.common.by import By

class Instabot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.option = webdriver.ChromeOptions()
        self.option.add_argument('--lang=en-US')
        self.option.add_argument('--window-size=1200,1000')
        self.browser = webdriver.Chrome(options=self.option)
        self.browser.get("http://instagram.com")
        sleep(3)

        # Log in to Instagram
        self.browser.find_element(By.NAME, "username").send_keys(self.username)
        self.browser.find_element(By.NAME, "password").send_keys(self.password)
        self.browser.find_element(By.XPATH, "//button[@type='submit']").click()
        sleep(5)

        # Go to the user's profile page
        self.browser.find_element(By.XPATH, "//a[contains(@href, '/{}')]".format(self.username)).click()
        sleep(5)

        # Get total followers and following counts
        self.total_followers = self.get_total_count('followers')
        self.total_following = self.get_total_count('following')
        print(f"Total Followers: {self.total_followers}, Total Following: {self.total_following}")

    def get_total_count(self, category):
        """
        Get total number of followers or following.
        :param category: 'followers' or 'following'
        :return: Total number of followers or following as an integer
        """
        try:
            if category == 'followers':
                element = self.browser.find_element(By.XPATH, "//a[contains(@href, '/followers')]/span/span")
            else:
                element = self.browser.find_element(By.XPATH, "//a[contains(@href, '/following')]/span/span")
            
            count_text = element.text
            print(f"{category.capitalize()} Count Text: {count_text}")

            return int(count_text.replace(",", "")) if count_text else 0
        except Exception as e:
            print(f"Error fetching {category} count: {e}")
            return 0




    def scroll_and_fetch(self, scroll_box, max_count):
        """
        Scroll and fetch user names up to the max_count limit.
        :param scroll_box: WebElement representing the scrollable box
        :param max_count: Maximum number of items to fetch
        :return: List of user names
        """
        last_ht, ht = 0, 1
        user_names = []

        while len(user_names) < max_count and last_ht != ht:
            last_ht = ht
            sleep(2)
            ht = self.browser.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
            """, scroll_box)
            sleep(5)

            # Get all anchor tags in the scroll box
            links = scroll_box.find_elements(By.TAG_NAME, 'a')
            user_names = [name.text for name in links if name.text != '' and name.text not in user_names]

        # Limit the list to max_count
        return user_names[:max_count]

    def get_following_list(self):
        # Click on the 'following' link
        self.browser.find_element(By.XPATH, "//a[contains(@href, '/following')]").click()
        sleep(10)

        # Locate the scroll box
        scroll_box = self.browser.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]")
        sleep(5)

        # Fetch following up to the total following count
        following_list = self.scroll_and_fetch(scroll_box, self.total_following)
        print(f"Following List: {following_list}")
        return following_list

    def get_follower_list(self):
        # Click on the 'followers' link
        self.browser.find_element(By.XPATH, "//a[contains(@href, '/followers')]").click()
        sleep(10)

        # Locate the scroll box
        scroll_box = self.browser.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
        sleep(5)

        # Fetch followers up to the total followers count
        follower_list = self.scroll_and_fetch(scroll_box, self.total_followers)
        print(f"Follower List: {follower_list}")
        return follower_list

    def following_back(self):
        followers = self.get_follower_list()  # Fetch followers
        self.close_button()  # Close the dialog after fetching followers
        following = self.get_following_list()  # Fetch following

        # Find users who follow you back
        following_back = [user for user in following if user in followers]
        print(f"Following back: {following_back}")

    def close_button(self):
        # Locate the "Close" button by its XPath
        close_button = self.browser.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button")
        # Click the "Close" button
        close_button.click()
        sleep(5)

username = input("Enter your username: ")
password = getpass("Enter your password: ")

# Create an instance of Instabot
bot = Instabot(username, password)

# Execute functions
bot.following_back()  # Check who is following you back
