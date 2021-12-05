init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tr_patch_about_creators",
            category=["creators", "topic"],
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
    m 1eua "[wb_quip]"
    return