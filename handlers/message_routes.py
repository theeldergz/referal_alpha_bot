from aiogram import types, Router
from aiogram.types import FSInputFile, Message
from aiogram.filters.command import Command

from keyboards.keyboards import welcome_yes_no_kb, unit_1_kb, unit_1_continue_kb, unit_2_accept_kb

from image_files.images_paths import path_welcome_img, path_revenue_img, path_unit_1_my_profile, path_unit_1_accept


router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    welcome_img = FSInputFile(path_welcome_img)
    await message.answer_photo(photo=welcome_img, reply_markup=welcome_yes_no_kb(), caption='''
    Привет, Имя!  Я - Варвара (Виктория, Ирина). 
Если ты нажал кнопку «старт», значит тебе интересен официальный доход без вложений, мне, кстати, тоже – рассказать?
    ''')


@router.callback_query(lambda c: c.data == 'yes')
async def welcome_handler_if_yes(callback_query: types.CallbackQuery):
    revenue_img = FSInputFile(path_revenue_img)

    await callback_query.message.answer(text='Добро пожаловать в проект «Свой в Альфе», '
                                             'посмотри на преимущества участия в нашем проекте!')

    await callback_query.message.answer_photo(photo=revenue_img, reply_markup=unit_1_kb(), caption='''Официальный 
    доход. В рамках проекта «Свой в Альфе» у тебя есть возможность получать официальный доход,что дает тебе 
    уверенность в том, что ты точно получишь заработанные деньги.  Ты становишься официальным партнером банка, 
    платишь налоги и получаешь все преимущества официального дохода.''')

    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'no')
async def welcome_handler_if_no(callback_query: types.CallbackQuery):
    revenue_img = FSInputFile(path_revenue_img)

    await callback_query.message.answer(text='Прости, но я не знаю другого, ведь проект «Свой в Альфе»'
                                             'это проект от крупного российского банка, посмотри на его преимущества:')

    await callback_query.message.answer_photo(photo=revenue_img, reply_markup=unit_1_kb(), caption='''
    Официальный доход. В рамках проекта «Свой в Альфе» у тебя есть возможность получать официальный доход, 
    что дает тебе уверенность в том, что ты точно получишь заработанные деньги. Ты становишься официальным 
    партнером банка, платишь налоги и получаешь все преимущества официального дохода.
    ''')

    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'unit_1_accept' or c.data == 'unit_1_continue')
async def unit_1_accept_handler(callback_query: types.CallbackQuery):
    photo = FSInputFile(path_unit_1_accept)

    await callback_query.message.answer_photo(photo=photo, reply_markup=unit_2_accept_kb(), caption='''Доход без вложений. 
    Проект «Свой в Альфе»  это бизнес-модель, которая дает возможность  любому гражданину РФ  без первоначального 
    капитала начать свой бизнес либо просто создать дополнительный источника дохода без  вложений.
    ''')
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'unit_1_details')
async def unit_1_details_handler(callback_query: types.CallbackQuery):
    photo = FSInputFile(path_unit_1_my_profile)

    await callback_query.message.answer_photo(photo=photo, caption='''Ты можешь 
    самостоятельно выбрать форму сотрудничества: Самозанятый. Простая и быстрая регистрация через приложение банка, 
    низкие ставки по налогам всего 6%  и отсутствие отчетности. Получаешь  возможность официально работать оплачивая 
    небольшой налог в соответствии с законодательством РФ. Самозанятость, к примеру,  не влияет на пенсию. 
    Федеральная налоговая служба не считает самозанятых пенсионеров трудоустроенными гражданами. Так пенсионеры могут 
    уплачивать налог на профессиональный доход и при этом не рискуют потерять право на доплаты и индексацию 
    пенсионных выплат.''')

    await callback_query.message.answer(text='''
     Дает возможность заниматься предпринимательской деятельностью без образования юридического 
    лица. Заплати налоги и спи спокойно. Индивидуальный предприниматель. Если вы уже ИП просто предоставьте справку 
    что вы работаете по УСН и начинайте сотрудничество с банком. Простая регистрация, быстрый и простой вывод денег. 
    Физическое лицо, вам достаточно предоставить паспорт, инн и снилс и ваша форма сотрудничества подтверждена. 
    Обратите внимание по физическому лицу необходимо оплатить налог 13% . Можно совмещать разные виды деятельности. 
    Можно работать с 18 лет. Сотрудничество с проектом «Свой в Альфе» дает возможность студентам пройти практику и 
    получить  свой первый доход. 
    ''', reply_markup=unit_1_continue_kb())

    await callback_query.answer()
