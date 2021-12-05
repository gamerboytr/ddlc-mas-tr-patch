init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_discord",
            category=['Discord'],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_discord:
    $ wrs_success = display_notif(
        m_name,
        [
            "Birileriyle mi sohbet ediyorsun, [player]?",
            "Kimlerle konuşuyorsun, [player]?",
            "discord.gg/crackturkey sende aramıza katıl!"
        ],
        'Window Reactions'
    )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_discord')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_gamermunity",
            category=['Gamermunity'],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_gamermunity:
    $ wrs_success = display_notif(
        m_name,
        [
            "GamerboyTR'nin sitesi ha",
            "Seni bu sitede görmek güzel, [player]!"
        ],
        'Window Reactions'
    )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_gamermunity')
    return