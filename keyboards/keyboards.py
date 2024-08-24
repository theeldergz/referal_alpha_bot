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


def make_accept_details_kb(advantage_name: str) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text='Понятно', callback_data=f'advantage_{advantage_name}_accept')
    )
    kb.row(types.InlineKeyboardButton(
        text='Подробнее', callback_data=f'advantage_{advantage_name}_details')
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
        text='Позже', callback_data=f'hook_10k_later')
    )
    kb.adjust(2)

    return kb.as_markup()

























def advantage_1_kb() -> InlineKeyboardMarkup:
    """
    Клавиатура отвечает за первое преимущество - "официальный доход"
    """
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text='Понятно', callback_data='advantage_1_accept')
    )
    kb.row(types.InlineKeyboardButton(
        text='Подробнее', callback_data='advantage_1_details')
    )
    kb.adjust(2)

    return kb.as_markup()


def advantage_1_continue_kb() -> InlineKeyboardMarkup:
    """
    Клавиатура отвечает за переход к следующему "преимуществу"
    """
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text='Продолжить', callback_data='advantage_1_continue')
    )
    kb.adjust(1)

    return kb.as_markup()


def advantage_2_kb() -> InlineKeyboardMarkup:
    """
    Клавиатура отвечает за второе преимущество - "Доход без вложений"
    """
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text='Понятно', callback_data='advantage_2_accept')
    )
    kb.row(types.InlineKeyboardButton(
        text='Подробнее', callback_data='advantage_2_details')
    )
    kb.adjust(2)

    return kb.as_markup()


def advantage_2_continue_kb() -> InlineKeyboardMarkup:
    """
    Клавиатура отвечает за переход к следующему "преимуществу"
    """
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text='Продолжить', callback_data='advantage_2_continue')
    )
    kb.adjust(1)

    return kb.as_markup()


def advantage_3_kb() -> InlineKeyboardMarkup:
    """
    Клавиатура отвечает за третье преимущество - "Сотрудничество с крупным российским банком"
    """
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text='Понятно', callback_data='advantage_3_accept')
    )
    kb.row(types.InlineKeyboardButton(
        text='Подробнее', callback_data='advantage_3_details')
    )
    kb.adjust(2)

    return kb.as_markup()


def advantage_3_continue_kb() -> InlineKeyboardMarkup:
    """
    Клавиатура отвечает за переход к следующему "преимуществу"
    """
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text='Продолжить', callback_data='advantage_3_continue')
    )
    kb.adjust(1)

    return kb.as_markup()


def advantage_4_kb() -> InlineKeyboardMarkup:
    """
    Клавиатура отвечает за четвертое преимущество - "Свободный график"
    """
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text='Понятно', callback_data='advantage_4_accept')
    )
    kb.row(types.InlineKeyboardButton(
        text='Подробнее', callback_data='advantage_4_details')
    )
    kb.adjust(2)

    return kb.as_markup()


def advantage_4_continue_kb() -> InlineKeyboardMarkup:
    """
    Клавиатура отвечает за переход к следующему "преимуществу"
    """
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text='Продолжить', callback_data='advantage_4_continue')
    )
    kb.adjust(1)

    return kb.as_markup()


def advantage_5_kb() -> InlineKeyboardMarkup:
    """
    Клавиатура отвечает за пятое преимущество - "Удаленная работа"
    """
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text='Понятно', callback_data='advantage_5_accept')
    )
    kb.row(types.InlineKeyboardButton(
        text='Подробнее', callback_data='advantage_5_details')
    )
    kb.adjust(2)

    return kb.as_markup()


def advantage_5_continue_kb() -> InlineKeyboardMarkup:
    """
    Клавиатура отвечает за переход к следующему "преимуществу"
    """
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text='Продолжить', callback_data='advantage_5_continue')
    )
    kb.adjust(1)

    return kb.as_markup()
