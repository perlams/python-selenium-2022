# Ejercicio 11:
# Utilizando Page Factory poder llamar al browser especifico con llamar a la funcion de get_drver

import time
from lib.factory.factory_driver import get_driver

# Call the Page Factory
driver = get_driver("chRome")
#driver = get_driver("FireFox")

# Open Web Page
url = 'https://qamindslab.com'
driver.get(url)
time.sleep(3)

# Close browser
driver.quit()