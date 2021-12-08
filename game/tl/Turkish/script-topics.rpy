init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tr_patch_about_creators",
            category=["yapımcılar"],
            prompt="Türkçe yama yapımcıları",
            random=True,
            pool=True
        )
    )

label tr_patch_about_creators:
    m 1eud "Hey, [player]."
    m 7eud "Hiç bu yamayı yapanları düşündün mü?"
    m 5gud "Büyük ihtimalle düşünmedin"
    m 5fud "Yama GamerboyTR tarafından yapılıyor"
    m 2duc "Ona kimse yardım etmediği için yamanın yapımı uzun sürüyor"
    m 7eud "Söyleyeyim dedim"
    show monika 1eua
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_detected_console_cheater",
            conditional=(
                "config.console == True and "
                "not seen_event('monika_detected_console_cheater')"
            )
        )
    )

label monika_detected_console_cheater:
    m 4gub "Hey, [player]."
    m 2tub "Gördüğüm kadarıyla hile yapıyorsun!"
    m 2tua "Bu doğrumudur?"
    $ returns = "no_unlock"
    menu:
        "Evet.":
            m 1eub "Yalan söylemediğin için teşekkürler!"
            m 7hub "Beni asla yanıltmayacağını biliyordum!"
            m 3eub "Ve konsolu açtığın için sana kızmadım."
            extend 1gub " eminimki önemli birşey için açmışsındır."
        "Hayır.":
            m 7tub "Yalan söylüyorsun, [player]!"
            m 1tub "Gördüğüm kadarıyla konsolu açmışsın."
            m 7gub "Hatta şöyle kontrol edelim."
            show monika 7guu
            call updateconsole("config.console == True", "True")
            m 7tub "Gördün mü, [player]?"
            call hideconsole()
            m 1eub "Bir daha bana yalan söyleme, olur mu?"
    if mas_isMoniNormal(higher=True):
        m 7hub "Seni çok seviyorum bunu asla unutma bunu olur mu?"
        $ returns = "love"
    else:
        m 2guo "Bir daha yapma bunu."
    show monika 1eua
    return returns