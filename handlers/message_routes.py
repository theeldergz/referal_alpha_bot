import os
import textwrap as tw

from aiogram import types, Router
from aiogram.types import FSInputFile, Message, InputMediaPhoto
from aiogram.filters.command import Command
from dotenv import load_dotenv, find_dotenv

from keyboards.keyboards import welcome_yes_no_kb, make_accept_details_kb, make_continue_kb, \
    make_hook_10k_want_later_kb, make_become_partner_kb, make_card_order_kb, make_register_kb, make_common_kb, \
    make_common_continue_kb, make_check_partner_or_no_kb, \
    make_partner_url_kb, make_call_mentor_kb, make_study_in_personal_acc_triple_kb, make_i_order_card_kb, \
    make_info_after_test_kb

from image_files.images_paths import path_to_welcome_img, path_to_welcome_personal_photo, \
    path_to_advantage_official_income, \
    path_to_advantage_official_income_details, \
    path_to_advantage_income_without_investment, path_to_advantage_cooperation_bank, \
    path_to_advantage_income_without_investment_details, path_to_advantage_cooperation_bank_details, \
    path_to_advantage_unlimited_income, path_to_advantage_unlimited_income_details_apr, \
    path_to_advantage_unlimited_income_details_jan, path_to_advantage_unlimited_income_details_feb, \
    path_to_advantage_unlimited_income_details_march, path_to_advantage_unlimited_income_details_may, \
    path_to_advantage_free_schedule, path_to_advantage_free_schedule_details, path_to_advantage_remote_work, \
    path_to_advantage_remote_work_details, path_to_advantage_free_study_details, path_to_advantage_free_study, \
    path_to_advantage_privilege_details, path_to_advantage_privilege, path_to_advantage_new_profession, \
    path_to_advantage_new_profession_details, path_to_how_to_make_10k_details, path_to_how_to_make_10k, \
    path_to_card_order, path_to_card_order_cashback, path_to_card_order_employee, path_to_become_a_partner, \
    path_to_registration, path_to_answers_test, path_to_ai_gen_man_1, path_to_ai_gen_man_2, \
    path_to_own_at_alpha, path_to_advantage_unlimited_income_details_common, path_to_advantage_privilege_details_2, \
    path_to_check_partner, path_to_how_to_make_50k, path_to_filler_1, path_to_filler_2, path_to_cashback_and_sales_1, \
    path_to_cashback_and_sales_2, path_to_cashback_and_sales_3, path_to_cashback_and_sales_4

router = Router()
load_dotenv(find_dotenv())
USER = os.environ.get('USER')
CARD_ORDER_LINK_FOR_OUR = os.environ.get('CARD_ORDER_LINK_FOR_OUR')
CARD_ORDER_LINK_WITH_CASHBACK = os.environ.get('CARD_ORDER_LINK_WITH_CASHBACK')
PARTNER_LINK = os.environ.get('PARTNER_LINK')


@router.message(Command("start"))
async def cmd_start(message: Message) -> None:
    """
    Функция выводит приветственной сообщение
    """
    photo = FSInputFile(path_to_welcome_img)
    photo_group = [path_to_welcome_img, path_to_welcome_personal_photo]
    media_group = [InputMediaPhoto(media=types.FSInputFile(path)) for path in photo_group]
    username = message.from_user.first_name
    await message.answer_media_group(media=media_group)
    await message.answer(reply_markup=welcome_yes_no_kb(), text=f'''
Привет, {username} 👋
\nЯ - {USER} 😁
\nЕсли ты нажал кнопку «старт», значит тебе интересен официальный доход без вложений, мне, кстати, тоже – рассказать?🔊
    ''')


@router.callback_query(lambda c: c.data == 'yes')
async def welcome_official_income_handler_if__yes(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит за начало диалога по проекту Альфа, если клиент ответил ДА в приветствии.
    Создает пост с преимуществом "Официальный доход"
    """
    photo = FSInputFile(path_to_advantage_official_income)
    next_advantage_kb = make_accept_details_kb(next_advantage_name='income_without_investment',
                                               current_advantage_details_name='official_income')

    await callback_query.message.answer_photo(photo=photo, parse_mode='HTML', caption=tw.dedent('''
<b>Добро пожаловать в проект «Свой в Альфе»</b> 👍
    '''))

    await callback_query.message.answer(reply_markup=next_advantage_kb, text=tw.dedent('''
Официальный доход ✨ \
В рамках проекта «Свой в Альфе» у тебя есть возможность получать официальный доход, что дает тебе уверенность в \
том, что ты точно получишь заработанные деньги. Ты становишься официальным партнером банка, платишь налоги и \
получаешь все преимущества официального дохода. \
    '''))

    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'no')
async def welcome_official_income_handler_if_no(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит за начало диалога по проекту Альфа, если клиент ответил НЕТ в приветствии.
    Создает пост с преимуществом "Официальный доход"
    """
    photo = FSInputFile(path_to_advantage_official_income)
    next_advantage_kb = make_accept_details_kb(next_advantage_name='income_without_investment',
                                               current_advantage_details_name='official_income')

    await callback_query.message.answer_photo(photo=photo, parse_mode='HTML', caption=tw.dedent('''
<b>Прости, но я не знаю другого</b> 😍 
ведь проект «Свой в Альфе» это проект от крупного российского банка
    '''))

    await callback_query.message.answer(reply_markup=next_advantage_kb, text=tw.dedent('''
Официальный доход ✨ \
В рамках проекта «Свой в Альфе» у тебя есть возможность получать официальный доход, что дает тебе уверенность в \
том, что ты точно получишь заработанные деньги. Ты становишься официальным партнером банка, платишь налоги и \
получаешь все преимущества официального дохода. \
    '''))

    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'advantage_official_income_details')
async def advantage_official_income_details_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальным описанием преимущества - "Официальный доход"
    """
    photo = FSInputFile(path_to_advantage_official_income_details)
    continue_kb = make_continue_kb(next_advantage_name='income_without_investment')

    await callback_query.message.answer_photo(parse_mode='HTML', photo=photo, caption=tw.dedent('''
Ты можешь самостоятельно выбрать форму сотрудничества:
\n<b>Самозанятый</b> ⭐
\n• Простая и быстрая регистрация через приложение банка, низкие ставки по налогам всего 6% и отсутствие отчетности. 
\n• Получаешь возможность официально работать оплачивая небольшой налог в соответствии с законодательством РФ.
\n• Самозанятость, к примеру, не влияет на пенсию. Федеральная налоговая служба не считает самозанятых пенсионеров \
трудоустроенными гражданами. Так пенсионеры могут уплачивать налог на профессиональный доход и при этом не рискуют \
потерять право на доплаты и индексацию пенсионных выплат. 
\n• Дает возможность заниматься предпринимательской деятельностью без образования юридического лица. 
\nЗаплати налоги и спи спокойно.
    '''))

    await callback_query.message.answer(parse_mode='HTML', text=tw.dedent('''
<b>Индивидуальный предприниматель</b> ⭐
\n\n• Если вы уже ИП просто предоставьте справку что вы работаете по УСН и начинайте сотрудничество с банком. \
Простая регистрация, быстрый и простой вывод денег. 
    '''))

    await callback_query.message.answer(parse_mode='HTML', text=tw.dedent('''
<b>Физическое лицо</b> ⭐
\n• Вам достаточно предоставить паспорт, инн и снилс и ваша форма сотрудничества подтверждена. \
Обратите внимание по физическому лицу необходимо оплатить налог 13% .
\n• Можно совмещать разные виды деятельности. Можно работать с 18 лет. Сотрудничество с проектом «Свой в Альфе» \
дает возможность студентам пройти практику и получить свой первый доход.
        '''))

    await callback_query.message.answer(parse_mode='HTML', text=tw.dedent('''
<b>Можно совмещать разные виды деятельности</b> ⭐
\n• Можно работать с 18 лет. 
\n• Сотрудничество с проектом «Свой в Альфе» дает возможность студентам пройти практику и получить свой первый доход.
            '''), reply_markup=continue_kb)

    await callback_query.answer()


@router.callback_query(
    lambda c: c.data == 'advantage_income_without_investment_accept' or
              c.data == 'advantage_income_without_investment_continue')
async def advantage_income_without_investment_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с преимуществом "Доход без вложений"
    """
    photo = FSInputFile(path_to_advantage_income_without_investment)
    next_advantage_kb = make_accept_details_kb(next_advantage_name='cooperation_bank',
                                               current_advantage_details_name='income_without_investment')

    await callback_query.message.answer_photo(parse_mode='HTML',
                                              photo=photo, reply_markup=next_advantage_kb, caption=tw.dedent('''
Доход без вложений 💳
Проект «Свой в Альфе» это бизнес-модель, которая дает возможность любому гражданину РФ без первоначального \
капитала начать свой бизнес либо просто создать <b>дополнительный источника дохода без вложений</b>.
    '''))
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'advantage_income_without_investment_details')
async def advantage_income_without_investment_details_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальным описанием преимущества - "Доход без вложений"
    """
    photo = FSInputFile(path_to_advantage_income_without_investment_details)
    continue_kb = make_continue_kb(next_advantage_name='cooperation_bank')

    await callback_query.message.answer_photo(parse_mode='HTML',
                                              photo=photo, reply_markup=continue_kb, caption=tw.dedent('''
Можно зарабатывать <b>без финансовых вложений и риска потерять деньги</b>, ты <b>приобретаешь финансовую \
независимость</b>, у тебя появляется дело, которое будет по душе и будет приносить не только деньги, но и \
удовольствие. <b>Не нужны никакие вложения кроме души и желания помочь людям.</b>
    '''))
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'advantage_cooperation_bank_accept' or
                                 c.data == 'advantage_cooperation_bank_continue')
async def advantage_cooperation_bank_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с преимуществом "Сотрудничество с крупным российским банком"
    """
    photo = FSInputFile(path_to_advantage_cooperation_bank)
    next_advantage_kb = make_accept_details_kb(next_advantage_name='unlimited_income',
                                               current_advantage_details_name='cooperation_bank')

    await callback_query.message.answer_photo(parse_mode='HTML',
                                              photo=photo, reply_markup=next_advantage_kb, caption=tw.dedent('''
<b>Сотрудничество с крупным российским банком</b>🔥
\nПроект <b>«Свой в Альфе»</b> это маркетинговый проект от \
<b>крупного российского банка</b>, входящего в <b>топ-3</b> банков России.
    '''))
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'advantage_cooperation_bank_details')
async def advantage_cooperation_bank_details_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальным описанием преимущества - "Сотрудничество с крупным российским банком"
    """
    photo = FSInputFile(path_to_advantage_cooperation_bank_details)
    continue_kb = make_continue_kb(next_advantage_name='unlimited_income')

    await callback_query.message.answer_photo(parse_mode='HTML',
                                              photo=photo, caption=tw.dedent('''
<b>• Проект "Свой в Альфе"</b> сотрудничает с <b>крупнейшим банком России</b> занимающий <b>4-ое</b> место по размеру \
активов: 8,79 триллионов рублей и это один из самых надежных банков.
\n<b>• Банк победил в главных номинациях премии «Банки.ру»</b> по итогам \
2023 года. Год основания <b>20 декабря 1990 года.</b> Вошел в <b>топ-3</b> российских банков с лучшей репутацией.
    '''), reply_markup=continue_kb)

    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'advantage_unlimited_income_accept' or
                                 c.data == 'advantage_unlimited_income_continue')
async def advantage_unlimited_income_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с преимуществом "Неограниченный доход"
    """
    photo = FSInputFile(path_to_advantage_unlimited_income)
    next_advantage_kb = make_accept_details_kb(next_advantage_name='free_schedule',
                                               current_advantage_details_name='unlimited_income', )

    await callback_query.message.answer_photo(parse_mode='HTML',
                                              photo=photo, reply_markup=next_advantage_kb, caption=tw.dedent('''
<b>Неограниченный доход</b>🌟
\nПроект предоставляет возможность получать почти <b>неограниченный доход</b>, чего \
сложно достичь просто работая по найму.
    '''))

    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'advantage_unlimited_income_details')
async def advantage_unlimited_income_details_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальным описанием преимущества - "Неограниченный доход"
    """
    photo_group = [path_to_advantage_unlimited_income_details_jan, path_to_advantage_unlimited_income_details_feb,
                   path_to_advantage_unlimited_income_details_march, path_to_advantage_unlimited_income_details_apr,
                   path_to_advantage_unlimited_income_details_may, path_to_advantage_unlimited_income_details_common]
    media_group = [InputMediaPhoto(media=types.FSInputFile(path)) for path in photo_group]

    continue_kb = make_continue_kb(next_advantage_name='free_schedule')

    await callback_query.message.answer_media_group(media=media_group)
    await callback_query.message.answer(parse_mode='HTML',
                                        text=tw.dedent('''
✅<b>• Размер дохода</b> зависит только от тебя и нет «потолка», в среднем </b>от 25 000р. до 2 000 000р. и более в \
месяц в зависимости от того сколько времени и сил ты будешь уделять проекту.
    '''))
    await callback_query.message.answer(parse_mode='HTML',
                                        text=tw.dedent('''
✅<b>• Можно рассматривать этот доход просто как дополнительный источник средств</b>, а можно перестать работать по \
найму и легко построить <b>свой бизнес</b> в любом возрасте и с любым опытом работы при мощной поддержке опытных \
наставников.
        '''), reply_markup=continue_kb)
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'advantage_free_schedule_accept' or
                                 c.data == 'advantage_free_schedule_continue')
async def advantage_free_schedule_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с преимуществом "Свободный график"
    """
    photo = FSInputFile(path_to_advantage_free_schedule)
    next_advantage_kb = make_accept_details_kb(next_advantage_name='remote_work',
                                               current_advantage_details_name='free_schedule', )

    await callback_query.message.answer_photo(parse_mode='HTML',
                                              photo=photo, reply_markup=next_advantage_kb, caption=tw.dedent('''
<b>Свободный график</b>😊
\nПроектом «Свой в Альфе» ты можешь заниматься <b>по свободному графику</b>, в своем комфортном темпе.
    '''))
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'advantage_free_schedule_details')
async def advantage_free_schedule_details_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальным описанием преимущества - "Свободный график"
    """
    photo = FSInputFile(path_to_advantage_free_schedule_details)
    continue_kb = make_continue_kb(next_advantage_name='remote_work')

    await callback_query.message.answer_photo(parse_mode='HTML',
                                              caption=tw.dedent('''
• <b>Ты сам выбираешь</b> сколько тебе работать, гибкий рабочий график помогает найти баланс между работой семьей и \
личной жизнью. 
\n• Люди, с таким графиком работы, могут чувствовать себя <b>более счастливыми</b>. На фрилансе тебе всегда хочется \
развиваться, узнавать новое и расти профессионально.
    '''), reply_markup=continue_kb, photo=photo)

    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'advantage_remote_work_accept' or
                                 c.data == 'advantage_remote_work_continue')
async def advantage_remote_work_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с преимуществом "Удаленная работа"
    """
    photo = FSInputFile(path_to_advantage_remote_work)
    next_advantage_kb = make_accept_details_kb(next_advantage_name='free_study',
                                               current_advantage_details_name='remote_work', )

    await callback_query.message.answer_photo(parse_mode='HTML',
                                              photo=photo, reply_markup=next_advantage_kb, caption=tw.dedent('''
<b>Удаленная работа</b> 🥰
\nРаботайте дистанционно <b>прямо из дома</b>, в любом месте где есть интернет.
    '''))
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'advantage_remote_work_details')
async def advantage_remote_work_details_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальным описанием преимущества - "Удаленная работа"
    """
    photo = FSInputFile(path_to_advantage_remote_work_details)
    continue_kb = make_continue_kb(next_advantage_name='free_study')

    await callback_query.message.answer_photo(parse_mode='HTML',
                                              caption=tw.dedent('''
<b>Свобода места работы и времени</b> 🌍⏳
\n• <b>не нужно ходить в офис</b> и вставать утром в дикую рань, трястись в автобусе или метро. Ты сам выбираешь, 
где тебе сегодня работать: дома, в кафе или вообще собрать вещи и уехать в другой город. 
\n• <b>не нужно выпрашивать отпуск</b> и выходные, потому что ты их можешь устроить себе в любой момент: вообще - \
полная свобода действий. 
\n• работа через интернет позволяет <b>масштабироваться</b> и зарабатывать деньги уютно устроившись на любимом диване.
    '''), reply_markup=continue_kb, photo=photo)

    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'advantage_free_study_accept' or
                                 c.data == 'advantage_free_study_continue')
async def advantage_free_study_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с преимуществом "Бесплатное обучение"
    """
    photo = FSInputFile(path_to_advantage_free_study)
    next_advantage_kb = make_accept_details_kb(next_advantage_name='privilege',
                                               current_advantage_details_name='free_study')

    await callback_query.message.answer_photo(parse_mode='HTML',
                                              photo=photo, reply_markup=next_advantage_kb, caption=tw.dedent('''
<b>Бесплатное обучение</b>✌️
\nВ рамках проекта «Свой в Альфе» ты попадаешь в команду, где ты можешь пройти профессиональное \
обучение абсолютно бесплатно.
    '''))
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'advantage_free_study_details')
async def advantage_free_study_details_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальным описанием преимущества - "Бесплатное обучение"
    """
    photo = FSInputFile(path_to_advantage_free_study_details)
    continue_kb = make_continue_kb(next_advantage_name='privilege')

    await callback_query.message.answer_photo(parse_mode='HTML', reply_markup=continue_kb, photo=photo,
                                              caption=tw.dedent('''
<b>Обучающие модули устроены таким образом, что ты быстро изучишь суть проекта и возможности, которые предоставляет \
известный российский банк.</b>
\n• Ты можешь обучаться онлайн у наставников-профессионалов, и 24/7 тебе доступна \
тех. поддержка и онлайн обучение в личном кабинете партнера, а также ты можешь обучаться оффлайн посещая презентации, \
круглые столы и форумы с куратором твоего региона.
    '''))

    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'advantage_privilege_accept' or
                                 c.data == 'advantage_privilege_continue')
async def advantage_privilege_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с преимуществом "Привилегии для своих"
    """
    photo = FSInputFile(path_to_advantage_privilege)
    next_advantage_kb = make_accept_details_kb(next_advantage_name='new_profession',
                                               current_advantage_details_name='privilege', )

    await callback_query.message.answer_photo(parse_mode='HTML',
                                              photo=photo, reply_markup=next_advantage_kb, caption=tw.dedent('''
<b>Привилегии «Для своих»</b> 🥰
\n<b>Возможность получать уникальные привилегии по продуктам</b>, \
которые доступны только для партнеров проекта «Свой в Альфе»
    '''))
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'advantage_privilege_details')
async def advantage_privilege_details_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальным описанием преимущества - "Привилегии для своих"
    """
    # photo = FSInputFile(path_to_advantage_privilege_details)
    photo_group = [path_to_advantage_privilege_details, path_to_advantage_privilege_details_2]
    media_group = [InputMediaPhoto(media=types.FSInputFile(path)) for path in photo_group]

    continue_kb = make_continue_kb(next_advantage_name='new_profession')

    await callback_query.message.answer_media_group(media=media_group)

    await callback_query.message.answer(parse_mode='HTML', text=tw.dedent('''
• <b>Эксклюзивный кэшбэк</b> для вас и ваших клиентов. Возврат кэшбэка деньгами на карту до 5000 руб. в месяц по \
обычной дебетовой карте. Повышенный кэшбэк по актуальным категориям, приветственный кэшбэк 500 рублей новым клиентам \
банка. Супер-кэшбэк до 100% на барабане и лучший кэшбэк от партнеров 💰 \
\n• Возможность получать <b>гарантированный кэшбэк</b> на самые популярные категории : «Продукты», «АЗС», «Здоровье», \
«Кафе и рестораны», «Маркетплейсы» 💵\
\n• Выгодные тарифы и новые продукты 🔥 \
\n• Участие в привилегированном клубе <b>«Для своих»</b> 😊 \
\n• <b> Премиальная бонусная система по выплатам.</b>  Бонус за новых партнеров <b>до 5000 р.</b> за каждого партнера. \
Бонусный дуэт за развитие своего партнера <b>до 80 000 р.</b> за каждого. И бонус за все поколения \
<b>до 5 000 000 р.</b> ✨\
\n• Приглашения на <b>мероприятия с руководителями и VIP клиентами</b> крупного российского банка ⚡️\
\n• <b>Бесплатное участие в рейтинговых поездках</b> в рамках проекта «Свой в Альфе» 🏆\
    '''), reply_markup=continue_kb)

    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'advantage_new_profession_accept' or
                                 c.data == 'advantage_new_profession_continue')
async def advantage_new_profession_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с преимуществом "Новая профессия эксперта по личным финансам"
    """
    photo = FSInputFile(path_to_advantage_new_profession)
    next_advantage_kb = make_accept_details_kb(next_advantage_name='how_to_make_10k',
                                               current_advantage_details_name='new_profession', )

    await callback_query.message.answer_photo(parse_mode='HTML',
                                              photo=photo, reply_markup=next_advantage_kb, caption=tw.dedent('''
<b>Новая профессия эксперта по личным финансам 👍</b>
\nПовысь свою <b>финансовую грамотность</b> и помоги стать более финансово \
грамотными своему окружению.
    '''))
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'advantage_new_profession_details')
async def advantage_new_profession_details_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальным описанием преимущества - "Новая профессия эксперта по личным финансам"
    """
    photo = FSInputFile(path_to_advantage_new_profession_details)
    continue_kb = make_continue_kb(next_advantage_name='how_to_make_10k')

    await callback_query.message.answer_photo(parse_mode='HTML',
                                              caption=tw.dedent('''
<b>Освой профессию эксперта и получай от 25 000 р. в месяц за работу 5 часов в неделю. Стань «своим человеком» в \
банке</b> ❤️ \
\n• Ты разберешься в теме личных финансов. Узнаешь как составить личный финансовый план для себя и своих клиентов; \
\n• Научишься строить личный бренд эксперта по личным финансам; \
\n• Сможешь консультировать клиентов; \
\n• Научишься делать самые выгодные предложения клиентам и работать с их возражениями, узнаешь как обучать свою команду. \
    '''), reply_markup=continue_kb, photo=photo)


@router.callback_query(lambda c: c.data == 'advantage_how_to_make_10k_accept' or
                                 c.data == 'advantage_how_to_make_10k_continue')
async def advantage_how_to_make_10k_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с хуком о том "как заработать 10к"
    """
    photo = FSInputFile(path_to_how_to_make_10k)
    next_advantage_kb = make_hook_10k_want_later_kb()

    await callback_query.message.answer_photo(photo=photo, reply_markup=next_advantage_kb, caption=tw.dedent('''
Много информации? 👀
\nСчитаешь, что потратил время зря? 😫
\nА хочешь я тебе докажу что ты можешь заработать 10 000 р. прямо сейчас? 🤑
    '''))
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'hook_10k_want')
async def advantage_how_to_make_10k_info_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с информацией о том "как заработать 10к"
    """
    photo = FSInputFile(path_to_how_to_make_10k_details)
    next_advantage_kb = make_become_partner_kb()

    await callback_query.message.answer_photo(parse_mode='HTML',
                                              photo=photo, reply_markup=next_advantage_kb, caption=tw.dedent('''
\n<b>Как заработать 10000 р за 1 день?</b> 👀 \
\n1. Выдать <b>6 дебетовых карт</b> новым клиентам банка, можно близким родственникам или друзьям, которые тебя \
обязательно поддержат. За каждого нового клиента тебе начислят 17 баллов (8б - дебетовая карта, 5б - новый клиент, \
3б - подключение госуслуг к банку, 1б - сделать банк основным для сбп). \
\n2. Важно чтобы твой клиент потратил картой за месяц <b>от 3000 р.</b> и более, тогда ему начисляют приветственный \
кэшбэк <b>500 р.</b>, а тебе соответствующие баллы \
\n3. Шесть клиентов x 17 баллов за каждого x 100 руб. (стоимость 1б на старте) = <b>10200 руб.</b> \
\n4. <b>Никуда ходить не надо</b>, курьеры сами привезут карты твоим клиентам домой. \
\n\n<b>Нажми “стать партнером” и получи возможность заработать 10.000 рублей за 1 день</b> \
    '''))
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'become_partner')
async def check_partner_or_no_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с вопросом о том является ли клиент
    """
    photo = FSInputFile(path_to_check_partner)
    next_advantage_kb = make_check_partner_or_no_kb()

    await callback_query.message.answer_photo(parse_mode='HTML',
                                              photo=photo, reply_markup=next_advantage_kb, caption=tw.dedent('''
<b>Ты уже являешься клиентом Альфа банка?</b>
Надеюсь что у тебя уже есть приложение банка в телефоне?
Тогда становись партнером <b>прямо сейчас!</b>
    '''))
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'check_partner_no')
async def advantage_how_to_make_10k_info_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с информацией о том как стать партнером
    """
    next_advantage_kb = make_partner_url_kb()

    photo_group = [path_to_card_order_cashback, path_to_card_order_employee]
    media_group = [InputMediaPhoto(media=types.FSInputFile(path)) for path in photo_group]

    await callback_query.message.answer_media_group(media=media_group)

    await callback_query.message.answer(parse_mode='HTML', disable_web_page_preview=True,
                                        reply_markup=next_advantage_kb, text=tw.dedent(f'''
<b>Если нет, то сначала закажи карту, установи приложение и только после этого проходи по партнерской ссылке!</b>
\n\n<b>Закажи карту и получи 500 руб.</b> \
\n\n<a href="{CARD_ORDER_LINK_FOR_OUR}">"ДЛЯ СВОИХ"</a> 👈 НАЖМИ ЗДЕСЬ ЧТОБЫ ПЕРЕЙТИ
\n• Для всех клиентов, смотри описание выше, преимущество для клиентов и сотрудников сетевых компаний - \
кэшбэк на товарооборот в их компании. \
\n\n<a href="{CARD_ORDER_LINK_WITH_CASHBACK}">"С ЛЮБИМЫМ КЭШБЭКОМ"</a> 👈 НАЖМИ ЗДЕСЬ ЧТОБЫ ПЕРЕЙТИ
\n• Для новых клиентов, повышенные категории кэшбэка. \
\n<b>Закажи карту - получи 500   р и думай!</b>
\n<b>Тестируй - получи кэшбэк до 5000 р. в месяц!</b>  
\n<b>Когда надумаешь рекомендовать эту карту - напиши наставнику и он пришлет тебе ссылку на регистрацию в \
проекте «Свой в Альфе»!</b>
    '''))
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'card_order')
async def advantage_card_order_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальной информацией по оформлению карты
    """
    photo = FSInputFile(path_to_card_order)

    await callback_query.message.answer_photo(parse_mode='HTML',
                                              caption=tw.dedent(f'''
<b>Тогда пока закажи карту и получи 500 руб.</b> \
\n\n<a href="{CARD_ORDER_LINK_FOR_OUR}">"ДЛЯ СВОИХ"</a> 👈 НАЖМИ ЗДЕСЬ ЧТОБЫ ПЕРЕЙТИ
\n• Для всех клиентов, смотри описание выше, преимущество для клиентов и сотрудников сетевых компаний - \
кэшбэк на товарооборот в их компании. \
\n\n<a href="{CARD_ORDER_LINK_WITH_CASHBACK}">"С ЛЮБИМЫМ КЭШБЭКОМ"</a> 👈 НАЖМИ ЗДЕСЬ ЧТОБЫ ПЕРЕЙТИ
\n• Для новых клиентов, повышенные категории кэшбэка. \
\n<b>Закажи карту - получи 500 р. и думай!</b>
\n<b>Тестируй - получи кэшбэк до 5000 р. в месяц!</b>
\n<b>Когда надумаешь рекомендовать эту карту - напиши наставнику и он пришлет тебе ссылку на регистрацию в \
проекте «Свой в Альфе»!</b>
\nТолько твоя ссылка партнера* даст тебе возможность получать доход с максимальной выгодой! 
\n\n*Предупреждение: НЕ БЕРИ ССЫЛКУ ИЗ КЛИЕНТСКОГО ПРИЛОЖЕНИЯ АЛЬФА БАНКА, это единовременная выплата за рекомендацию карт.
\nЧтобы получать неограниченный официальный доход без вложений запроси ссылку у своего наставника - от кого узнал о \
проекте, стань официальным партнером  проекта “Свой в Альфе”.
'''), photo=photo, reply_markup=make_card_order_kb())

    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'call_mentor')
async def advantage_call_mentor_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция отсылает контакт ментора в чат
    """
    mentor_contact = types.Contact(
        phone_number='+7 900 323 6934',
        first_name='Александр',
        last_name='Дружинин',

    )
    await callback_query.message.answer_contact(phone_number=mentor_contact.phone_number,
                                                first_name=mentor_contact.first_name,
                                                last_name=mentor_contact.last_name)
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'get_url' or c.data == 'check_partner_yes')
async def partner_url_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с партнерской ссылкой
    """

    keyboard = make_register_kb()

    await callback_query.message.answer(parse_mode='HTML', disable_web_page_preview=True,
                                        reply_markup=keyboard, text=tw.dedent(f'''
<b><a href="{PARTNER_LINK}">Жми чтобы стать партнером!</a></b>
'''))
    await callback_query.answer()


# DEPRECATE?
@router.callback_query(lambda c: c.data == 'register_complete')
async def advantage_register_complete_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальной информацией о том что делать после регистрации
    """
    photo = FSInputFile(path_to_registration)
    keyboard = make_common_kb(next_handler_name='card_order_info',
                              current_handler_details_name='answers_test',
                              first_key_text='Закажи карту, на которую будет приходить твой доход',
                              second_key_text='Подробнее')

    await callback_query.message.answer_photo(photo=photo, reply_markup=keyboard, caption=tw.dedent('''
     Пройди обучение в личном кабинете партнера и сдай тест: получи 200 руб!» если есть сложности с прохождением \
     теста, ищи ответы здесь
        '''))
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'answers_test')
async def advantage_answers_test_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальной информацией с ответами на тест
    """
    photo = FSInputFile(path_to_answers_test)
    keyboard = make_info_after_test_kb()

    await callback_query.message.answer_photo(photo=photo, caption=tw.dedent('''
\nПРАВИЛЬНЫЕ ОТВЕТЫ НА ТЕСТ : \
\n🅰️Проект Свой в Альфе - это... \
\n✅Возможность самому выбирать, \
сколько времени уделять проекту \
\n✅Неограниченный доход без \
вложений и рисков \
\n✅Сотрудничество с крупным частным банком, которому доверяют миллионы клиентов. \
'''))

    await callback_query.message.answer(text=tw.dedent('''
\n🅰️Отметьте преимущества дебетовой Альфа-Карты для СВОИХ: \
\n✅Бесплатное обслуживание. \
Всегда, без условий. \
\n✅Кэшбэк до 100% на категорию суперкэшбэка, 5% в трёх категориях на выбор и 1% на всё + партнёрский кэшбэк до 50% \
(категорийный кэшбэк - до 5000 ₽, партнерский кэшбэк- безлимитно) \
\n✅Кэшбэк 5% на покупки в MLM-
компаниях
'''))

    await callback_query.message.answer(text=tw.dedent('''
\n🅰️Кому подходит Альфа-Карта с любимым кэшбэком: \

\n✅Для новых клиентов банка, кто заинтересован в кэшбэке по категориям: вкусный (продукты, кафе и рестораны), \
автомобильный (заправки и авто), модный (одежда и обувь, красота), молодежный (фастфуд, развлечения), полезный \
(продукты, здоровье, АЗС)
'''))

    await callback_query.message.answer(text=tw.dedent('''
\n🅰️Отметьте преимущества Детской карты?

\n✅Кэшбэк до 2000 ₽
\n✅Детское приложение с денежными призами
\n✅Родители в курсе всех трат - могут моментально пополнять счёт ребенка, устанавливать лимит, контролировать расходы \
ребёнка в своем приложении
'''))

    await callback_query.message.answer(text=tw.dedent('''
\n🅰️Ваш клиент рассказал, что планирует сделать ремонт в квартире и ему нужны деньги.
\nКакую кредитную карту вы ему порекомендуете в первую очередь?

\n✅Целый 
'''))

    await callback_query.message.answer(text=tw.dedent('''
\n🅰️ Когда можно снимать, переводить деньги и пополнять накопительный Альфа-Счёт?

\n✅В любое время
'''))

    await callback_query.message.answer(text=tw.dedent('''
\n🅰️ Что делает агент Свой в Альфе, чтобы получать доход

\n✅Пользуется продуктом сам
\n✅Рекомендует продукты и сервисы банка знакомым
\n✅Приглашает в команду агентов, которые делают то же самое
\n✅Строит бизнес вместе с
командой
'''))

    await callback_query.message.answer(text=tw.dedent('''
\n🅰️ Выберите обязательные условия для получения выплаты агента:

\n✅Не менее 40 баллов в месяц от
личных клиентов
'''))

    await callback_query.message.answer(reply_markup=keyboard, text=tw.dedent('''
\n🅰️Какой способ работы с клиентами эффективнее?

\n✅ Агент нашёл 5 клиентов, которым оформил 5 Альфа-Карт для своих, 2 Детские карты, 2 Кредитные карты Целый год без \
%, проконсультировал по открытию 3 Накопительных Альфа-Счетов, помог подключить Госуслуги и выбрать Альфа-Банк \
основным для СБП
    '''))

    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'debit_card_order_info')
async def advantage_debit_card_order_info_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальной информацией о том как сделать дебетовую карту
    """
    photo_group = [path_to_card_order_cashback, path_to_card_order_employee]
    media_group = [InputMediaPhoto(media=types.FSInputFile(path)) for path in photo_group]
    keyboard = make_i_order_card_kb()

    await callback_query.message.answer_media_group(media=media_group)

    await callback_query.message.answer(parse_mode='HTML',
                                        disable_web_page_preview=True,
                                        reply_markup=keyboard,
                                        text=tw.dedent(f'''
\n\n<a href="{CARD_ORDER_LINK_FOR_OUR}">"ДЛЯ СВОИХ"</a> 👈 НАЖМИ ЗДЕСЬ ЧТОБЫ ПЕРЕЙТИ
\n• Для всех клиентов, смотри описание выше, преимущество для клиентов и сотрудников сетевых компаний - \
кэшбэк на товарооборот в их компании. \
\n\n<a href="{CARD_ORDER_LINK_WITH_CASHBACK}">"С ЛЮБИМЫМ КЭШБЭКОМ"</a> 👈 НАЖМИ ЗДЕСЬ ЧТОБЫ ПЕРЕЙТИ
\n• Для новых клиентов, повышенные категории кэшбэка. \
\n<b>Закажи карту - получи 500   р и думай!</b>
\n<b>Тестируй - получи кэшбэк до 5000 р. в месяц!</b>  
\n<b>Когда надумаешь рекомендовать эту карту - напиши наставнику и он пришлет тебе ссылку на регистрацию в \
проекте «Свой в Альфе»!</b>
        '''))

    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'i_order_card')
async def advantage_i_order_card_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальной информацией о том что делать после заказа карты
    """
    keyboard = make_call_mentor_kb()

    photo_group = [path_to_card_order_cashback, path_to_card_order_employee]
    media_group = [InputMediaPhoto(media=types.FSInputFile(path)) for path in photo_group]

    await callback_query.message.answer_media_group(media=media_group)

    await callback_query.message.answer(reply_markup=keyboard,
                                        parse_mode='HTML',
                                        text=tw.dedent('''
<b>Инструкция, что нужно сделать при получении карты:</b>
\n1. Получить пластик (карту);
2️. Установить приложение Альфа-банка;
3️. Выбрать кэшбэк по категориям и покрутить барабан;
4️. Подключить Госуслуги;
5️. Сделать банк основным для переводов (просто будет появляться первым при выборе);
6️. Альфа-чек (смс оповещения 99₽) нужны чтобы быть в курсе всех списаний, можно оставить, чтобы обезопасить себя, \
или отключить;
7️. Услуга бесплатные переводы. Все переводы первые 2 месяца бесплатно, далее бесплатно, при покупках более 10 000 \
руб. в месяц , если меньше, то 149 руб. в месяц. Опцию при желании можно отключить;
При желании подключаем Альфа пэй или отдельно в витрине можно заказать платежный стикер, 490 ₽ в 1-ый год, \
потом бесплатно;
9️. Оплатить любую коммунальную услугу в течение месяца;
10. Потратить КАРТОЙ в течение 3-х - 5-ти дней от 1000₽, чтобы активировать карту, а затем в течение 30 дней \
потрать еще 2 000 р чтобы  через 5 рабочих дней вернулось 500₽. 
ВАЖНО: Оплата ЖКХ, мобильной и интернет связи, а также переводы, и оплата по QR коду, НЕ ЯВЛЯЮТСЯ ПОКУПКОЙ и \
приветственный бонус в этом случае не начисляется.
\n\nЕсли остались вопросы - напиши наставнику 👇
'''))

    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'info_after_test_details')
async def advantage_i_order_card_details_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальной информацией о карте(статистика)
    """
    photo_group = [path_to_cashback_and_sales_1, path_to_cashback_and_sales_2,
                   path_to_cashback_and_sales_3, path_to_cashback_and_sales_4]
    media_group = [InputMediaPhoto(media=types.FSInputFile(path)) for path in photo_group]

    keyboard = make_call_mentor_kb()
    await callback_query.message.answer_media_group(media=media_group)

    await callback_query.message.answer(parse_mode='HTML',
                                        text=tw.dedent('''
Кстати, ты сможешь предлагать не просто карты, а <b>карты крупного российского банка</b>, \
который входит в <b>топ-5 банков</b> России. 
\n\n<b>И вот каковы преимущества продуктов банка:</b> 
\n1. Обслуживание дебетовых карт — <b>всегда бесплатно</b>;
\n2. Возможность делать <b>бесплатные переводы</b>;
\n3. <b>Оплата ЖКХ</b>, штрафов и налогов <b>без комиссии</b>;
\n4. Приветственный <b>кэшбэк 500 р.</b>; 
\n5. <b>Востребованные категории кэшбэков:</b> продукты, здоровье, АЗС, кафе и рестораны, маркетплейсы, развлечения, \
ремонт, такси и т.д. в среднем 3-5% от трат. До 100% кэшбэка на барабане;
        '''))

    await callback_query.message.answer(reply_markup=keyboard,
                                        parse_mode='HTML',
                                        text='''
\n6. Максимальная <b>сумма кэшбэка 5000 р.</b> в месяц по дебетовой карте, <b>7000 р.</b> при подписке  “Альфа Смарт” \
и <b>15 000 р.</b> в месяц по премиум карте. 
Возврат кэшбэка деньгами на карту;
\n7. <b>Эксклюзивная категория кэшбэка 5-7%</b> на товарооборот для МЛМ компаний;
\n8. Возможность <b>заказать комбо-карту 2 в 1</b> дебетовая и кредитная на одном пластике;
\n9. Возможность получить <b>беспроцентную рассрочку</b> на 365 дней по кредитной карте;
\n10. Возможность получать <b>кэшбэк по кредитной карте</b>;
\n11. <b>Доставка карты</b> в удобное место и время;    
    ''')
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'how_to_make_50k')
async def advantage_how_to_make_50k_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальной информацией о карте(статистика)
    """
    photo = FSInputFile(path_to_how_to_make_50k)
    keyboard = make_common_kb(next_handler_name='study_in_personal_account',
                              current_handler_details_name='study_in_personal_account_details',
                              first_key_text='С чего начать?',
                              second_key_text='Как находить клиентов?')

    await callback_query.message.answer_photo(photo=photo, reply_markup=keyboard, caption=tw.dedent('''
\nПЛАН КАК ЗАРАБОТАТЬ 50000 ₽:
\n1. Ты оформил 10 ДК новым клиентам 
\nС 1 ДК можно получить 17 б! 
\nЕсли это новый клиент для банка, подключил госуслуги и сделал банк основным для СБП.
\nПРИМЕР: 
\n8Б- дебетовая карта
\n5Б- новый клиент
\n3Б- подключение Госуслуг
\n1Б- основной для СБП
\n\n———————————
\n\nИтого : 17 Б( 1 балл = 100 р) 
\n17 Б • 10 кл = 170 Б 
\n170Б •100 р = 17000 
\n\n2 . Ты оформил 5 КК 
\nОдна КК даёт 15 Б 
\n15Б • 5 кл = 75 Б
\n75Б •100 р = 7500
\n\nИз 10 клиентов 5 человек  станут агентами в статусе А1 т.е. наберут по 40Б каждый 
\n\n5 агентов •40Б = 200 Б
\n200Б •20 р = 4000 (20 р это стоимость 1 балла за агентов 1 поколения)
\n\n+ БОНУС! 
\nЗа каждого твоего нового агента , который набрал 40 Б и более ты получаешь по 5000 р
\n5 агентов А1 • 5000 р = 25000
\n\n17000+7500+4000+25000= 53500 
\n\nИТОГО : 53 500 ₽ !!!
        '''))

    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'study_in_personal_account' or c.data == 'study_in_personal_account_details')
async def advantage_personal_account_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальной информацией о обучении в личном кабинете
    """
    photo = FSInputFile(path_to_filler_1)
    keyboard = make_study_in_personal_acc_triple_kb()

    await callback_query.message.answer_photo(photo=photo, reply_markup=keyboard, caption=tw.dedent('''
 Пройди обучение в личном кабинете партнера и сдай тест: получи 200 руб! 
 
        '''))

    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'mentor_details')
async def advantage_mentor_details_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальной информацией о личном наставнике
    """
    photo = FSInputFile(path_to_filler_2)

    await callback_query.message.answer_photo(photo=photo,
                                              parse_mode='HTML',
                                              caption=tw.dedent('''
<b>Запишись на индивидуальную консультацию в телеграм: напиши наставнику: "Консультация”</b>
        '''))

    mentor_contact = types.Contact(
        phone_number='+7 900 323 6934',
        first_name='Александр',
        last_name='Дружинин',

    )
    await callback_query.message.answer_contact(phone_number=mentor_contact.phone_number,
                                                first_name=mentor_contact.first_name,
                                                last_name=mentor_contact.last_name)

    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'own_at_alpha')
async def advantage_own_at_alpha_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальной информацией о преимуществах "своего в Альфе"
    """
    photo = FSInputFile(path_to_own_at_alpha)

    await callback_query.message.answer_photo(photo=photo, caption=tw.dedent('''
\nПреимущества партнера проекта "Свой в Альфе"
\n\n1. Есть ли какие-то обязательства?
\nОбязательств по работе нет, но если ты хочешь получать выплаты за текущий месяц нужно обязательно набрать от \
40 баллов. 
\n\nЧто такое 40 баллов? Это 3 новые оформленные и активированные дебетовые карты с выполненными целевыми действиями \
выданные личным клиентам. В проекте "Свой в Альфе" есть система дохода, по которой каждый выданный продукт и каждое \
целевое действие клиента оценивается в баллах. Подробнее о системе дохода смотрите в обучающем модуле в личном \
кабинете партнера проекта "Свой в Альфе". 
\n\n2. Как начисляются баллы? 
\n\nПо системе дохода " Свой в Альфе" 
        '''))
    await callback_query.message.answer(text='''
\nПример: дебетовая карта дает 17 баллов: 8 баллов - дебетовая карта; 5 баллов - новый клиент, \
3 балла - подключенные госуслуги к банку, 1 балл - сделать банк основным для СБП. 
\n\n3. Как и куда я получу деньги? 
\n\nДля того чтобы получить выплату за текущий месяц нужно заполнить реквизиты, предоставить документы и \
набрать от 40 балллов. 
\n\nДля получения выплат нужно подтвердить акты в личном кабинете "Свой в Альфе". Срок выплаты от 16 рабочих дней с \
начала следующего месяца, выплаты проводятся от 3000 рублей. Если сумма выплаты меньше, то она сохранится и \
будет доступна в следующем месяце.
\nДеньги придут на твой личный банковский счет указанный при оформлении в платежной информации в личном кабинете \
"Свой в Альфе".    
    ''')
    await callback_query.message.answer(text='''
4. Буду ли я платить налоги?
\nДа, обязательно, это официальный проект. 
\nДля выплат налогов необходимо установить приложение "Мой налог" и оплачивать банковской картой. В приложении \
"Мой налог" нужно зайти после 12 го числа, на главной странице под текстом "К оплате" увидите сумму налога. \n
Нажмите на сумму, чтобы перейти к оплате. 
\n\n5. Как долго этот проект будет работать? 
\n\nХороший вопрос! Давай посчитаем, население России 144 млн. человек из них 13 млн. являются активными \
пользователями банка. В год добавляется около 1 млн новых клиентов. Сколько времени потребуется, чтобы охватить \
весь рынок? Как считаешь?
\n\nВот видишь, рынок еще абсолютно пустой, охвачено лишь около 10% населения России, при развитии даже большими \
темпами еще есть не менее 50 лет на развитие. 
\n\nПрисоединяйся к проекту прямо сейчас и стань партнером номером 1 в России.
\n6. Откуда банк берет деньги?
\n\nЛюбое предприятие закладывает определенные издержки на рекламу, также как и банк. 
\n\nВыплаты партнерам проекта "Свой в Альфе", а также кэшбэк для клиентов выплачивается из этого бюджета.    
    ''')

    await callback_query.message.answer(text='''
Подробнее:
\n\nУ банка есть несколько каналов рекламы. Проект "Свой в Альфе" является одним из таких каналов \
и занимает 2-ое место из 10. 
\nВ этом году на развитие проекта "Свой в Альфе" банк выделил 9 млрд. руб.
\n\n7. Где мне брать клиентов: 
\n\nПервыми твоими клиентами могут стать родные и близкие, которые обязательно тебя поддержат. 
\n\nЕсть круг друзей, коллег, знакомых, потом ты можешь выйти в социальные сети и работать удаленно, \
что позволяет проект "Свой в Альфе". 
\n\nУ нас для тебя есть разработанная система поиска и привлечения клиентов. У тебя нет необходимости постоянно \
заниматься поиском клиентов, а надо лишь найти активных партнеров и выстроить систему, которая будет работать на тебя.
        ''')
    await callback_query.message.answer(text='''
\n\n8. Насколько это официально и безрисково?
\nПроект "Свой в Альфе" - это официальная партнерская программа банка, которая запустилась в июне 2023 года.
\n\nЭто легальный готовый бизнес под ключ он не требует никаких вложений ни со стороны клиента, \
ни со стороны партнера, соответственно никаких рисков потери средств нет. 
\n\nПроект "Свой в Альфе" это официальный легальный маркетинговый канал крупного российского банка одного из \
ведущих и самых успешных банков России. 
\n\nКак ты понимаешь рисков нет, единственный риск это недополученная тобой выгода, упущенный шанс и возможность. 
\n\nТы получаешь официальный доход, а банк выплачивает налоги с денежных выплат своим партнерам.     
    ''')

    mentor_contact = types.Contact(
        phone_number='+7 900 323 6934',
        first_name='Александр',
        last_name='Дружинин',

    )
    await callback_query.message.answer_contact(phone_number=mentor_contact.phone_number,
                                                first_name=mentor_contact.first_name,
                                                last_name=mentor_contact.last_name)

    await callback_query.answer()
