# Petercord User
from time import sleep
from userbot import CMD_HELP, bot
from userbot.events import register
from telethon import events
import asyncio


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(117)

    input_str = event.pattern_match.group(1)

    if input_str == "sad":

        await event.edit(input_str)

        animation_chars = [
            "🥺",
            "😭",
            "🥺",
            "😭",
            "🥺",
            "SENYUM DIKIT 🙃",
            "🙂",
            "☹️",
            "NANGIS LAGI",
            "🥺",
            "😭",
            "🥺",
            "😭",
            "🥺",
            "😭",
            "🥺",
            "😭",
            "🥺",
            "😭",
            "🥺",
            "😭",
            "🥺",
            "😭",
            "🥺",
            "😭",
            "😭",
            "🥺",
            "😭",
            "🥺",
            "😭",
            "🥺",
            f"😭"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 32])


@register(outgoing=True, pattern='^.gaje(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("🥀🥀🥀🥀.◙.🥀🥀🥀🥀 \n"
                     "═🔥🔥🔥▓🔥🔥🔥 \n"
                     "◢👀 🦷🧠🧠🧠🧠🧠🧠💀 \n"
                     " 👄 🙅 🙆👀 💀💀💀💀💀💀💀💀💀╬ \n"
                     "◥💯💯💯💯◤ \n"
                     "══╩══╩══ \n"
                     "👀 \n"
                     "👄 \n"
                     "👀 \n"
                     "💋 \n"
                     "👀 \n"
                     "👅 \n"
                     "👀 Hallo Semuanya :) \n"
                     "👅☻/ \n"
                     "👀/▌ \n"
                     "👅/ \\ \n")


@register(outgoing=True, pattern='^.pikiran(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("PIKIRANKU 🙆\n"
                     "(TAK DAPAT KU MENGERTI 💆\n"
                     "<KAKI DIKEPALA 🤸\n"
                     r"KEPALA DIKAKI🧘"
                     "\n**Mau Jadi Pacarku Gak?!**")


@register(outgoing=True, pattern='^.gitar(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`GITAR GAK JADI 😂...`          \n　　　　　|"
                     "\n　　　🎸　　 \n"
                     "　    '　'　　　 \n"
                     "    　'　'　　　 \n"
                     "　    '　'　　　 \n"
                     " 　   '　'　 \n"
                     "　　　 '　'   \n"
                     "|||||| 　　|||||| \n"
                     "||||||    |||||| \n"
                     "||||||　　 ||||||      | \n"
                     "　|||       |||      \n"
                     "  |||　|||　||| \n"
                     "　GITAR MACAM APA INI) \n"
                     "　　ASTAGFIRULLAH💆　　　 \n")


@register(outgoing=True, pattern='^.senyum(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(".   🙃     ☹️    🙂\n"
                     "──▄▀█▄▄▄─────▄▀█▄▄▄\n"
                     "▄▀──█▄▄──────█─█▄▄\n"
                     "─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n"
                     "─▀───────▀▀─▀───────▀▀\n`SENYUM JALAN LIAT MANTAN..`")




   
})
