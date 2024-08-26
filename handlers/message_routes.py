import os
import textwrap as tw

from aiogram import types, Router
from aiogram.types import FSInputFile, Message, InputMediaPhoto
from aiogram.filters.command import Command
from dotenv import load_dotenv, find_dotenv

from keyboards.keyboards import welcome_yes_no_kb, make_accept_details_kb, make_continue_kb

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
    path_to_card_order, path_to_card_order_cashback, path_to_card_order_employee

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
    next_advantage_kb = make_accept_details_kb(next_advantage_name='how_to_make_10k_info',
                                               current_advantage_details_name='card_order',
                                               first_key_text='Хочу',
                                               second_key_text='Позже')

    await callback_query.message.answer_photo(photo=photo, reply_markup=next_advantage_kb, caption=tw.dedent('''
Много информации? Считаешь, что потратил время зря? А хочешь я тебе докажу что ты можешь заработать 10 000 руб. \
прямо сейчас?
    '''))
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'advantage_card_order_details')
async def advantage_card_order_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с детальной информацией по оформлению карты
    """
    photo = FSInputFile(path_to_card_order)
    # TODO сделать отдельную клавиатуру под этот хендлер
    continue_kb = make_continue_kb(next_advantage_name='NEXT_ADV')

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
    '''), reply_markup=continue_kb, photo=photo)

    photo_group = [path_to_card_order_cashback, path_to_card_order_employee]
    media_group = [InputMediaPhoto(media=types.FSInputFile(path)) for path in photo_group]

    await callback_query.message.answer_media_group(media=media_group)

    await callback_query.message.answer(text='''
    Инструкция, что нужно сделать при получении карты: \
1️⃣ Получить пластик (карту); \
2️⃣ Установить приложение Альфа-банка; \
3️⃣ Выбрать кэшбэк по категориям и покрутить барабан; \
4️⃣ Подключить Госуслуги; \
5️⃣ Сделать банк основным для переводов (просто будет появляться первым при выборе); \
6️⃣ Альфа-чек (смс оповещения 99₽) нужны чтобы быть в курсе всех списаний, можно оставить, чтобы обезопасить себя, \
или отключить; \
7️⃣ Услуга бесплатные переводы. Все переводы первые 2 месяца бесплатно, далее бесплатно, при покупках более 10 000 \
руб.в месяц, если меньше, то 149 руб. в месяц. Опцию при желании можно отключить. \
8️⃣ При желании подключаем Альфа пэй или отдельно в витрине можно заказать платежный стикер, 490 ₽ в 1-ый год, \
потом бесплатно. \
9️⃣ Оплатить любую коммунальную услугу в течение месяца; \
🔟 Потратить КАРТОЙ в течение 3-х - 5-ти дней от 1000₽ , чтобы через 5 рабочих дней вернулось 500₽. \
ВАЖНО: Оплата ЖКХ, мобильной и интернет связи, а также переводы, и оплата по QR коду, НЕ ЯВЛЯЮТСЯ ПОКУПКОЙ и \
приветственный бонус в этом случае не начисляется. \
    ''')

    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'advantage_how_to_make_10k_info_accept' or
                                 c.data == 'advantage_how_to_make_10k_info_continue')
async def advantage_how_to_make_10k_info_handler(callback_query: types.CallbackQuery) -> None:
    """
    Функция выводит пост с информацией о том "как заработать 10к"
    """
    photo = FSInputFile(path_to_how_to_make_10k_details)
    next_advantage_kb = make_accept_details_kb(next_advantage_name='NEXT_ADV',
                                               current_advantage_details_name='card_order',
                                               first_key_text='Хочу',
                                               second_key_text='Позже')

    await callback_query.message.answer_photo(photo=photo, reply_markup=next_advantage_kb, caption=tw.dedent('''
Как заработать 10000 р за 1 день? \
1. Выдать 6 дебетовых карт новым клиентам банка, можно близким родственникам или друзьям, которые тебя обязательно \
поддержат. За каждого нового клиента тебе начислят 17 баллов (8б - дебетовая карта, 5б - новый клиент, 3б - \
подключение госуслуг к банку, 1б - сделать банк основным для сбп). \
2. Важно чтобы твой клиент потратили от 1000 р и более, тогда ему начислят приветственный кэшбэк 500 р, \
а тебе соответствующие баллы. \
3. Шесть клиентов x 17 баллов за каждого x 100 руб. (стоимость 1б на старте) = 10200 руб. \
4. Никуда ходить не надо, курьеры сами привезут карты твоим клиентам домой. \
\nНажми “стать партнером” и получи возможность заработать 10.000 рублей за 1 день \
    '''))
    await callback_query.answer()
