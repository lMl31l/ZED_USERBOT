# commands for source ZED by ~ @zlzzl77


import random
from ..tosh import Cmds
from telethon import events

@bot.on(admin_cmd(pattern="الاوامر"))
@bot.on(sudo_cmd(pattern="الاوامر", allow_sudo=True))
async def cmds(zed):
    await eor(zed, Cmds)

########################  SOURCE ZED ~ BY: ZelZal (@ZedThon)  ########################


import random

from telethon import events

@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م1":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 [𝑺𝑶𝑼𝑹𝑪𝑬 𝙕𝞝𝘿𝙏𝙃𝙊𝙉 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/ZedThon) 𓆪\n **⌔∮ قائـمه اوامر الادمن :** \n⪼ `.حظر` \n⪼ `.الغاء حظر` \n⪼ `.تقيد` \n⪼ `.الغاء تقيد` \n⪼ `.رفع القيود` \n⪼ `.كتم` \n⪼ `.الغاء كتم` \n⪼ `.تثبيت` \n⪼ `.الغاء التثبيت` \n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿𝙏𝙃𝙊𝙉](t.me/ZedThon) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 [𝑺𝑶𝑼𝑹𝑪𝑬 𝙕𝞝𝘿𝙏𝙃𝙊𝙉 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/ZedThon) 𓆪\n **⌔∮ قائـمه اوامر الادمن :** \n⪼ `.حظر` \n⪼ `.الغاء حظر` \n⪼ `.تقيد` \n⪼ `.الغاء تقيد` \n⪼ `.رفع القيود` \n⪼ `.كتم` \n⪼ `.الغاء كتم` \n⪼ `.تثبيت` \n⪼ `.الغاء التثبيت` \n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿𝙏𝙃𝙊𝙉](t.me/ZedThon) 𓆪"
            )

########################  SOURCE ZED ~ BY: ZelZal (@ZedThon)  ########################


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م2":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 [𝑺𝑶𝑼𝑹𝑪𝑬 𝙕𝞝𝘿𝙏𝙃𝙊𝙉 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/ZedThon) 𓆪\n **⌔∮ قائـمه اوامر التسليه :** \n\n⪼ `.شرح تسليه` \n⪼ `.شرح تسليه1` \n⪼ `.شرح تسليه2` \n⪼ `.شرح تسليه3` \n⪼ `.شرح تسليه4` \n⪼ `.شرح تسليه5` \n⪼ `.شرح تسليه7` \n⪼ `.شرح تسليه8` \n\n\n**⌔∮ قائـمه اوامر التسليه الجديده حقـوق سـورس زد ثــون :**\n\n⪼ `.كشف` \nبالـرد / المعرف/ الايدي \n**امـر تسـليه كشـف حيـوان 😂🐴**\n\n⪼ `.مشهور`\n بالـرد /المعرف /الايدي\n**امـر تسـليه زوجنـي من مشهـور 👨‍⚖💍** \n\n⪼ `.مشهوره`\n بالرد /المعرف /الايدي \n **امـر تسـليه زوجنـي من مشهـوره 👰🏻‍♀💍**\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿𝙏𝙃𝙊𝙉](t.me/ZedThon) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 [𝑺𝑶𝑼𝑹𝑪𝑬 𝙕𝞝𝘿𝙏𝙃𝙊𝙉 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/ZedThon) 𓆪\n **⌔∮ قائـمه اوامر التسليه :** \n\n⪼ `.شرح تسليه` \n⪼ `.شرح تسليه1` \n⪼ `.شرح تسليه2` \n⪼ `.شرح تسليه3` \n⪼ `.شرح تسليه4` \n⪼ `.شرح تسليه5` \n⪼ `.شرح تسليه7` \n⪼ `.شرح تسليه8` \n\n\n**⌔∮ قائـمه اوامر التسليه الجديده حقـوق سـورس زد ثــون :**\n\n⪼ `.كشف` \nبالـرد / المعرف/ الايدي \n**امـر تسـليه كشـف حيـوان 😂🐴**\n\n⪼ `.مشهور`\n بالـرد /المعرف /الايدي\n**امـر تسـليه زوجنـي من مشهـور 👨‍⚖💍** \n\n⪼ `.مشهوره`\n بالرد /المعرف /الايدي \n **امـر تسـليه زوجنـي من مشهـوره 👰🏻‍♀💍**\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿𝙏𝙃𝙊𝙉](t.me/ZedThon) 𓆪"
            )

########################  SOURCE 𝙕𝞝𝘿𝙏𝙃𝙊𝙉 ~ BY: ZelZal (@ZedThon)  ########################


import random

from telethon import events

@bot.on(sudo_cmd(pattern="م3", allow_sudo=True))
async def _(zed):
    await eor(zed, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/ZedThon) 𓆪\n **⌔∮ قائـمه اوامر الترحيب :** \n⪼ `.ترحيب ` \n⪼ `.حذف ترحيب ` \n⪼ `.الترحيب `\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪")

########################  SOURCE 𝙕𝞝𝘿𝙏𝙃𝙊𝙉 ~ BY: ZelZal (@ZedThon)  ########################


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م3":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 [𝑺𝑶𝑼𝑹𝑪𝑬 𝙕𝞝𝘿𝙏𝙃𝙊𝙉 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/ZedThon) 𓆪\n **⌔∮ قائـمه اوامر الترحيب :** \n⪼ `.ترحيب ` \n⪼ `.حذف ترحيب ` \n⪼ `.الترحيب `\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿𝙏𝙃𝙊𝙉](t.me/ZedThon) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 [𝑺𝑶𝑼𝑹𝑪𝑬 𝙕𝞝𝘿𝙏𝙃𝙊𝙉 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/ZedThon) 𓆪\n **⌔∮ قائـمه اوامر الترحيب :** \n⪼ `.ترحيب ` \n⪼ `.حذف ترحيب ` \n⪼ `.الترحيب `\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿𝙏𝙃𝙊𝙉](t.me/ZedThon) 𓆪"
            )

########################  SOURCE 𝙕𝞝𝘿𝙏𝙃𝙊𝙉 ~ BY: ZelZal (@ZedThon)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م4"))
@bot.on(sudo_cmd("م4", allow_sudo=True))
async def _(zed):
    await eor(zed, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/ZedThon) 𓆪\n **⌔∮ قائـمه اوامر الردود :** \n⪼ `.اضف رد ` الامر ثم اسم الرد بالرد ع كلمة الرد \n⪼ `.حذف رد ` \n⪼ `.حذف الردود `\n⪼ `.الردود `\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪")

########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م5"))
@bot.on(sudo_cmd("م5", allow_sudo=True))
async def _(zed):
    await eor(zed, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/ZedThon) 𓆪\n **⌔∮ قائـمه اوامر الرفع :** \n⪼ `.رفع مطي ` \n⪼ `.رفع جلب ` \n⪼ `.رفع بكلبي `\n⪼ `.رفع مرتي ` \n⪼ `.رفع تاج ` \n⪼ `.رفع جريذي `\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪")

########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م6"))
@bot.on(sudo_cmd("م6", allow_sudo=True))
async def _(zed):
    await eor(zed, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/ZedThon) 𓆪\n **⌔∮ قائـمه اوامر الحمايه قفل/فتح :** \n⪼ `.الكل ` \n⪼ `.الدردشه ` \n⪼ `.الوسائط `\n⪼ `.الملصقات ` \n⪼ `.المتحركه ` \n⪼ `.الاضافه `\n⪼ `.الاونلاين `\n⪼ `.الماركدون `\n⪼ `.الالعاب `\n⪼ `.التثبيت `\n⪼ `.المعلومات `\n⪼ `.الاعدادات ` لرؤية الاعدادات\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪")

########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م7"))
@bot.on(sudo_cmd("م7", allow_sudo=True))
async def _(zed):
    await eor(zed, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/ZedThon) 𓆪\n **⌔∮ قائـمه اوامر التلكراف :** \n⪼ `.تلكراف ميديا ` \n⪼ `.تلكراف نص ` \n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪")

########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م8"))
@bot.on(sudo_cmd("م8", allow_sudo=True))
async def _(zed):
    await eor(zed, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/ZedThon) 𓆪\n **⌔∮ قائـمه اوامر الملصقات :** \n⪼ `.ملصق ` \n⪼ `.معلومات الملصق ` \n⪼ `.حزمه ` \n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪")

########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م9"))
@bot.on(sudo_cmd("م9", allow_sudo=True))
async def _(zed):
    await eor(zed, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/ZedThon) 𓆪\n **⌔∮ قائـمه اوامر التاك :** \n⪼ `.تاك ` \n⪼ `.للكل ` + الكلام \n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪")

########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م10"))
@bot.on(sudo_cmd("م10", allow_sudo=True))
async def _(zed):
    await eor(zed, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/ZedThon) 𓆪\n **⌔∮ قائـمه اوامر الكشف :** \n⪼ `.الايدي ` \n⪼ `.ايدي ` \n⪼ `.رابط الحساب ` \n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪")

########### for SOURCE ZED by ~ @ZlZZl77 ###########


import random

from telethon import events

@bot.on(admin_cmd("م11"))
@bot.on(sudo_cmd("م11", allow_sudo=True))
async def _(zed):
    await eor(zed, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/ZedThon) 𓆪\n **⌔∮ قائـمه اوامر المجموعه :** \n⪼ `.المجموعه ` \n⪼ `.رفع مشرف ` \n⪼ `.رفع مالك ` \n⪼ `.تك ` \n⪼ `.الاحصائيات ` \n⪼ `.تنظيف الحسابات ` \n⪼ `.الاعضاء ` \n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪")

########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م12"))
@bot.on(sudo_cmd("م12", allow_sudo=True))
async def _(zed):
    await eor(zed, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/ZedThon) 𓆪\n **⌔∮ قائـمه اوامر الترجـمه :**\n\n `.ترجمه ar`  بالرد على الرسالـه\n**•❒ ترجمـة النص المـحدد من أي لغـه الى اللغـه العربيـه**\n\n `.ترجمه en`  بالرد على الرسالـه\n**•❒ ترجمـة النص المـحدد من أي لغـه الى اللغـه الانجليزيـه**\n\n `.صوت كوكل en/ar`  بالرد على الرسالـه\n**•❒ ترجمـة النص المـحدد الى جمله صوتيـه**\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪")

########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م13"))
@bot.on(sudo_cmd("م13", allow_sudo=True))
async def _(zed):
    await eor(zed, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/ZedThon) 𓆪\n **⌔∮ قائـمه اوامر البحث :** \n\n**❶ يـوتيـوب :**\n\n `.اغنيه` + اسـم\n**•❒ لتحميل الاغانـي من يوتيوب بدقـه عاليـه 360**\n `.فيديو` + اسـم\n**•❒ لتحميل مقاطـع الفيديـو من يوتيوب**\n `.يوتيوب` + كلمـه\n**•❒ للبحث عن روابـط بالكلـمه المعطـاه على يوتيوب**\n `.تحميل ف` + رابـط\n**•❒ لتحميل مقاطـع الفيديو من اليوتيوب عن طريق الرابـط**\n `.تحميل ص` + رابـط\n**•❒ لتحميل مقاطـع الصوت من يوتيوب عن طريق الرابـط**\n\n\n**❷ انستجـرام :**\n\n `.انستا` + رابـط\n**•❒ للتحميل من الانستكرام**\n\n\n**❸ تيـك تـوك :**\n\n `.تيكتوك` بالـرد علـى رابـط\n**•❒ لتحميل مقاطـع الفيديـو من تيـك تـوك**\n\n\n**❹ فيس بـوك :** \n\n`.فيسبوك` + رابط\n**•❒ لتحميل الفيديو من فيس بوك**\n`.فيس` بالرد ع الرابط\n**•❒ لتحميل الفيديو من فيس بوك بالـرد ع الرابـط**\n\n\n**❺ تـويتـر :** \n\n`.تويتر` + رابط\n**•❒ لتحميل الفيديو من تويتـر**\n`.تويت` بالرد ع الرابط\n**•❒ لتحميل الفيديو من تـويتـر بالـرد علـى رابـط**\n\n\n**❻ بنتـرسـت :** \n\n`.ترست` + رابط\n**•❒ لتحميل مقاطـع الفيديو والصـور من بنتـرسـت**\n\n\n**❼ جـوجـل :**\n\n `.جوجل` + كلمـه\n**•❒ للبحث عـن الكلمـه في محرك البحث جـوجل**\n `.صور` + كلمـه / `.صور` + عدد + كلمـه\n**•❒ لتحميل الصـور من محرك البحث جـوجل**\n `.متحركه` + كلمـه\n**•❒ لتحميل متحركـات عبـر البحـث بالكـلمه**\n `.تحليل` بالرد على صوره\n**•❒ للبحث عن مصادر الصوره الاصليه وشبيهاتها على جـوجل**\n `.تخمين`  بالرد على ملصق\n**•❒ للبحث على مصادر الصورة الاصليه على جـوجل**\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪")

########### for SOURCE ZED by ~ @ZlZZl77 ###########


import random

from telethon import events


@bot.on(admin_cmd("م14"))
@bot.on(sudo_cmd("م14", allow_sudo=True))
async def _(zed):
    await eor(zed, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/ZedThon) 𓆪\n **⌔∮ قائـمه اوامر الانتحال :** \n⪼ `.نسخ`  \n⪼ `.اعاده` \n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪")

########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م15"))
@bot.on(sudo_cmd("م15", allow_sudo=True))
async def _(zed):
    await eor(zed, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/ZedThon) 𓆪\n **⌔∮ قائـمه اوامر النت :** \n⪼ `.بنك`  \n⪼ `.سرعه النت` \n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪")

########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م16"))
@bot.on(sudo_cmd("م16", allow_sudo=True))
async def _(zed):
    await eor(zed, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/ZedThon) 𓆪\n **⌔∮ قائـمه اوامر البوت :** \n⪼ `.اعاده تشغيل`  \n⪼ `.ايقاف ` \n⪼ `.تحديث ` \n⪼ `.تحديث الان `\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪")

########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################

import random

from telethon import events


@bot.on(admin_cmd("م17"))
@bot.on(sudo_cmd("م17", allow_sudo=True))
async def _(zed):
    await eor(zed, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/ZedThon) 𓆪\n **⌔∮ قائـمه اوامر الحساب :** \n⪼ `.ضع اسم` لتغير اسم حسابك \n⪼ `.جلب صوره` لتغير صوره حسابك \n⪼ `.ضع معرف ` لتغير معرف حسابك \n⪼ `.ضع بايو ` لتغير بايو حسابك \n⪼ `.كروباتي ` لعرض المجموعات التي انشأتها \n⪼ `.تهيئه الكل ` لحذف جميع صور حسابك \n⪼ `.تهيئه ` لحذف صوره واحده من حسابك \n⪼ `.الحساب ` لعرض معلومات الحساب \n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪")

########### for SOURCE ZED by ~ @ZlZZl77 ###########


import random

from telethon import events


@bot.on(admin_cmd("م18"))
@bot.on(sudo_cmd("م18", allow_sudo=True))
async def _(zed):
    await eor(zed, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/ZedThon) 𓆪\n **⌔∮ قائـمه اوامر السورس :** \n⪼ `.السورس ` لعرض معلومات السورس \n⪼ `.المطور` \n⪼ `.المده ` لعرض مدة استخدام السورس \n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪")

########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م25"))
@bot.on(sudo_cmd("م25", allow_sudo=True))
async def _(zed):
    await eor(zed, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/ZedThon) 𓆪\n **⌔∮ قائمـه الوقتـي :** \n⪼ `.الاسم تلقائي ` لوضع وقت يتغير مع اسم حسابك \n⪼ `.البروفايل تلقائي ` لوضع وقت يتغير مع صورة حسابك  \n⪼ `.البايو تلقائي` لوضع وقت يتغير مع بايو حسابك \n⪼ `.انهاء + الامر` لانهاء اوامر الوقتي \n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪")

########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م26"))
@bot.on(sudo_cmd("م26", allow_sudo=True))
async def _(zed):
    await eor(zed, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 - 𝑩𝑳𝑨𝑪𝑲𝑳𝑰𝑺𝑻](t.me/ZedThon) 𓆪\n **⌔∮ القائمة السوداء :** \n⪼ `.منع كلمه + الكلمه ` لمنع كلمه  \n⪼ `.الغاء منع + الكلمه` \n⪼ `.الكلمات المحظوره` \n⪼ `.ازعاج` \n⪼ `.الغاء ازعاج` \n⪼ `.قائمة الازعاج` \n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪")

########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م27"))
@bot.on(sudo_cmd("م27", allow_sudo=True))
async def _(zed):
    await eor(zed, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/ZedThon) 𓆪\n **⌔∮ قائمـه التحويلات :** \n\n**❶ تحـويلات :** \n⪼ `.لصوره ` بالـرد ع ملصق  \n⪼ `.لملصق`  بالـرد ع صـوره\n⪼ `.لمتحرك` بالـرد ع ملصق متحرك \n⪼ `.حول بصمه` \n⪼ `.حول صوت` \n\n\n**❷ تحـويلات :** \n⪼ `.دائري ` بالرد ع ملصق او صـوره \n⪼ `.لمتحركه`  بالـرد ع صـوره او ملصـق لتحـويلها ⇄ متحـركـه جاهـزه\n⪼ `.متحرك` بالرد ع فيديـو لتحـويله ⇄ متحـركـه \n⪼ `.نوت` بالـرد ع فيديـو لتحـويله ⇄ فيديـو نـوت \n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪")

########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م28"))
@bot.on(sudo_cmd("م28", allow_sudo=True))
async def _(zed):
    await eor(zed, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/ZedThon) 𓆪\n **⌔∮ قائـمه اوامر الکـشف العـام :** \n\n `.الاسماء` بالرد/المعرف/الايدي\n**•❒ لعرض قائمـه بسجل جميع اسماء الحساب + تاريخ انضمـام  الشخص على تليكـرام .**\n\n `.كروباتي عام/مالك/مشرف` \n**•❒ عام ⇎ قائمـه بجميع الكروبات المتواجد بيها**\n**•❒ مالك ⇎ قائمـه بجميع كروباتك الملكـيه**\n**•❒ مشرف ⇎ قائمـه بجميع الكروبات الانته مشرف بيها**\n\n `.قنواتي عام/مالك/مشرف` \n**•❒ عام ⇎ قائمـه بجميـع القنوات المنضـم بيها**\n**•❒ مالك ⇎ قائمـه بجميـع قنـواتك الملكـيه**\n**•❒ مشرف ⇎ قائمـه بجميـع القنوات الانته مشـرف بيها**\n\n `.احصائياتي/احصائياته` \n**•❒ لعرض قائمـه بجميـع احصائيات حسابك على تلكـرام**\n\n `.المشرفين` / .المشرفين + معـرف الكروب/القنـاة\n**•❒ لعـرض قائمـه بجميع مشرفين المجموعه/القناة المحدده**\n\n `.البوتات` / .البوتات + معـرف الكروب\n**•❒ لعـرض قائمـه بجميع بوتات المجموعه المحدده**\n\n `.الاعضاء` / .الاعضاء + معرف الكروب\n**•❒ لعـرض قائمـه بجميـع اعضـاء المجموعة المحدده**\n\n `.المجموعه` / .المجموعه + معرف الكروب/القناه\n**•❒ لرؤيـة كل المعلومات المتعلقه بالمجموعه او القناة المحدده**\n\n `.اكسباير` \n**•❒ لعـرض لستـة معلومات خاصه بالمجموعه او القناة المحدده**\n\n `.مسح المحظورين` \n**•❒ مسـح كل المحظورين في الدردشـه المحدده**\n\n `.تنظيف الحسابات` \n**•❒ لتنظـيف المجموعـه او القناة المحدده من الحسابات المحذوفـه**\n\n `.الاحصائيات` \n**•❒ لعـرض قائمـه بالحسابات المتصله والآخـر ظهور والحسابات المحذوفـه الـخ ...**\n\n 𓆩 [𝙎𝙊𝙐𝙍??𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪")

########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م29"))
@bot.on(sudo_cmd("م29", allow_sudo=True))
async def _(zed):
    await eor(zed, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/ZedThon) 𓆪\n **⌔∮ اوامـر الميديـا ( صـورة - فيديـو ) ذاتيـة التدمير :** \n\n⪼ `.ذاتيه ` بالرد ع (صوره / فيديو) ذاتيـة التدمير لحفظها بـ حافظـة حسابك   \n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪")

########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


import random

from telethon import events


@bot.on(admin_cmd("قائمه"))
@bot.on(sudo_cmd("قائمه", allow_sudo=True))
async def _(zed):
    await eor(zed, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/ZedThon) 𓆪\n⪼ **قائمه اوامر زد ثـون قم بضغط على الامر لنسخه :**\n⪼ `.ترحيب` \n⪼ `.مسح ترحيب` \n⪼ `.الترحيب ` \n⪼ `.حظر` \n⪼ `.الغاء حظر` \n⪼ `.المحظورين` \n⪼ `.كتم` \n⪼ `.الغاء كتم` \n⪼ `.تقيد` \n⪼ `.الغاء تقيد` \n⪼ `.رفع القيود` \n⪼ `.رفع` - مطي ، جلب \n⪼ `.تثبيت` \n⪼ `.الغاء تثبيت` \n⪼ `.الغاء تثبيت الكل` \n⪼ `.منع كلمه` \n⪼ `.الغاء منع` \n⪼ `.رفع مشرف` \n⪼ `.رفع مالك` \n⪼ `.تنظيف`  》》 يستخدم بالرد على الرساله \n⪼ `.نسخ`  》》لنسخ بروفايل الشخص \n⪼ `.اعاده` 》》لاعاده حسابك بعد نسخ الصوره.. الخ \n⪼ `نسبه الانوثه` \n⪼ `.اعادة التشغيل` \n⪼ `.ايقاف التشغيل` \n⪼ `.تحديث`  》 لتحديث السورس \n⪼ `.بحث` 》 مثلا  `.بحث عشك` \n⪼ `.صوره` 》 مثلا  .صوره طياره \n⪼ `.ايدي` 》 لعرض معلومات البوت \n⪼ `.بنك`  》 يعرض البنك \n⪼ `.سرعه النت` 》 قياس سرعه النت \n⪼ `.ترجمه ar` \n⪼ `.ترجمه en`  \n⪼ `.تكرار`+الرقم + الكلمه \n⪼ `.سبام`  》 كذالك نفس التكرار \n⪼ `.سماح` 》الامر فقط لميزه  حمايه الخاص \n⪼ `.رفض` 》 كذالك \n⪼ `.الكل` 》 لرفض الكل وتشغيل الحمايه \n⪼ `.بلوك` 》 من الخاص \n⪼ `.انبلوك` 》》لرفع الحظر من الخاص  \n⪼ `.المسموح لهم` 》لعرض قائمه السماح \n⪼ `.ايدي` 》 لعرض معلومات المستخدم \n⪼ `.الايدي` \n⪼ `.المجموعه 》》لعرض معلومات المجموعه ` \n⪼ `.السورس 》》 لعرض معلومات السورس ` \n⪼ `.مغادره` 》 تستخدم  لمغادره الكروب \n⪼ `.تاك` 》 لعمل تاك للكل \n⪼ `.للكل` + الكلام 》 لعمل تاك \n⪼ `.تلكراف ميديا` 》 يستخدم بالرد على الصوره \n⪼ `.تلكراف نص` 》 بالرد على الكتابه\n⪼ `.المطور` \n 𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪 ")

########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


import random

from telethon import events


@bot.on(admin_cmd("المطور"))
@bot.on(sudo_cmd("المطور", allow_sudo=True))
async def _(zed):
    await eor(zed, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 - 𝑫𝑬𝑽𝑬𝑳𝑶𝑷𝑬𝑹](t.me/ZedThon) 🧸♥️𓆪\n**𓍹━─━─━─━─𝙕𝞝𝘿─━─━─━─━𓍻**\n **𓄂༒** 𝑫𝑬𝑽 𝑼𝑺𝑬𝑹  ↬ @ZlZZl77 ༗\n **𓄂༒** 𝑫𝑬𝑽 𝑼𝑺𝑬𝑹  ↬ @ZZZZl1l ༗\n **𓄂༒** 𝑫𝑬𝑽 𝑼𝑺𝑬𝑹  ↬ @VVVVZ7 ༗")

########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع جلب(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع جلب(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """ For .link command, generates a link to the user's PM with a custom text. """
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌔∮ المستخدم [{custom}](tg://user?id={user.id}) \n ⌔∮تم رفعه جلب في زد",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌔∮ المستخدم [{tag}](tg://user?id={user.id}) \n ⌔∮تم رفعه جلب في زد",
        )


async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and len(args) != 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_obj, extra


async def ge(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع مطي(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع مطي(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """ For .link command, generates a link to the user's PM with a custom text. """
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌔∮ المستخدم [{custom}](tg://user?id={user.id}) \n ⌔∮ تم رفعه مطي هنا ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌔∮ المستخدم [{tag}](tg://user?id={user.id}) \n ⌔∮ تم رفعه مطي هنا ",
        )


async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and len(args) != 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_obj, extra


async def ge(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع مرتي(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع مرتي(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """ For .link command, generates a link to the user's PM with a custom text. """
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌔∮ المستخدم [{custom}](tg://user?id={user.id}) \n ⌔∮ تـم رفعـه مـࢪتك مـشي نخـلف 😹🤤",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌔∮ المستخدم [{tag}](tg://user?id={user.id}) \n ⌔∮ تـم رفعـه مـࢪتك مـشي نخـلف 😹🤤",
        )


########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################

from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع تاج(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع تاج(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """ For .link command, generates a link to the user's PM with a custom text. """
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌔∮ المستخدم [{custom}](tg://user?id={user.id}) \n ⌔∮ تـم رفعـه تـاج 👑🔥 ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌔∮ المستخدم [{tag}](tg://user?id={user.id}) \n ⌔∮ تـم رفعـه تـاج 👑🔥 ",
        )


########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع بكلبي(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع بكلبي(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """ For .link command, generates a link to the user's PM with a custom text. """
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌔∮ المستخدم [{custom}](tg://user?id={user.id}) \n ⌔∮ تـم رفعـه بڪلبك 🖤 ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌔∮ المستخدم [{tag}](tg://user?id={user.id}) \n ⌔∮ تـم رفعـه بڪلبك 🖤 ",
        )


########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع جريذي(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع جريذي(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """ For .link command, generates a link to the user's PM with a custom text. """
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌔∮ المستخدم [{custom}](tg://user?id={user.id}) \n ⌔∮ تـم رفعـه جـࢪيذي ۿنـا 😹🐀 ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌔∮ المستخدم [{tag}](tg://user?id={user.id}) \n ⌔∮ تـم رفعـه جـࢪيذي ۿنـا 😹🐀 ",
        )


########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع فرخ(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع فرخ(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """ For .link command, generates a link to the user's PM with a custom text. """
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌔∮ المستخدم [{custom}](tg://user?id={user.id}) \n ⌔∮ تم رفعه فرخ هنا ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌔∮ المستخدم [{tag}](tg://user?id={user.id}) \n ⌔∮ تم رفعه فرخ هنا ",
        )


async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and len(args) != 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_obj, extra


async def ge(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


import random

from telethon.tl.types import MessageEntityMentionName

ppp = [
    "100% 🔱💕.",
    "90%",
    "80%",
    "70%",
    "60%",
    "50%",
    "40%",
    "30%",
    "20%",
    "10%",
    "0%",
]


@bot.on(admin_cmd(pattern="نسبه الانوثه(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="نسبه الانوثه(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    ioi = random.choice(ppp)
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌔∮ نسبه الانوثه لـ [{custom}](tg://user?id={user.id}) هيه {ioi} ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌔∮ نسبه الانوثه لـ [{tag}](tg://user?id={user.id}) هيه {ioi} ",
        )


async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and len(args) != 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_obj, extra


async def ge(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


import time

from . import StartTime, get_readable_time, reply_id

DEFAULTUSER = "ZED"
CAT_IMG = "https://telegra.ph/file/5adc05c0958432a117183.jpg"
CUSTOM_ALIVE_TEXT = "𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 - 𝑫𝑬𝑽𝑬𝑳𝑶𝑷𝑬𝑹 𓆪"
EMOJI = "  𓄂† "


@bot.on(admin_cmd(outgoing=True, pattern="$مطور"))
@bot.on(sudo_cmd(pattern="$مطور", allow_sudo=True))
async def dev(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if CAT_IMG:
        cat_caption = f"**{CUSTOM_ALIVE_TEXT}**\n"
        cat_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝙕𝞝𝘿ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        cat_caption += f"**{EMOJI}** 𝑫𝑬𝑽 𝑼𝑺𝑬𝑹 1 ↬ @ZlZZl77 ༗\n"
        cat_caption += f"**{EMOJI}** 𝑫𝑬𝑽 𝑼𝑺𝑬𝑹 2 ↬ @N7QQQ ༗\n"
        cat_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝙕𝞝𝘿ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻"
        await alive.client.send_file(
            alive.chat_id, CAT_IMG, caption=cat_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n"
            f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝙕𝞝𝘿ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
            f"**{EMOJI}** 𝑫𝑬𝑽 𝑼𝑺𝑬𝑹 1 ↬ @ZlZZl77 ༗\n"
            f"**{EMOJI}** 𝑫𝑬𝑽 𝑼𝑺𝑬𝑹 2 ↬ @N7QQQ ༗\n"
            f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧ𝙕𝞝𝘿ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻",
        )
