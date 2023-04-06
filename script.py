import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Настройка пути до хром драйвера внутри ''
s = Service('')
driver = webdriver.Chrome(service=s)


def reboot(ip: str, login: str, password: str) -> None:
    """
    Функция, используя веб драйвер, находит кнопку Reboot на странице и кликает по ней.
    """
    try:
        driver.get(f"http://{login}:{password}@{ip}/default/en_US/tools.html")
        time.sleep(1)
        button = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr[7]/td[2]/table/tbody/tr[9]/td/div/input")
        button.click()
        driver.switch_to.alert.accept()
        time.sleep(1)
        print(f'{ip} Готов.')
    except Exception as e:
        print(f'Что то пошло не так на сим банке {ip}, {e}.')


if __name__ == "__main__":
    reboot('test', 'test', 'test')
    # пример НЕ рабочий
