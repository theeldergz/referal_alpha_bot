from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def welcome_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Запустить")
    kb.adjust(2)

    return kb.as_markup(resize_keyboard=True)


def welcome_yes_no_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text='Да', callback_data='yes')
    )
    kb.row(types.InlineKeyboardButton(
        text='Нет', callback_data='no')
    )
    kb.adjust(2)

    return kb.as_markup()


def unit_1_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text='Понятно', callback_data='unit_1_accept')
    )
    kb.row(types.InlineKeyboardButton(
        text='Подробнее', callback_data='unit_1_details')
    )
    kb.adjust(2)

    return kb.as_markup()


def unit_1_continue_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text='Продолжить', callback_data='unit_1_continue')
    )
    kb.adjust(1)

    return kb.as_markup()


def unit_2_accept_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text='Понятно', callback_data='unit_2_accept')
    )
    kb.row(types.InlineKeyboardButton(
        text='Подробнее', callback_data='unit_2_details')
    )
    kb.adjust(2)

    return kb.as_markup()