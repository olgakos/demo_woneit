from selene.support.shared.jquery_style import s

from tests.data.form_data import name, company, status, phone, email, mess

def fill_contact_form():
    s('[name="NAME"]').type(name).press_enter()
    #s('[name="SURNAME"]').type(surname).press_enter() #from ver 2022
    s('[name="COMPANY"]').type(company).press_enter()
    s('[name="STATUS"]').type(status).press_enter()
    s('[name="PHONE"]').type(phone).press_enter()
    s('[name="EMAIL"]').type(email).press_enter()
    s('[name="MESSAGE"]').type(mess).press_enter()


checkbox_politics = s("[for='feedback-agree']")


send_button = s(".feedback-form__bottom")
