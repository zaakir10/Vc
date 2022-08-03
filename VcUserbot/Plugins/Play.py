from pyrogram.raw.types import InputPeerChannel
from pyrogram.raw.functions.phone import CreateGroupCall
from pytgcalls.exceptions import GroupCallNotFound, NoActiveGroupCall
from pyrogram import filters
from Config import PREFIXES
from Client import app
from Core.Decorators import language, register, handle_error
from Core import search, xd, delete_messages, get_group, get_queue, start_stream, set_group



@app.on_message(
    filters.command(["p", "play"], PREFIXES) & ~filters.private & ~filters.edited
)
@register
@language
@handle_error
async def play_stream(_, message: Message, lang):
    chat_id = message.chat.id
    group = get_group(chat_id)
    song = search(message)
    if song is None:
        k = await message.reply_text(lang["notFound"])
        return await delete_messages([message, k])
    ok, status = await song.parse()
    if not ok:
        raise Exception(status)
    if not group["is_playing"]:
        set_group(chat_id, is_playing=True, now_playing=song)
        try:
            await start_stream(song, lang)
        except (NoActiveGroupCall, GroupCallNotFound):
            peer = await app.resolve_peer(chat_id)
            await app.send(
                CreateGroupCall(
                    peer=InputPeerChannel(
                        channel_id=peer.channel_id,
                        access_hash=peer.access_hash,
                    ),
                    random_id=app.rnd_id() // 9000000000,
                )
            )
            await start_stream(song, lang)
        await delete_messages([message])
    else:
        queue = get_queue(chat_id)
        await queue.put(song)
        k = await message.reply_text(
            lang["addedToQueue"] % (song.title, song.yt_url, len(queue)),
            disable_web_page_preview=True,
        )
        await delete_messages([message, k])
