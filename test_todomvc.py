from selene import browser, have, be, command, query
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys

"""
fromselenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
"""
"""
# browser.config.click_by_js
# browser.config.type_by_js
# browser.element('#send').with_(click_by_js=True).click() # кликнуть конкретный элемент через JS
# browser.element('#send').perform(command.js.click) # удобнее 1 раз кликнуть так через JS

# send = browser.element('#send').with_(click_by_js=True) # положили в переменную клик по JS чтобы только этот элемент несколько раз кликать всегда через JS.
# send.click()
"""


def test_todomvc():
    browser.config.browser_name = 'firefox'
    browser.config.hold_browser_open = True
    """
    chrome_options = Options()
    chrome_options.headless = True
    browser.config.driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=chrome_options
        )
        browser.open('https://todomvc.com/examples/emberjs/todomvc/dist/')
        browser.element('#doesnotexist').click()
    """

    browser.open('https://todomvc.com/examples/emberjs/todomvc/dist/')
    browser.should(have.title_containing('TodoMVC'))
    """
    browser.execute_script('document.querySelector("#new-todo").remove()') -- позволяет использовать Java-script.
    browser.element('#new-todo').execute_script('element.remove()')
    browser.element('#new-todo').perform(command.js.remove)
    """

    """
    browser.element('#new-todo').type('a').press_enter()

    browser.element('#new-todo').get(query.text)  # подождет ответа и не упадет (текст заберет)  Это более удобно если потребуется
    browser.element('#new-todo').locate().text  # может не успеть отрендериться хтмл страница и тест упадет)
    browser.element('.....').should(have.text('...')) # ЭТО САМЫЙ ВЕРНЫЙ и самый правильный способ теста проверки текста в элементе!!!!!
"""

    """
    text = browser.element('#new-todo').get(query.text) # foo bar kuka riku
    assert 'foo' in text
    assert 'kuka' in text

    browser.element('#new-todo').should(have.text('foo')).should(have.text('kuka'))
    # also we can write AND -- browser.element('#new-todo').should(have.text('foo')).and_(have.text('kuka'))
    # also we can write OR -- browser.element('#new-todo').should(have.text('foo')).or_(have.text('kuka'))
    """

    browser.element('.new-todo').type('a.').press_enter()
    browser.element('.new-todo').type('b.').press_enter()
    browser.element('.new-todo').type('c.').press_enter()
    browser.element('.new-todo').type('d.').press_enter()
    browser.all('.todo-list>li').should(have.exact_texts('a.', 'b.', 'c.', 'd.'))      # чтобы проверить сразу и порядок и текст и кол-во исп. exact_texts(), а чтобы например только кол-во исп. have.size(3) и т.д.
    browser.all('.todo-list>li')[0].should(have.exact_text('a.'))                             # первый элемент по индексу
    browser.all('.todo-list>li')[1:3].should(have.texts('b', 'c'))                # брать значения в диапазоне (причем верхн граница 3 не входит, т.е. перед ней остановится тут.
    browser.all('.todo-list>li').first.should(have.exact_text('a.'))                          # первый (причем есть только первый и сторой ни третьего ни последнего нет тут варианта такого.
    browser.all('.todo-list>li').second.should(have.text('b'))                                # второй
    browser.all('.todo-list>li')[-1].should(have.exact_text('d.'))                            # последний
    browser.all('.todo-list>li').even.should(have.texts('b', 'd'))                # парные (видать четные)
    browser.all('.todo-list>li').odd.should(have.texts('a', 'c'))                 # непарные (видать НЕ четные)

    # находим чекбокс по тексту (by позволяет фильтровать - это тоже что в селекторах [] квадратные скобки, фильтровать можем по тем же conditions что и в should`ах )
    # находит все li с таким текстом (b.)
    browser.all('.todo-list>li').by(have.exact_text('b.')).first.element(
        '.toggle'
    ).click()

    browser.all('.todo-list>li').by(have.css_class('completed')).should(
        have.exact_texts('b.') # exact_text не срабатывает / а вот exact_texts - СРАБОТАЛО!!! в чем прекл (потому что по всем ищет??)
    )

    browser.all('.todo-list>li').by(have.no.css_class('completed')).should(
        have.exact_texts('a.', 'c.', 'd.')
    )

"""
actions = ActionChains(browser.driver)
actions.key_down(keys.CTRL).send_keys('a').keys_up(keys.CTRL).perform()
browser.element('#new-todo').clear().type('b')
"""
