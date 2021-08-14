import os

TG_TOKEN = os.getenv("TG_TOKEN")

button_text_calendar = "Календарь смены"
button_text_songs = "Песенник"
button_text_employees = "Комиссары смены"

# Cписок сотрудников лагеря по отрядам и службы
# Тут нужно проработать для каждого отряда Фамилия и Имя комиссаров и id_photo для каждого из них (фотки взять из их вк)
employees_list = [
    {
        'group_name': 'Отряд 1',
        'place': 'Беседка около 1 Корпуса',
        'employees' : [
            {
                'name': 'Бухер Сергей',
                'image_id': 'AgACAgIAAxkBAAICAAFhF6g-tQda0R7B4LJQJWdvYcj50QAChbUxG_37uUi3H1duXz6FQgEAAwIAA3MAAyAE'
            },
            {
                'name': 'Бондарева Ирина',
                'image_id': 'AgACAgIAAxkBAANOYRQ4d0TyXTLfuE7-1mwb2EYKVzwAApy2MRtCkKFItutOgufAXgkBAAMCAANzAAMgBA'
            }
        ]
    },
    {
        'group_name': 'Отряд 2',
        'place': 'Беседка около 1 Корпуса',
        'employees' : [
            {
                'name':'Цыцаров Денис',
                'image_id': 'AgACAgIAAxkBAANQYRQ52ff23jAHSIaIeo2bGLdTIf4AAp-2MRtCkKFIVDnjoiXvwXUBAAMCAANzAAMgBA'
            },
            {
                'name': 'Козырькова Дина',
                'image_id': 'AgACAgIAAxkBAANSYRQ5-xolXIWxTk-nnH8EdYqxiykAAqC2MRtCkKFII7dtIiHpwTcBAAMCAANzAAMgBA'
            }
        ]
    },
    {
        'group_name': 'Отряд 3',
        'place': 'Беседка около 1 Корпуса',
        'employees': [
            {
                'name': 'Назимов Дмитрий',
                'image_id': 'AgACAgIAAxkBAANUYRQ-8AMXblJ8WbG7uQXyDbRe244AAqG2MRtCkKFIWRbq612oNYABAAMCAANzAAMgBA'
            },
            {
                'name': 'Давыдова Мария',
                'image_id': 'AgACAgIAAxkBAANWYRQ_bTppuQpF_GfAwwoHDWP_v1kAAqK2MRtCkKFIfMUscvZ9RvoBAAMCAANzAAMgBA'
            }
        ]
    },
    {
        'group_name': 'Отряд 4',
        'place': 'Беседка около 1 Корпуса',
        'employees': [
            {
                'name': 'Кушнир Артём',
                'image_id': 'AgACAgIAAxkBAANaYRRARgogQ5zaMzd01fd59i4nT0sAAqW2MRtCkKFIntSLbZERFUUBAAMCAANzAAMgBA'
            },
            {
                'name': 'Харлина Анастасия',
                'image_id': 'AgACAgIAAxkBAANYYRQ_6qr9MEBSOXBcsCRu74CFr1kAAqO2MRtCkKFIRQHuGz2hfJsBAAMCAANzAAMgBA'
            }
        ]
    },
    {
        'group_name': 'Отряд 5',
        'place': 'Беседка около 1 Корпуса',
        'employees': [
            {
                'name': 'Старченков Кирилл',
                'image_id': 'AgACAgIAAxkBAANeYRRDeQ_PqVLdaU1CXCtVxfzNUXcAAqi2MRtCkKFIIz-a5BsZMmUBAAMCAANzAAMgBA'
            },
            {
                'name': 'Сафонова Дарья',
                'image_id': 'AgACAgIAAxkBAANcYRRDW55yIOiptj3qcFwzU7pZCgYAAqe2MRtCkKFIDJHHd0goMNQBAAMCAANzAAMgBA'
            }
        ]
    },
    {
        'group_name': 'Отряд 6',
        'place': 'Беседка около 1 Корпуса',
        'employees': [
            {
                'name': 'Конон Артем',
                'image_id': 'AgACAgIAAxkBAANiYRRFW6jZihb0eZmyBk_AlXPCWYcAAqq2MRtCkKFI8ouuP04W3IQBAAMCAANzAAMgBA'
            },
            {
                'name': 'Филоненко Елизавета',
                'image_id': 'AgACAgIAAxkBAANgYRRFL4mLht868O6lQARMuiXVZZ0AAqm2MRtCkKFIZ3p-bHmnUycBAAMCAANzAAMgBA'
            }
        ]
    },
    {
        'group_name': 'Отряд 7',
        'place': 'Беседка около 1 Корпуса',
        'employees': [
            {
                'name': 'Ваньков Дарви',
                'image_id': 'AgACAgIAAxkBAANmYRRHyinARbby9A_qMflNRJkSuk0AAq62MRtCkKFIi0RQIbxClKcBAAMCAANzAAMgBA'
            },
            {
                'name': 'Шацкова Валерия',
                'image_id': 'AgACAgIAAxkBAANkYRRHpOdM20mUmNXv0MI6Dijg1e8AAq22MRtCkKFIEbNRi9a6mzABAAMCAANzAAMgBA'
            }
        ]
    },
    {
        'group_name': 'Отряд 8',
        'place': 'Беседка около 1 Корпуса',
        'employees': [
            {
                'name': 'Ерохин Валера',
                'image_id': 'AgACAgIAAxkBAANqYRRJopVCod3GI0ZZMelYovqc6LUAArC2MRtCkKFIKEcR1ZYkK-MBAAMCAANzAAMgBA'
            },
            {
                'name': 'Фомина Екатерина',
                'image_id': 'AgACAgIAAxkBAAIBQmEWqjGV23dvMjVGT6eXG9xNxMWqAALitTEb_fuxSF8V1hDG8p0sAQADAgADcwADIAQ'
            }
        ]
    },
    {
        'group_name': 'Медиацентр',
        'place': 'Беседка около 1 Корпуса',
        'employees': [
            {
                'name': 'Черняева Екатерина',
                'image_id': 'AgACAgIAAxkBAANsYRRMMQRyh015nIGRuu7JDE9fSvwAArO2MRtCkKFIsrJQsj4ZhJIBAAMCAANzAAMgBA'
            },
            {
                'name': 'Афонина Арина',
                'image_id': 'AgACAgIAAxkBAANuYRRNc7ucg6sKzoWbfIk7x461lU0AArS2MRtCkKFI9C2XXt180HgBAAMCAANzAAMgBA'
            },
            {
                'name': 'Косухина Мария',
                'image_id': 'AgACAgIAAxkBAANwYRRNlfKyGYNF8nTNmBEL6UovIX0AArW2MRtCkKFILmlj7FHyiG8BAAMCAANzAAMgBA'
            },
            {
                'name': 'Шмелева Анастасия',
                'image_id': 'AgACAgIAAxkBAANyYRRN_d-tGQfHsP3P4CiSiXHheZkAAre2MRtCkKFIKz118tNlgpoBAAMCAANzAAMgBA'
            },
            {
                'name': 'Романова Елизавета',
                'image_id': 'AgACAgIAAxkBAAN0YRROFY9PCj0qa-xknhYUWLI396IAAri2MRtCkKFIK9GMIYwipSABAAMCAANzAAMgBA'
            }
        ]
    },
    {
        'group_name': 'Служба \"Рассвет\"',
        'place': 'Беседка около 1 Корпуса',
        'employees': [
            {
                'name': 'Варсеев Тимофей',
                'image_id': 'AgACAgIAAxkBAAN2YRRTw1avidrA9semx1NL20hFixsAArm2MRtCkKFIOF-LNeNqScwBAAMCAANzAAMgBA'
            },
            {
                'name': 'Чучина Анастасия',
                'image_id': 'AgACAgIAAxkBAAN4YRRT6MbQX3NG-YG8KQtVhl0YNuoAArq2MRtCkKFICIlE7guA7VUBAAMCAANzAAMgBA'
            },
            {
                'name': 'Рогова Марина',
                'image_id': 'AgACAgIAAxkBAAN6YRRUC_IUV28ZPxosKWxahPUd_TIAAru2MRtCkKFIXjsveV06b9cBAAMCAANzAAMgBA'
            }
        ]
    },
    {
        'group_name': 'Тех-служба',
        'place': 'Беседка',
        'employees': [
            {
                'name': 'Толоконов Илья',
                'image_id': 'AgACAgIAAxkBAAN8YRRUzKnUoicLExCR-bnO65tFaPUAAry2MRtCkKFIS2_w7wnNYG8BAAMCAANzAAMgBA'
            },
            {
                'name': 'Конаков Павел',
                'image_id': 'AgACAgIAAxkBAAOAYRRVA959qZZWDoK7c-BSBb5vEB8AAr62MRtCkKFIH5SF6UXnnzkBAAMCAANzAAMgBA'
            },
            {
                'name': 'Близнов Матвей',
                'image_id': 'AgACAgIAAxkBAAOCYRRVHhX0jZL0N2tqFIWtX9-UdxUAAr-2MRtCkKFIn0_BbgFkiu4BAAMCAANzAAMgBA'
            },
            {
                'name': 'Рюмин Кирилл',
                'image_id': 'AgACAgIAAxkBAAIB_mEXpknVfsQ0mLhk90SS4koGlq-CAAKAtTEb_fu5SPh3ymYFvLOOAQADAgADcwADIAQ'
            }
        ]
    },
]

# Здесь должен быть id фотки с календарём (прокидываешь через бота фотку и пишешь id сюда
CALENDAR_FILE_ID = 'AgACAgIAAxkBAAIB-GEXpFrXjxa20TVe9Tws9bTCZewxAAJytTEb_fu5SCK_83ZsS2ZIAQADAgADcwADIAQ'


# Здесь у нас словарь с file_id текстовых файлов песен
song_file_ids = {
    '00': 'BQACAgIAAxkBAAIBRGEWqsaKEMUILO0sEiuo1C_owoPdAAIVEQAC_fuxSHwpMVyFfE3nIAQ',
    '01': 'BQACAgIAAxkBAAIBRmEWquXAEc4pBy_DCZ6cHT5nuUmKAAIWEQAC_fuxSPkxGyHfZIbOIAQ',
    '02': 'BQACAgIAAxkBAAIBXmEWrTvO3yRMEqUPeUbug_glf3X7AAIkEQAC_fuxSP_2xwjmxXFnIAQ',
    '03': 'BQACAgIAAxkBAAIBSmEWrGU6FYZwil_0FeXhBpQ8cPlRAAIdEQAC_fuxSEfKmNM2Fsl_IAQ',
    '04': 'BQACAgIAAxkBAAIBTGEWrGmKXm4KhB2wgA1RxEr7OzAQAAIeEQAC_fuxSGwzopG1ozaNIAQ',
    '05': 'BQACAgIAAxkBAAIBTmEWrGzIXc34vEcShqM9Adj24FZnAAIfEQAC_fuxSNNrub1c4db0IAQ',
    '10': 'BQACAgIAAxkBAAIBYGEWsSaZkurWSbL2XF7tqRaIRJqtAAI0EQAC_fuxSGCCPrHXEiGpIAQ',
    '11': 'BQACAgIAAxkBAAIBYmEWsS18CczVl4Xyf5FzmShtT5wiAAI1EQAC_fuxSFDcTk01IBpXIAQ',
    '12': 'BQACAgIAAxkBAAIBZGEWsTBVVgUpl1dQBwIbVR7iEdR-AAI2EQAC_fuxSGr7pj0Ci9KSIAQ',
    '13': 'BQACAgIAAxkBAAIBeGEWuDqUQQFOqCWaYxKJ4C3WXCn_AAJfEQAC_fuxSDJp8F1hKifWIAQ',
    '14': 'BQACAgIAAxkBAAIBemEWuJeWncgiU4tVj09dhTpvU_vtAAJjEQAC_fuxSCSpJt22iliSIAQ',
    '15': 'BQACAgIAAxkBAAIBamEWsTufM4qoSfPruKSlcTwj05EBAAI5EQAC_fuxSKA7gaMrwU0rIAQ',
    '20': 'BQACAgIAAxkBAAIBfGEWuNnjYSfeCxOL0RabgqoznGHuAAJoEQAC_fuxSNN6m8xKvef2IAQ',
    '21': 'BQACAgIAAxkBAAIBfmEWuOBQG3RnnEd0PDiIxi_Z8rruAAJpEQAC_fuxSBGb2ht2pS7yIAQ',
    '22': 'BQACAgIAAxkBAAIBgGEWuOd1Zx5p1rwCoyvPD--ivK7AAAJqEQAC_fuxSOm9rzl4aPdMIAQ',
    '23': 'BQACAgIAAxkBAAIBgmEWuO2WHVhM8X-koz0WNcFjREZTAAJsEQAC_fuxSPdX5TgE2ksmIAQ',
    '24': 'BQACAgIAAxkBAAIBhGEWuPQ9LVN-bwG7cOM51M6W2bg-AAJtEQAC_fuxSE-lxcG9Xf1kIAQ',
    '25': 'BQACAgIAAxkBAAIBhmEWuPpGWY1hCpAAARu6zr_EZSJmggACbhEAAv37sUjtepYo2Y-qeSAE',
    '30':'BQACAgIAAxkBAAIBkmEWugLFr1_nTehfhff9rP2TcFBaAAJ7EQAC_fuxSCMf0Qu-vKHEIAQ',
    '31':'BQACAgIAAxkBAAIBlGEWugo_MtYF7edJodEcHMQB73gLAAJ9EQAC_fuxSCv8VzKP9ahXIAQ',
    '32':'BQACAgIAAxkBAAIBlmEWug7JVBso78LempfMkN__Vn3EAAJ-EQAC_fuxSFCZghhMjWjdIAQ',
    '33':'BQACAgIAAxkBAAIBmGEWuhN85MZTccSfXoP0MDqjhrRjAAKAEQAC_fuxSDkrgkVcISpWIAQ',
    '34':'BQACAgIAAxkBAAIBmmEWuhlSjHOqqjxioYgAAd0CyUDNdQACgREAAv37sUibpd7-PJyulyAE',
    '35':'BQACAgIAAxkBAAIBnGEWuhw5ZtA7hw5dZH8q2h2HCRz2AAKCEQAC_fuxSN7oUzwfq32aIAQ',
    '40':'BQACAgIAAxkBAAIBqGEWv5sFetdYCuqLM7WDKl5WxicyAAKYEQAC_fuxSJZfT52LsW-AIAQ',
    '41':'BQACAgIAAxkBAAIBqmEWv5798_dtE0tMw5-ym9eZ7HcBAAKZEQAC_fuxSOawKSH3IAZuIAQ',
    '42':'BQACAgIAAxkBAAIBrGEWv6X7Ghfcy6evFiDmV051A2rQAAKaEQAC_fuxSL0rIdzjwrOUIAQ',
    '43':'BQACAgIAAxkBAAIBrmEWv6cq8C2yiCNzJnttl-4bzyYgAAKbEQAC_fuxSMv2vHLWYmC3IAQ',
    '44':'BQACAgIAAxkBAAIBsGEWv60861V0qS5j9NeqaIWAE3qdAAKcEQAC_fuxSC-Jz6tA1pkxIAQ',
    '45':'BQACAgIAAxkBAAIBsmEWv7bOwwhgCWF5jPPzrvYfsse7AAKdEQAC_fuxSFcMvVRtHpE_IAQ',
    '50':'BQACAgIAAxkBAAIBtmEWwBzvv4YWM0rqdSgv4Qu2tJ18AAKeEQAC_fuxSLkxron0blYRIAQ',
    '51':'BQACAgIAAxkBAAIBuGEWwCCtjSPlGO3mDF9AJOx6NElaAAKfEQAC_fuxSMFM36kdvlAVIAQ',
    '52':'BQACAgIAAxkBAAIBumEWwCbfnOmODoK99FMTN3HMbJBPAAKgEQAC_fuxSF2b-8i3XYTiIAQ',
    '53':'BQACAgIAAxkBAAIBvGEWwCqmSr9hGB-dtzbTAkHzFTHnAAKhEQAC_fuxSA6c76JHYL5zIAQ',
    '54':'BQACAgIAAxkBAAIBvmEWwC4WVy4c0Uw-stPT1fMoeEU1AAKiEQAC_fuxSJBKjhYHQuGWIAQ',
    '55':'BQACAgIAAxkBAAIBwGEWwDTlf5dq7nIBDIqPwMR9E1yAAAKjEQAC_fuxSK98uRYH1w-7IAQ',
    '60':'BQACAgIAAxkBAAIBxGEWwIrljXmdCa2eEMsQtEQ_Jw_PAAKkEQAC_fuxSOQgUOUVUpZlIAQ',
    '61':'BQACAgIAAxkBAAIBxmEWwI8qh2mnbiM-sjSbIQ2sgLM8AAKlEQAC_fuxSLM0qdX8ESN-IAQ',
    '62':'BQACAgIAAxkBAAIByGEWwJNg8I3R9d9QnjM0UX9BfVf3AAJVEAACDUm4SGJrX7jxCLI1IAQ',
    '63':'BQACAgIAAxkBAAIBymEWwJkVUwO-I5iirzmnTtf0JmEXAAKmEQAC_fuxSCYQzcHk27hZIAQ',
    '64':'BQACAgIAAxkBAAIBzGEWwJ3Jp80juEU8Gbp0xq7F3d2nAAKnEQAC_fuxSKeJs7BGnHuEIAQ',
    '65':'BQACAgIAAxkBAAIBzmEWwKbJc723iCBQyEzR2wSDjpcZAAKoEQAC_fuxSLkmWvvM92QNIAQ',
    '70':'BQACAgIAAxkBAAIB0mEWwPhfIgaULxYPWfaOyqs-lboUAAKpEQAC_fuxSEoRMdSM4HI-IAQ',
    '71':'BQACAgIAAxkBAAIB1GEWwPskGYzXf0WaoWI8SOWyBXVsAAKqEQAC_fuxSBg_tzQ3mS3rIAQ',
    '72':'BQACAgIAAxkBAAIB1mEWwQHqmelx-ISebPXziSRck1U4AAKsEQAC_fuxSKRuyk46mk1JIAQ',
    '73':'BQACAgIAAxkBAAIB2GEWwQVzZ0sEN54P8Ogj-jiGrYjSAAKtEQAC_fuxSAKbOSqk9drDIAQ',
    '74':'BQACAgIAAxkBAAIB2mEWwQmX10V5c_RGAAElEK6PKvrXawACrhEAAv37sUicy2FxHqNi3SAE'
}

song_names = [
    [
        "Гимн Российской Федерации",
        "Гимн Рубина",
        "Утренняя",
        "Вечерняя",
        "Надежда",
        "Юбилейная"
    ],
    [
        "Арт-парад",
        "Алые паруса",
        "Вахтерам",
        "Весна",
        "Весенняя",
        "В платье белом"
    ],
    [
        "Город-сказка",
        "Губы-вишни",
        "Дом",
        "Дыхание",
        "Евпатория",
        "Звезды"
    ],
    [
        "Золотка",
        "Изгиб гитары желкой",
        "Капитал",
        "Ключ",
        "Кораблик детства",
        "Любовь, конечно, победит"
    ],
    [
        "Метель",
        "Мой рок-н-ролл",
        "Мое сердце",
        "Милая моя",
        "Мы с тобой",
        "Нафиг нам"
    ],
    [
        "Непогода",
        "Ну, пожалуйста",
        "Ой-йо",
        "Парапет",
        "Перевал",
        "Половинка"
    ],
    [
        "Распустила",
        "Расстояния",
        "Разноцветная Москва",
        "Рыжая",
        "Серебро",
        "Солдат"
    ],
    [
        "Ты, да я, да мы с тобой",
        "Яхта, парус",
        "Я готов целовать песок",
        "Я верю",
        "Прощальная",
    ]
]
