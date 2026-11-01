from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, GiftEvent, ConnectEvent
from responses import get_comment_reply, get_gift_reply, get_welcome_reply
from gtts import gTTS
import os

# ضع اسم مستخدم حساب تيك توك هنا
client: TikTokLiveClient = TikTokLiveClient(unique_id="@your_tiktok_username")

@client.on("connect")
async def on_connect(event: ConnectEvent):
    print("✅ الشخصية متصلة الآن ببث تيك توك وجاهزة لصنع الجو!")

@client.on("comment")
async def on_comment(event: CommentEvent):
    user = event.user.nickname
    comment = event.comment
    print(f"[{user}]: {comment}")
    
    # اختيار الرد التونسي المناسب
    reply = get_comment_reply(comment)
    print(f"🤖 [7eventy 7 ]: {reply}")
    
    # هنا يمكنك تحويل النص (reply) إلى صوت عبر gTTS أو تشغيله مباشرة
    # tts = gTTS(text=reply, lang='ar')
    # tts.save("reply.mp3")

@client.on("gift")
async def on_gift(event: GiftEvent):
    if event.gift.streakable and not event.gift.repeat_end:
        return
    
    user = event.user.nickname
    gift_name = event.gift.name
    reply = get_gift_reply(gift_name, user)
    print(f"🎁 [تفاعل الهدية]: {reply}")

if __name__ == '__main__':
    client.run()
