# Автоматизувати процес замовлення робота за допомогою Selenium
# 1. Отримайте та прочитайте дані з "https://robotsparebinindustries.com/orders.csv". Увага!
# Файл має бути прочитаний з сервера кожного разу при запускі скрипта, не зберігайте файл локально.
# 2. Зайдіть на сайт "https://robotsparebinindustries.com/"
# 3. Перейдіть у вкладку "Order your robot"
# 4. Для кожного замовлення з файлу реалізуйте наступне:
#     - закрийте pop-up, якщо він з'явився. Підказка: не кожна кнопка його закриває.
#     - оберіть/заповніть відповідні поля для замовлення
#     - натисніть кнопку Preview та збережіть зображення отриманого робота. Увага! Зберігати треба
#     тільки зображення робота, а не всієї сторінки сайту.
#     - натисніть кнопку Order та збережіть номер чеку. Увага! Інколи сервер тупить і видає помилку,
#     але повторне натискання кнопки частіше всього вирішує проблему. Дослідіть цей кейс.
#     - переіменуйте отримане зображення у формат <номер чеку>_robot (напр. 123456_robot.jpg).
#     Покладіть зображення в директорію output (яка має створюватися/очищатися під час запуску скрипта).
#     - замовте наступного робота (шляхом натискання відповідної кнопки)


import os
import shutil
from csv import DictReader
from io import BytesIO, StringIO

import chromedriver_autoinstaller
import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class OrderRobots:
    '''Class for automated ordering robots from "https://robotsparebinindustries.com"'''

    def __init__(self, output_folder: str = "output") -> None:
        self.output_folder = output_folder
        self.driver = None
        self.URL = "https://robotsparebinindustries.com"

    def setup_driver(self) -> None:
        """Set up chrome driver"""

        # Install crome driver if not installed
        chromedriver_autoinstaller.install()
        # Initialise chrome driver
        self.driver = webdriver.Chrome()
        # Get main site
        self.driver.get(self.URL)

    def close_driver(self) -> None:
        """Close driver"""
        self.driver.quit()

    def order_robots(self) -> None:
        """Order robots from /orders.csv file and save ther pictures in folder"""

        orders_info = self._get_orders_info()
        self._create_or_empty_folder()
        self._open_order_tab()

        # Order each robot from orders
        for order_info in orders_info:
            self._close_alert()
            self._select_robot_configuration(order_info=order_info)
            robot_image = self._get_robot_image()
            self._order_robot()
            receipt = self._get_receipt()
            self._save_robot_image(image=robot_image, receipt=receipt)
            self._click_order_another_robot()

    def _get_orders_info(self) -> DictReader:
        """Get orders info from /orders.csv
        Structure of dict {'order_num':str, 'head':str, 'body':str, 'legs':str, 'address':str}"""

        # Get orders CSV
        response = requests.get(f"{self.URL}/orders.csv")

        # Parse the CSV content from the response
        csv_content = StringIO(response.text)

        # Turn CSV content into a list of dictionaries
        custom_fieldnames = ["order_num", "head", "body", "legs", "address"]
        csv_reader = DictReader(f=csv_content, fieldnames=custom_fieldnames)

        # Skip the header row
        next(csv_reader)
        return csv_reader

    def _create_or_empty_folder(self) -> None:
        """Create or empty folder for storing robots pictures"""

        # If folder exists, remove its contents
        if os.path.exists(self.output_folder):
            shutil.rmtree(self.output_folder)

        # Create folder
        os.makedirs(self.output_folder)

    def _open_order_tab(self) -> None:
        """Open order tab"""

        order_nav_link = self.driver.find_element(By.CSS_SELECTOR, "a[href='#/robot-order']")
        order_nav_link.click()

    def _close_alert(self) -> None:
        """Close alert"""

        ok_btn = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-dark")
        ok_btn.click()

    def _select_robot_configuration(self, order_info: dict) -> None:
        """Select robot configuration for order according to the received info"""

        # Select head
        head_selector = Select(self.driver.find_element(By.NAME, "head"))
        head_selector.select_by_value(order_info["head"])

        # Select body
        needed_body = self.driver.find_element(
            By.CSS_SELECTOR, f"input[type='radio'][value='{order_info['body']}']"
        )
        needed_body.click()

        # Select legs
        legs_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='number']")
        legs_input.send_keys(int(order_info["legs"]))

        # Type address
        address_input = self.driver.find_element(By.NAME, "address")
        address_input.send_keys(order_info["address"])

    def _get_robot_image(self) -> Image:
        """Get robot image from preview button"""

        def _open_robot_preview(self) -> None:
            """Open robot preview"""

            preview_btn = self._driver_wait().until(EC.element_to_be_clickable((By.ID, "preview")))
            self._click_js(preview_btn)

        def _get_robot_parts_img_srcs(self) -> list[str]:
            """Get sources for robot parts images"""

            images = self._driver_wait().until(
                EC.visibility_of_all_elements_located(
                    (By.CSS_SELECTOR, "#robot-preview-image > img")
                )
            )
            return [image.get_attribute("src") for image in images]

        def _open_image_from_src(src: str) -> Image:
            """Open image from received source"""
            response = requests.get(src)
            return Image.open(BytesIO(response.content))

        def _get_combined_image(image_srcs: list[str]) -> Image:
            """Get combined image from robot parts images"""

            # Open images from URLs
            images = [_open_image_from_src(image_src) for image_src in image_srcs]

            # Get width and total height of the images
            width = 354
            total_height = sum(image.size[1] for image in images)

            # Create a new image with the same width and total height
            combined_image = Image.new("RGB", (width, total_height))

            # Paste each image into new image
            current_height = 0
            for image in images:
                # Resize image if needed
                if image.width != width:
                    image = image.resize((width, image.height))
                # Add image to combined image
                combined_image.paste(image, (0, current_height))
                current_height += image.size[1]
            return combined_image

        _open_robot_preview(self)
        robot_parts_img_srcs = _get_robot_parts_img_srcs(self)
        return _get_combined_image(image_srcs=robot_parts_img_srcs)

    def _order_robot(self) -> None:
        """Order robot"""

        # Try to order
        def _try_order() -> bool:
            """Try to order robot. Returns True if success, otherwise False"""

            order_btn = self._driver_wait().until(EC.element_to_be_clickable((By.ID, "order")))
            self._click_js(order_btn)

            # Check if ordered
            success_failure = self._driver_wait().until(
                EC.any_of(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-danger")),
                    EC.visibility_of_element_located((By.CLASS_NAME, "badge-success")),
                )
            )
            return True if success_failure.aria_role == "paragraph" else False

        # Repeat clicking on order button while not ordered
        is_ordered = _try_order()
        while not is_ordered:
            is_ordered = _try_order()

    def _get_receipt(self) -> str:
        """Get receipt for ordered robot"""

        receipt_line_elem = self._driver_wait().until(
            EC.visibility_of_element_located((By.CLASS_NAME, "badge-success"))
        )
        return receipt_line_elem.text.split("-")[-1]

    def _save_robot_image(self, image: Image, receipt: str) -> None:
        """Save robot image to folder"""
        image.save(os.path.join(self.output_folder, f"{receipt}_robot.png"))

    def _click_order_another_robot(self) -> None:
        """Click on order another robot button to open page for ordering next robot"""

        order_btn = self._driver_wait().until(EC.element_to_be_clickable((By.ID, "order-another")))
        self._click_js(order_btn)

    def _driver_wait(self, timeout: int = 10) -> WebDriverWait:
        """Shortcut for WebDriverWait"""
        return WebDriverWait(self.driver, timeout=timeout)

    def _click_js(self, elem: WebElement) -> None:
        """Short cut for clicking using JavaScript"""
        self.driver.execute_script("arguments[0].click();", elem)


if __name__ == "__main__":
    robots = OrderRobots()
    robots.setup_driver()
    robots.order_robots()
    robots.close_driver()
