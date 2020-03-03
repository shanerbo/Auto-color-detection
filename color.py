from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Firefox(executable_path="/Users/Unchained_Erbo/Downloads/geckodriver")
browser.get('http://www.cuishuai.cc/game/')

# start game
start = browser.find_element_by_xpath("/html/body/div/div[1]/div[2]/button")
start.click()

# color grid

inGame = True
while inGame:
    go = True
    i = 1
    colors = {}
    while go:
        block = browser.find_elements_by_xpath('/html/body/div/div[2]/div/span[' + str(i) + ']')
        if len(block) > 0:
            attr = block[0].get_attribute('style')
            # if exist
            if attr in colors:
                for key, value in colors.items():
                    if key == attr:
                        continue
                    else:
                        target = browser.find_element_by_xpath('/html/body/div/div[2]/div/span[' + str(value[0]) + ']')
                        target.click()
                        break
                colors[attr].append(i)
            else:
                if len(colors) > 0 and len(colors[list(colors.keys())[0]]) > 1:
                    target = browser.find_element_by_xpath('/html/body/div/div[2]/div/span[' + str(i) + ']')
                    target.click()
                    break
                else:
                    colors[attr] = [i]
            i += 1
        else:
            break

    for key, value in colors.items():
        if len(value) == 1:
            print('bigO n')
            target = browser.find_element_by_xpath('/html/body/div/div[2]/div/span[' + str(value[0]) + ']')
            target.click()
            break
