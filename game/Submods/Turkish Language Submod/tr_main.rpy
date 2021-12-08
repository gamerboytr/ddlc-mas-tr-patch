define config.default_language = "Turkish"
define config.language = "Turkish"

init -990 python hide:
    version = "0.2.0"

    if version.isdecimal():
        name_suffix = ""
        is_unstable = False

    elif "-" in version:
        name_suffix = " Canary Build"
        is_unstable = True
        version_split = version.split('-')
        version_split[2] = str(int(version[-7:], 16))
        version = ".".join(version_split)

    else:
        name_suffix = " In Development"
        is_unstable = True

    tr_submod = store.mas_submod_utils.Submod(
        author = "GamerboyTR",
        name = "Turkish Language Submod" + name_suffix,
        description = (
            "Bu türkçe çeviri için bir submod."
            + (" Bu sürüm kararsız. Mümkünse en son kararlı sürümü kullanın." if is_unstable else "")
        ),
        version = version,
        dependencies={},
        settings_pane="turkish_submod_screen",
    )

init -989 python hide:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Turkish Language Submod",
            user_name="gamerboytr",
            repository_name="ddlc-mas-tr-patch",
            update_dir=""
        )

screen turkish_submod_screen():
    pass

python early hide:
    import os.path
    def create_dummy_if_needs(path):
        if os.path.isfile(path) or os.path.isfile(path + "c"):
            with open(path, "w") as f:
                pass

    create_dummy_if_needs(renpy.config.gamedir + "/tl/Turkish/overrides/definitions.rpy")
    create_dummy_if_needs(renpy.config.gamedir + "/tl/Turkish/overrides/gui.rpy")
    create_dummy_if_needs(renpy.config.gamedir + "/tl/Turkish/overrides/poems.rpy")
    create_dummy_if_needs(renpy.config.gamedir + "/tl/Turkish/overrides/screens.rpy")
    create_dummy_if_needs(renpy.config.gamedir + "/tl/Turkish/overrides/submod.rpy")
    create_dummy_if_needs(renpy.config.gamedir + "/tl/Turkish/overrides/zz_calendar.rpy")

label gamerboytr_turkish_language_submod_v020(version="v0.2.0"):
    python hide:
        def trydel(path):
            import shutil
            try:
                shutil.rmtree(path)
            except Exception as e:
                pass

        trydel(renpy.config.gamedir + "/tl/Turkish/dev")
        trydel(renpy.config.gamedir + "/tl/Turkish/overrides")
    return