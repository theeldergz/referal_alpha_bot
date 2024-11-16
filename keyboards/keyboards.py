from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def welcome_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Запустить")
    kb.adjust(2)

    return kb.as_markup(resize_keyboard=True)


def welcome_yes_no_kb() -> InlineKeyboardMarkup:
    """
    Клавиатура отвечает за первый приветственный блок
    """
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text='Да', callback_data='yes')
    )
    kb.row(types.InlineKeyboardButton(
        text='Нет', callback_data='no')
    )
    kb.adjust(2)

    return kb.as_markup()


def make_accept_details_kb(next_advantage_name: str,
                           current_advantage_details_name: str = None,
                           first_key_text: str = 'Понятно',
                           second_key_text: str = 'Подробнее') -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text=first_key_text, callback_data=f'advantage_{next_advantage_name}_accept')
    )
    kb.row(types.InlineKeyboardButton(
        text=second_key_text, callback_data=f'advantage_{current_advantage_details_name}_details')
    )
    kb.adjust(2)

    return kb.as_markup()


def make_continue_kb(next_advantage_name: str) -> InlineKeyboardMarkup:
    """
    Клавиатура отвечает за переход к следующему "преимуществу"
    """
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text='Продолжить', callback_data=f'advantage_{next_advantage_name}_continue')
    )
    kb.adjust(1)

    return kb.as_markup()


def make_hook_10k_want_later_kb() -> InlineKeyboardMarkup:
    """
    Клавиатура отвечает за кнопки "хочу" и "позже" в модуле о быстром заработке 10к
    """
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text='Хочу', callback_data=f'hook_10k_want')
    )
    kb.row(types.InlineKeyboardButton(
        text='Позже', callback_data=f'card_order')
    )
    kb.adjust(2)

    return kb.as_markup()


def make_become_partner_kb() -> InlineKeyboardMarkup:
    """
    Клавиатура отвечает за кнопку "Хочу стать партнером"
    """
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text='Стать партнером!', callback_data=f'become_partner')
    )
    return kb.as_markup()


def make_card_order_kb() -> InlineKeyboardMarkup:
    """
    Клавиатура отвечает за кнопки в блоке заказа карты
    """
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text='Как получить 500 р. за карту?', callback_data=f'i_order_card')
    )
    kb.row(types.InlineKeyboardButton(
        text='Стать партнером и получить 50.000 р.', callback_data=f'become_partner')
    )

    return kb.as_markup()


def make_register_kb() -> InlineKeyboardMarkup:
    """
    Клавиатура отвечает за кнопку подтверждения регистрации
    """
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text='Я зарегистрировался', callback_data=f'how_to_make_50k')
    )

    return kb.as_markup()


def make_common_kb(next_handler_name: str,
                   current_handler_details_name: str,
                   first_key_text: str = 'Понятно',
                   second_key_text: str = 'Подробнее') -> InlineKeyboardMarkup:
    """
    Клавиатура отвечает за общие кнопки для коллбеков
    """
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text=first_key_text, callback_data=f'{next_handler_name}')
    )
    kb.row(types.InlineKeyboardButton(
        text=second_key_text, callback_data=f'{current_handler_details_name}')
    )

    return kb.as_markup()


def make_common_continue_kb(next_handler_name: str, key_text: str) -> InlineKeyboardMarkup:
    """
    Клавиатура отвечает за кнопки "продолжить" общего формата
    """
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text=f'{key_text}', callback_data=f'{next_handler_name}')
    )

    return kb.as_markup()


def make_info_after_test_kb() -> InlineKeyboardMarkup:
    """
    Клавиатура отвечает за кнопку подтверждения регистрации
    """
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text='Написать наставнику', callback_data=f'mentor_details')
    )
    kb.row(types.InlineKeyboardButton(
        text='Подробнее', callback_data=f'info_after_test_details')
    )

    return kb.as_markup()


def make_check_partner_or_no_kb() -> InlineKeyboardMarkup:
    """
    Клавиатура отвечает за кнопки "да" и "нет" в блоке с вопросом о том является ли пользователь партнером банка
    """
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text='ДА', callback_data=f'check_partner_yes')
    )
    kb.row(types.InlineKeyboardButton(
        text='НЕТ', callback_data=f'check_partner_no')
    )
    kb.adjust(2)

    return kb.as_markup()


def make_partner_url_kb() -> InlineKeyboardMarkup:
    """
    Клавиатура отвечает за кнопку "Я оформил карту"
    """
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text='Я оформил карту', callback_data=f'get_url')
    )

    return kb.as_markup()


def make_call_mentor_kb() -> InlineKeyboardMarkup:
    """
    Клавиатура отвечает за кнопку вызова наставника
    """
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text='Написать наставнику', callback_data=f'call_mentor')
    )

    return kb.as_markup()


def make_study_in_personal_acc_triple_kb() -> InlineKeyboardMarkup:
    """
    Клавиатура отвечает за три кнопки в блоке об обучении в ЛК
    """
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text='Карта куда будет приходить твой доход', callback_data=f'debit_card_order_info')
    )
    kb.row(types.InlineKeyboardButton(
        text='Написать наставнику', callback_data=f'mentor_details')
    )
    kb.row(types.InlineKeyboardButton(
        text='Ответы на тест', callback_data=f'answers_test')
    )

    return kb.as_markup()


def make_i_order_card_kb() -> InlineKeyboardMarkup:
    """
    Клавиатура отвечает за кнопку "Я заказал"
    """
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text='Я заказал', callback_data=f'mentor_details')
    )

    return kb.as_markup()