import os
import textwrap as tw

from aiogram import types, Router
from aiogram.types import FSInputFile, Message, InputMediaPhoto
from aiogram.filters.command import Command
from dotenv import load_dotenv, find_dotenv

from keyboards.keyboards import welcome_yes_no_kb, make_accept_details_kb, make_continue_kb, \
    make_hook_10k_want_later_kb, make_become_partner_kb, make_card_order_kb, make_register_kb, make_common_kb, \
    make_card_order_after_test_kb, make_i_order_card_kb, make_common_continue_kb

from image_files.images_paths import path_to_welcome_img, path_to_advantage_official_income, \
    path_to_advantage_official_income_details, \
    path_to_advantage_income_without_investment, path_to_advantage_cooperation_bank, \
    path_to_advantage_income_without_investment_details, path_to_advantage_cooperation_bank_details, \
    path_to_advantage_unlimited_income, path_to_advantage_unlimited_income_details_1, \
    path_to_advantage_unlimited_income_details_3, path_to_advantage_unlimited_income_details_2, \
    path_to_advantage_unlimited_income_details_4, path_to_advantage_unlimited_income_details_5, \
    path_to_advantage_free_schedule, path_to_advantage_free_schedule_details, path_to_advantage_remote_work, \
    path_to_advantage_remote_work_details, path_to_advantage_free_study_details, path_to_advantage_free_study, \
    path_to_advantage_privilege_details, path_to_advantage_privilege, path_to_advantage_new_profession, \
    path_to_advantage_new_profession_details, path_to_how_to_make_10k_details, path_to_how_to_make_10k, \
    path_to_card_order, path_to_card_order_cashback, path_to_card_order_employee, path_to_become_a_partner, \
    path_to_registration, path_to_answers_test, path_to_cashback_and_sales, path_to_ai_gen_man_1, path_to_ai_gen_man_2, \
    path_to_own_at_alpha

router = Router()
load_dotenv(find_dotenv())
USER = os.environ.get('USER')
CARD_ORDER_LINK = os.environ.get('CARD_ORDER_LINK')


@router.message(Command("start"))
async def cmd_start(message: Message) -> None:
    """
    Функция выводит приветственной сообщение
    """
    photo = FSInputFile(path_to_welcome_img)
    username = message.from_user.first_name
    await message.answer_photo(photo=photo, reply_markup=welcome_yes_no_kb(), caption=f'''
Привет, {username}! Я - {USER}.
Если ты нажал кнопку «старт», значит тебе интересен официальный доход без вложений, мне, кстати, тоже – рассказать?
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

    await callback_query.message.answer(text=tw.dedent('''
    Добро пожаловать в проект «Свой в Альфе»,посмотри на преимущества участия в нашем проекте!
    '''))

    await callback_query.message.answer_photo(photo=photo, reply_markup=next_advantage_kb, caption=tw.dedent('''
Официальный доход. \
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

    await callback_query.message.answer(text=tw.dedent('''
Прости, но я не знаю другого, ведь проект «Свой в Альфе» \
это проект от крупного российского банка, посмотри на его преимущества:
    '''))

    await callback_query.message.answer_photo(photo=photo, reply_markup=next_advantage_kb, caption=tw.dedent('''
Официальный доход. \
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

    await callback_query.message.answer_photo(photo=photo, caption=tw.dedent('''
Ты можешь самостоятельно выбрать форму сотрудничества: Самозанятый. Простая и быстрая регистрация через приложение \
банка, низкие ставки по налогам всего 6% и отсутствие отчетности. Получаешь возможность официально работать \
оплачивая небольшой налог в соответствии с законодательством РФ. Самозанятость, к примеру, не влияет на пенсию. \
Федеральная налоговая служба не считает самозанятых пенсионеров трудоустроенными гражданами. Так пенсионеры могут \
уплачивать налог на профессиональный доход и при этом не рискуют потерять право на доплаты и индексацию пенсионных \
выплат.
    '''))

    await callback_query.message.answer(text=tw.dedent('''
Дает возможность заниматься предпринимательской деятельностью без образования юридического лица. Заплати налоги и \
спи спокойно. Индивидуальный предприниматель. Если вы уже ИП просто предоставьте справку что вы работаете по УСН и \
начинайте сотрудничество с банком. Простая регистрация, быстрый и простой вывод денег. Физическое лицо, вам \
достаточно предоставить паспорт, инн и снилс и ваша форма сотрудничества подтверждена. Обратите внимание по \
физическому лицу необходимо оплатить налог 13% . Можно совмещать разные виды деятельности. Можно работать с 18 лет. \
Сотрудничество с проектом «Свой в Альфе» дает возможность студентам пройти практику и получить свой первый доход.  \
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

    await callback_query.message.answer_photo(photo=photo, reply_markup=next_advantage_kb, caption=tw.dedent('''
Доход без вложений.
Проект «Свой в Альфе» это бизнес-модель, которая дает возможность любому гражданину РФ без первоначального \
капитала начать свой бизнес либо просто создать дополнительный источника дохода без вложений.
    '''))
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'advantage_income_without_investment_details')
async def advantage_income_without_investment_details_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальным описанием преимущества - "Доход без вложений"
    """
    photo = FSInputFile(path_to_advantage_income_without_investment_details)
    continue_kb = make_continue_kb(next_advantage_name='cooperation_bank')

    await callback_query.message.answer_photo(photo=photo, reply_markup=continue_kb, caption=tw.dedent('''
Можно зарабатывать без финансовых вложений и риска потерять деньги, ты приобретаешь финансовую независимость, у тебя \
появляется дело, которое будет по душе и будет приносить не только деньги, но и удовольствие. Не нужны никакие \
вложения кроме души и желания помочь людям.
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

    await callback_query.message.answer_photo(photo=photo, reply_markup=next_advantage_kb, caption=tw.dedent('''
Сотрудничество с крупным российским банком. Проект «Свой в Альфе» это маркетинговый проект от \
крупного российского банка, входящего в топ-3 банков России.
    '''))
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'advantage_cooperation_bank_details')
async def advantage_cooperation_bank_details_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальным описанием преимущества - "Сотрудничество с крупным российским банком"
    """
    photo = FSInputFile(path_to_advantage_cooperation_bank_details)
    continue_kb = make_continue_kb(next_advantage_name='unlimited_income')

    await callback_query.message.answer_photo(photo=photo, caption=tw.dedent('''
Проект "Свой в Альфе" сотрудничает с крупнейшим банком России занимающий 4-ое место по размеру активов: 8,79 \
триллионов рублей и это один из самых надежных банков. Банк победил в главных номинациях премии «Банки.ру» по итогам \
2023 года. Год основания 20 декабря 1990 года. Вошел в топ-3 российских банков с лучшей репутацией.
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

    await callback_query.message.answer_photo(photo=photo, reply_markup=next_advantage_kb, caption=tw.dedent('''
Неограниченный доход. Проект предоставляет возможность получать почти неограниченный доход, что \
сложно достичь просто работая по найму.
    '''))

    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'advantage_unlimited_income_details')
async def advantage_unlimited_income_details_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальным описанием преимущества - "Неограниченный доход"
    """
    photo_group = [path_to_advantage_unlimited_income_details_1, path_to_advantage_unlimited_income_details_2,
                   path_to_advantage_unlimited_income_details_3, path_to_advantage_unlimited_income_details_4,
                   path_to_advantage_unlimited_income_details_5]
    media_group = [InputMediaPhoto(media=types.FSInputFile(path)) for path in photo_group]

    continue_kb = make_continue_kb(next_advantage_name='free_schedule')

    await callback_query.message.answer_media_group(media=media_group)
    await callback_query.message.answer(text=tw.dedent('''
Размер дохода зависит только от тебя и нет «потолка», в среднем от 25 000р. до 2 000 000 руб. и более в месяц в \
зависимости от того сколько времени и сил ты будешь уделять проекту.
\nМожно рассматривать этот доход просто как дополнительный источник средств, а можно перестать работать по найму и \
легко построить свой бизнес в любом возрасте и с любым опытом работы при мощной поддержке опытных наставников.
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

    await callback_query.message.answer_photo(photo=photo, reply_markup=next_advantage_kb, caption=tw.dedent('''
Свободный график. Проектом «Свой в Альфе» ты можешь заниматься по свободному графику, в своем комфортном темпе.
    '''))
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'advantage_free_schedule_details')
async def advantage_free_schedule_details_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальным описанием преимущества - "Свободный график"
    """
    photo = FSInputFile(path_to_advantage_free_schedule_details)
    continue_kb = make_continue_kb(next_advantage_name='remote_work')

    await callback_query.message.answer_photo(caption=tw.dedent('''
Ты сам выбираешь сколько тебе работать, гибкий рабочий график помогает найти баланс между работой семьей и личной \
жизнью. Люди, с таким графиком работы, могут чувствовать себя более счастливыми. На фрилансе тебе всегда хочется \
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

    await callback_query.message.answer_photo(photo=photo, reply_markup=next_advantage_kb, caption=tw.dedent('''
Удаленная работа. Работайте дистанционно прямо из дома, в любом месте где есть интернет.
    '''))
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'advantage_remote_work_details')
async def advantage_remote_work_details_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальным описанием преимущества - "Удаленная работа"
    """
    photo = FSInputFile(path_to_advantage_remote_work_details)
    continue_kb = make_continue_kb(next_advantage_name='free_study')

    await callback_query.message.answer_photo(caption=tw.dedent('''
Свобода места работы и времени:
- не нужно ходить в офис и вставать утром в дикую рань, трястись в автобусе или метро. Ты сам выбираешь, где тебе \
сегодня работать: дома, в кафе или вообще собрать вещи и уехать в другой город. 
- не нужно выпрашивать отпуск и выходные, потому что ты их можешь устроить себе в любой момент: вообще - \
полная свобода действий. 
- работа через интернет позволяет масштабироваться и зарабатывать деньги уютно устроившись на любимом диване.
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

    await callback_query.message.answer_photo(photo=photo, reply_markup=next_advantage_kb, caption=tw.dedent('''
Бесплатное обучение. В рамках проекта «Свой в Альфе» ты попадаешь в команду, где ты можешь пройти профессиональное \
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

    await callback_query.message.answer_photo(caption=tw.dedent('''
Обучающие модули устроены таким образом, что ты быстро изучишь суть проекта и возможности, которые предоставляет \
известный российский банк. Ты можешь обучаться онлайн у наставников-профессионалов, и 24/7 тебе доступна \
тех. поддержка и онлайн обучение в личном кабинете партнера, а также ты можешь обучаться оффлайн посещая презентации, \
круглые столы и форумы с куратором твоего региона.
    '''), reply_markup=continue_kb, photo=photo)

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

    await callback_query.message.answer_photo(photo=photo, reply_markup=next_advantage_kb, caption=tw.dedent('''
Привилегии «Для своих». Возможность получать уникальные привилегии по продуктам, \
которые доступны только для партнеров проекта «Свой в Альфе»
    '''))
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'advantage_privilege_details')
async def advantage_privilege_details_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальным описанием преимущества - "Привилегии для своих"
    """
    photo = FSInputFile(path_to_advantage_privilege_details)
    continue_kb = make_continue_kb(next_advantage_name='new_profession')

    await callback_query.message.answer_photo(caption=tw.dedent('''
- Эксклюзивный кэшбэк для вас и ваших клиентов. Возврат кэшбэка деньгами на карту до 5000 руб. в месяц по обычной \
дебетовой карте. Повышенный кэшбэк по актуальным категориям, приветственный кэшбэк 500 рублей новым клиентам банка. \
Супер-кэшбэк до 100% на барабане и лучший кэшбэк от партнеров. \
- Возможность получать гарантированный кэшбэк на самые популярные категории : «Продукты», «АЗС», «Здоровье», \
«Кафе и рестораны», «Маркетплейсы» \
- Выгодные тарифы и новые продукты; \
- Участие в привилегированном клубе «Для своих»; \
- Премиальная бонусная система по выплатам. Бонус за новых партнеров  до 5000 руб. за каждого партнера. \
Бонусный дуэт за развитие своего партнера до 80 000 руб. за каждого. И бонус за все поколения до 5 000 000 руб. \
- Приглашения на мероприятия с руководителями и VIP клиентами крупного российского банка. \
- Бесплатное участие в рейтинговых поездках в рамках проекта «Свой в Альфе» \
    '''), reply_markup=continue_kb, photo=photo)

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

    await callback_query.message.answer_photo(photo=photo, reply_markup=next_advantage_kb, caption=tw.dedent('''
Новая профессия эксперта по личным финансам. Повысь свою финансовую грамотность и помоги стать более финансово \
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

    await callback_query.message.answer_photo(caption=tw.dedent('''
Освой профессию эксперта и получай от 25 000 руб. в месяц за работу 5 часов в неделю. Стань «своим человеком» в \
банке. \
- Ты разберешься в теме личных финансов. Узнаешь как составить личный финансовый план для себя и своих клиентов; \
- Научишься строить личный бренд эксперта по личным финансам; \
- Сможешь консультировать клиентов; \
- Научишься делать самые выгодные предложения клиентам и работать с их возражениями, узнаешь как обучать свою команду. \
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
Много информации? Считаешь, что потратил время зря? А хочешь я тебе докажу что ты можешь заработать 10 000 руб. \
прямо сейчас?
    '''))
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'hook_10k_want')
async def advantage_how_to_make_10k_info_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с информацией о том "как заработать 10к"
    """
    photo = FSInputFile(path_to_how_to_make_10k_details)
    next_advantage_kb = make_become_partner_kb()

    await callback_query.message.answer_photo(photo=photo, reply_markup=next_advantage_kb, caption=tw.dedent('''
\nКак заработать 10000 р за 1 день? \
\n1. Выдать 6 дебетовых карт новым клиентам банка, можно близким родственникам или друзьям, которые тебя обязательно \
поддержат. За каждого нового клиента тебе начислят 17 баллов (8б - дебетовая карта, 5б - новый клиент, 3б - \
подключение госуслуг к банку, 1б - сделать банк основным для сбп). \
\n2. Важно чтобы твой клиент потратили от 1000 р и более, тогда ему начислят приветственный кэшбэк 500 р, \
а тебе соответствующие баллы. \
\n3. Шесть клиентов x 17 баллов за каждого x 100 руб. (стоимость 1б на старте) = 10200 руб. \
\n4. Никуда ходить не надо, курьеры сами привезут карты твоим клиентам домой. \
\nНажми “стать партнером” и получи возможность заработать 10.000 рублей за 1 день \
    '''))
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'card_order')
async def advantage_card_order_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальной информацией по оформлению карты
    """
    photo = FSInputFile(path_to_card_order)

    await callback_query.message.answer_photo(caption=tw.dedent(f'''
Тогда пока закажи карту и получи 500 руб. \
\n{CARD_ORDER_LINK} \
\nДЛЯ СВОИХ (для всех клиентов, смотри описание выше, преимущество для клиентов и сотрудников сетевых компаний - \
кэшбэк на товарооборот в их компании) \
\nС ЛЮБИМЫМ КЭШБЭКОМ (для новых клиентов, повышенные категории кэшбэка, смотри описание выше) \
Закажи карту, получи 500 руб., тестируй, получай кэшбэк до 5000 руб. в месяц и думай, а когда надумаешь рекомендовать \
эту карту, проверишь все сам, напиши наставнику и он пришлет тебе ссылку на регистрацию в проекте «Свой в Альфе», \
так как только твоя ссылка партнера* даст тебе возможность получать доход с максимальной выгодой \
\n*Предупреждение: ссылка из личного кабинета приложения банка дает возможность только единовременного заработка за \
рекомендацию карт без возможности построить команду и зарабатывать неограниченно, чтобы получать неограниченный \
официальный доход без вложений запроси ссылку только от наставника (от кого узнал о проекте) проекта «Свой в Альфе» 
    '''), photo=photo)

    photo_group = [path_to_card_order_cashback, path_to_card_order_employee]
    media_group = [InputMediaPhoto(media=types.FSInputFile(path)) for path in photo_group]

    await callback_query.message.answer_media_group(media=media_group)

    await callback_query.message.answer(text='''
\nИнструкция, что нужно сделать при получении карты: \
\n1️⃣ Получить пластик (карту); \
\n2️⃣ Установить приложение Альфа-банка; \
\n3️⃣ Выбрать кэшбэк по категориям и покрутить барабан; \
\n4️⃣ Подключить Госуслуги; \
\n5️⃣ Сделать банк основным для переводов (просто будет появляться первым при выборе); \
\n6️⃣ Альфа-чек (смс оповещения 99₽) нужны чтобы быть в курсе всех списаний, можно оставить, чтобы обезопасить себя, \
или отключить; \
\n7️⃣ Услуга бесплатные переводы. Все переводы первые 2 месяца бесплатно, далее бесплатно, при покупках более 10 000 \
руб.в месяц, если меньше, то 149 руб. в месяц. Опцию при желании можно отключить. \
\n8️⃣ При желании подключаем Альфа пэй или отдельно в витрине можно заказать платежный стикер, 490 ₽ в 1-ый год, \
потом бесплатно. \
\n9️⃣ Оплатить любую коммунальную услугу в течение месяца; \
\n🔟 Потратить КАРТОЙ в течение 3-х - 5-ти дней от 1000₽ , чтобы через 5 рабочих дней вернулось 500₽. \
\nВАЖНО: Оплата ЖКХ, мобильной и интернет связи, а также переводы, и оплата по QR коду, НЕ ЯВЛЯЮТСЯ ПОКУПКОЙ и \
приветственный бонус в этом случае не начисляется. \
    ''', reply_markup=make_card_order_kb())

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


@router.callback_query(lambda c: c.data == 'become_partner')
async def advantage_become_partner_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальной информацией о том как стать партнером
    """
    photo = FSInputFile(path_to_become_a_partner)
    keyboard = make_register_kb()

    await callback_query.message.answer_photo(photo=photo, caption=tw.dedent('''
\n1. Зайти в ЛК СВОЙ В АЛЬФА по логину и паролю созданному при регистрации; \
\n2. Нажать кнопку "Витрина" \
\n3. Вы на странице "Рекомендуйте продукты банка" \
\n4. Найти нужный продукт, например ДЕБЕТОВАЯ АЛЬФА КАРТА ДЛЯ СВОИХ; \
\n5. Нажать на РЕКОМЕНДОВАТЬ; \
\n6. Появится окно: "ссылка скопирована" отправьте ее клиенту, нажатать на черную кнопку "ХОРОШО"; \
\n7. Далее идём в ВОТСАП или ТЕЛЕГРАМ; \
\n8. Открываем сообщение клиенту; \
\n9. Вставляем сообщение; \
\n10. Закрываем ПРЕВЬЮ, это предварительный просмотр (если появился нажать на крестик). \
Что такое ПРЕВЬЮ: каждый раз, когда вы отправляете ссылку в соц.сети или мессенджере, она отображается с небольшим \
"превью", обычно это заголовок страницы и одна картинка, при отправлении ссылки клиенту ВАЖНО закрыть превью, \
нажав на крестик, и только потом отправлять клиенту. Если вы не уберете превью, ваш клиент может перейти в банк \
напрямую и вы рискуете недополучить баллы и деньги за проделанную работу; ДОБАВИТЬ КАРТИНКУ С ПРЕВЬЮ И БЕЗ ПРЕВЬЮ \
'''))
    await callback_query.message.answer(reply_markup=keyboard, text=tw.dedent('''
\n11. Отправляем клиенту; \
\n12. Сразу же отправляем ПАМЯТКУ ДЛЯ КЛИЕНТА - ИНСТРУКЦИЮ (что нужно сделать СРАЗУ после получения карты); \
\n13. Ведем клиента, помогаем ему подключить нужные категории кэшбэка, отключить лишнее; \
\n14. Проговариваем клиенту , что ВАЖНО СДЕЛАТЬ ПОКУПКИ от 1000 р в течение 3-х дней , чтобы получить ПРИВЕТСТВЕННЫЙ \
КЭШБЭК 500 руб.; \
\n15. ВАЖНО ! Предупредить клиента, что оплата жкх, оплата интернет и моб связи, оплата кьюаркодом, сбп , \
а также переводы НЕ СЧИТАЮТСЯ ПОКУПКОЙ! \
\nВажно! \
\nДля безопасности! \
\nВсегда генерировать новую ссылку, не пересылать одну и ту же несколько раз! \
    '''))
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'register_complete')
async def advantage_register_complete_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальной информацией о том что делать после реистрации
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
    keyboard = make_card_order_after_test_kb()

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


@router.callback_query(lambda c: c.data == 'card_order_info')
async def advantage_card_order_info_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальной информацией о том как сделать дебетовую карту
    """
    photo_group = [path_to_card_order_cashback, path_to_card_order_employee]
    media_group = [InputMediaPhoto(media=types.FSInputFile(path)) for path in photo_group]

    await callback_query.message.answer_media_group(media=media_group)
    await callback_query.message.answer(text=tw.dedent('''
\nДЕБЕТОВАЯ АЛЬФА КАРТА ДЛЯ СВОИХ
\n- бесплатная всегда, без условий;
\n- кэшбэк до 100% на категорию в барабане Суперкэшбэка, 5% в трех категориях на выбор и 1% на все + партнерский \
кэшбэк до 50%
\n- категория кэшбэка для своих 5%, гарантированный кэшбэк на товарооборот МЛМ компаний, список компаний смотри здесь: \
(подгрузить файл список компаний)
\n- тебе начисляется 500 руб. в течение 5 рабочих дней, после получения карты и проведения транзакций; 
\n- получи цифровую карту - начни пользоваться сервисами до получения пластиковой карты; 
\n- доставка пластиковой карты бесплатная; 
\n- снятие наличных в 25 580 банкоматах; 
\n- банки-партнеры: Газпромбанк, Промсвязьбанк, Россельхозбанк, МКБ, Росбанк, УБРиР;
\n- все платежи бесплатно; 
\n- карта доступна для получения с 14 лет.
        '''))
    await callback_query.message.answer(reply_markup=make_i_order_card_kb(), text=tw.dedent('''
\nЕсли ты никогда не был клиентом Альфа-банка то тебе подойдет ДЕБЕТОВАЯ АЛЬФА КАРТА С ЛЮБИМЫМ КЭШБЭКОМ 
\nДебетовая карта, которая подстраивается под каждого. 
\nТы можешь выбирать любимые категории кэшбэка
\n- получай кэшбэк до 5% на твои любимые категории (полезный, вкусный кэшбэк, модный, автомобильный и молодежный \
кэшбэк целых 3 месяца); 
\n- выбирай дополнительные категории каждый месяц - в приложении или Альфа Онлайн
\n- платежи всегда без комиссии, переводы бесплатные;
\n- бесплатное обслуживание навсегда; 
\n- тебе начисляется 500 руб. в течение 5 рабочих дней, после получения карты и проведения транзакций; 
\n- получи цифровую карту - начни пользоваться сервисами до получения пластиковой карты; 
\n- доставка пластиковой карты бесплатная; 
\n- снятие наличных в 25 580 банкоматах; 
\n- банки-партнеры: Газпромбанк, Промсвязьбанк, Россельхозбанк, МКБ, Росбанк, УБРиР;
\n- карта доступна для получения с 14 лет.
\n\nВажно: в комментарии при заказе карты напиши: Свой в Альфе
            '''))
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'i_order_card')
async def advantage_i_order_card_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальной информацией о том что делать после заказа карты
    """
    photo = FSInputFile(path_to_card_order)
    keyboard = make_common_kb(next_handler_name='how_to_make_50k',
                              current_handler_details_name='i_order_card_details',
                              first_key_text='Как заработать 50.000?',
                              second_key_text='Подробнее')

    await callback_query.message.answer_photo(photo=photo, reply_markup=keyboard, caption=tw.dedent('''
\nИнструкция, что нужно сделать при получении карты: \
\n1️⃣ Получить пластик (карту); \
\n2️⃣ Установить приложение Альфа-банка; \
\n3️⃣ Выбрать кэшбэк по категориям и покрутить барабан; \
\n4️⃣ Подключить Госуслуги; \
\n5️⃣ Сделать банк основным для переводов (просто будет появляться первым при выборе); \
\n6️⃣ Альфа-чек (смс оповещения 99₽) нужны чтобы быть в курсе всех списаний, можно оставить, чтобы обезопасить себя, \
или отключить; \
\n7️⃣ Услуга бесплатные переводы. Все переводы первые 2 месяца бесплатно, далее бесплатно, при покупках более 10 000 \
руб.в месяц, если меньше, то 149 руб. в месяц. Опцию при желании можно отключить. \
\n8️⃣ При желании подключаем Альфа пэй или отдельно в витрине можно заказать платежный стикер, 490 ₽ в 1-ый год, \
потом бесплатно. \
\n9️⃣ Оплатить любую коммунальную услугу в течение месяца; \
\n🔟 Потратить КАРТОЙ в течение 3-х - 5-ти дней от 1000₽ , чтобы через 5 рабочих дней вернулось 500₽. \
        '''))

    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'i_order_card_details')
async def advantage_i_order_card_details_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальной информацией о карте(статистика)
    """
    photo = FSInputFile(path_to_cashback_and_sales)
    keyboard = make_common_continue_kb(next_handler_name='how_to_make_50k', key_text='Как заработать 50.000?')

    await callback_query.message.answer_photo(photo=photo, caption=tw.dedent('''
\nКстати, ты сможешь предлагать не просто карты, а карты крупного российского банка, который входит в топ-5 банков \
России. И вот каковы преимущества продуктов банка: 
\n1. Обслуживание дебетовых карт — всегда бесплатно;
\n2. Возможность делать бесплатные переводы;
\n3. Оплата ЖКХ, штрафов и налогов без комиссии;
\n4. Приветственный кэшбэк 500 руб.; 
\n5. Востребованные категории кэшбэков: продукты, здоровье, АЗС, кафе и рестораны, маркетплейсы, развлечения, ремонт, \
такси и т.д. в среднем 3-5% от трат. До 100% кэшбэка на барабане;
        '''))
    await callback_query.message.answer(reply_markup=keyboard, text='''
\n6. Максимальная сумма кэшбэка 5000 руб. в месяц по дебетовой карте и 15 000 руб. в месяц по премиум карте. \
Возврат кэшбэка деньгами на карту;
\n7. Эксклюзивная категория кэшбэка 5-7% на товарооборот для МЛМ компаний, список компаний с которыми сотрудничает \
банк смотри здесь: ДОБАВИТЬ!!!
\n8. Возможность заказать комбо-карту 2 в 1 дебетовая и кредитная на одном пластике;
\n9. Возможность получить беспроцентную рассрочку на 365 дней по кредитной карте;
\n10. Возможность получать кэшбэк как и по категориям дебетовой карты;
\n11. Доставка карты в удобное место и время;    
    ''')
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'how_to_make_50k')
async def advantage_how_to_make_50k_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальной информацией о карте(статистика)
    """
    photo = FSInputFile(path_to_cashback_and_sales)
    keyboard = make_common_kb(next_handler_name='personal_account',
                              current_handler_details_name='personal_account_details',
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


@router.callback_query(lambda c: c.data == 'personal_account' or c.data == 'personal_account_details')
async def advantage_personal_account_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальной информацией о личном кабинете
    """
    photo = FSInputFile(path_to_ai_gen_man_1)
    keyboard = make_common_kb(next_handler_name='own_at_alpha',
                              current_handler_details_name='mentor_details',
                              first_key_text='Подробнее',
                              second_key_text='Написать наставнику')

    await callback_query.message.answer_photo(photo=photo, reply_markup=keyboard, caption=tw.dedent('''
Зайди в личный кабинет "Свой в Альфа", вкладка обучение, курсы - с чего начать. \
Обязательно пройди обучение онлайн, но если тебе что-то непонятно "напиши наставнику"
        '''))

    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'mentor_details')
async def advantage_mentor_details_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальной информацией о личном наставнике
    """
    photo = FSInputFile(path_to_ai_gen_man_2)

    await callback_query.message.answer_photo(photo=photo, caption=tw.dedent('''
\nЗапишись на индивидуальную консультацию в телеграм: напиши наставнику: "Консультация”
\nИнструкция «Как зарегистрировать клиента»
\n\n1. Зайти в ЛК СВОЙ В АЛЬФА по логину и паролю созданному при регистрации; 
\n2. Нажать кнопку "Витрина"
\n3. Вы на странице "Рекомендуйте продукты банка"
\n4. Найти нужный продукт, например ДЕБЕТОВАЯ АЛЬФА КАРТА ДЛЯ СВОИХ;
\n5. Нажать на РЕКОМЕНДОВАТЬ;
\n6. Появится окно: "ссылка скопирована" отправьте ее клиенту, нажать на черную кнопку "ХОРОШО";
\n7. Далее идём в ВОТСАП или ТЕЛЕГРАМ;
\n8. Открываем сообщение клиенту; 
\n9. Вставляем сообщение;
        '''))

    await callback_query.message.answer(text='''
\n10. Закрываем ПРЕВЬЮ, это предварительный просмотр (если появился нажать на крестик).
\nЧто такое ПРЕВЬЮ: каждый раз, когда вы отправляете ссылку в соц.сети или мессенджере, она отображается с небольшим \
"превью", обычно это заголовок страницы и одна картинка, при отправлении ссылки клиенту ВАЖНО закрыть превью, нажав на \
крестик, и только потом отправлять клиенту. Если вы не уберете превью, ваш клиент может перейти в банк напрямую и вы \
рискуете недополучить баллы и деньги за проделанную работу ; ДОБАВИТЬ КАРТИНКУ С ПРЕВЬЮ И БЕЗ ПРЕВЬЮ. 
\n11. Отправляем клиенту;
\n12. Сразу же отправляем ПАМЯТКУ ДЛЯ КЛИЕНТА - ИНСТРУКЦИЮ (что нужно сделать СРАЗУ после получения карты);
\n13. Ведем клиента, помогаем ему подключить нужные категории кэшбэка, отключить лишнее;
\n14. Проговариваем клиенту , что ВАЖНО СДЕЛАТЬ ПОКУПКИ от 1000 р в течение 3-х дней , чтобы получить ПРИВЕТСТВЕННЫЙ \
КЭШБЭК 500 руб.;
\n15. ВАЖНО ! Предупредить клиента, что оплата жкх, оплата интернет и моб связи, оплата кьюаркодом, сбп , а также \
переводы НЕ СЧИТАЮТСЯ ПОКУПКОЙ!
\nВажно! 
\nДля безопасности!
\nВсегда генерировать новую ссылку, не пересылать одну и ту же несколько раз!    
    ''')

    await callback_query.message.answer(text='''
\nИнструкция «Как зарегистрировать Партнера»
\n\n1.Заходим в партнерский личный кабинет проект "Свой в Альфа";
\n2. Нажимаем на вкладку КОМАНДА;
\n3. Заходим во вкладку и нажимаем черную кнопку "ПРИГЛАСИТЬ АГЕНТА";
\n4. Появляется окно: "ссылка скопирована, отправьте ее агенту", нажать кнопку ХОРОШО;
\n5. Далее идём в Вотсап или ТГ;
\n6. Заходим в сообщение клиента; 
\n7. Вставляем ссылку в сообщение (удерживаем несколько секунд на сообщение , появится окошко ВСТАВИТЬ);
\n8. Закрываем ПРЕВЬЮ, (если появилось, нажимаем на крестик). Что такое ПРЕВЬЮ: каждый раз, когда вы отправляете \
ссылку в соц.сети или мессенджере, она отображается с небольшим "превью", обычно это заголовок страницы и одна \
картинка, при отправлении ссылки клиенту ВАЖНО закрыть превью, нажав на крестик, и только потом отправлять клиенту. \
Если вы не уберете превью, ваш клиент может перейти в банк напрямую и вы рискуете недополучить баллы и деньги за \
проделанную работу ; ДОБАВИТЬ КАРТИНКУ С ПРЕВЬЮ И БЕЗ ПРЕВЬЮ. 
\n9. Отправляем сообщение партнеру;
\n10. Помогаем партнеру пройти регистрацию, объясняем как это сделать;
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
