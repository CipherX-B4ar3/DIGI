import asyncio
from rubika import Client, methods, models, handlers, exceptions
import time
from random import choice as ch
import os.path
import logging
from re import findall
logging.basicConfig(level=logging.ERROR)

admins  = "CipherX"
Channel = "Yes_GNG"
status  = []
mute    = []

async def main():
    async with Client(session="DIGI") as client:
        @client.on(handlers.MessageUpdates(models.raw_text))
        async def DIGI(event):
            me = await client.get_me()
            me_guid = me.user.user_guid
            admin = await client(methods.extras.GetObjectByUsername(username=admins))
    
            if os.path.exists("BOT"):
                mode = open("BOT").read()
            else:
                mode = "off"
            if mode == "on":
                if event.raw_text.startswith("/run") and event.type == "Group":
                    try:
                        count = status.count(event.object_guid)
                        acsess = await client(methods.groups.GetGroupAdminMembers(group_guid= event.object_guid ,start_id=None))
                        for admins_group in acsess.in_chat_members:
                            if event.message.author_object_guid in admins_group.member_guid:
                                if count == 1:
                                       await event.reply("ربـات قـبلـا در ایـن گـروه فـعـال شـده اسـت •❌")
                                elif count == 0:
                                    status.append(event.object_guid)    
                                    await event.reply("🔥 ربـات بـامـوفـقـیت در گـروه **فعال** شـد 🔥\n\n❌ مهم :\n• دقـت داشـتـه باشـید این ربـات رایگـان اسـت و فـقـط لـینـک پـاک مـیکـنـد •\n\n🔥👻 بـرای تـهـیـه ربـات حـرفـه ای و پـرسـرعـت بـه ایـدی زیـر مراجـعـه فـرمـایید :\n@CipherX")
                    except:
                        pass

                if event.object_guid in status:
                    try:
                    
                        if event.find_keys(keys=['forwarded_from']):
                            try:
                                await event.delete_messages()
                            except:
                                pass
                        if event.raw_text.startswith("https://") or event.raw_text.startswith("http://"):
                            try:
                                await event.delete_messages()
                            except:
                                pass
                        za_1 = findall(r"https://rubika.ir/joing/\w{32}",event.raw_text)
                        za_2 = findall(r"https://rubika.ir/joinc/\w{32}",event.raw_text)
                        if za_1:
                            try:
                                await event.delete_messages()
                            except:
                                pass
                        if za_2:
                            try:
                                await event.delete_messages()
                            except:
                                pass
                    except:
                        pass

                if event.raw_text.startswith("سرگرمی") and event.type == "Group":
                    try:
                        acsess = await client(methods.groups.GetGroupAdminMembers(group_guid= event.object_guid ,start_id=None))
                        for admins_group in acsess.in_chat_members:
                            if event.message.author_object_guid in admins_group.member_guid:
                                await event.reply(f"""
دستورات سرگرمی :

• کی با کی رل میزنه 👻✨

• کی منو دوست داره 👻✨

• کی با من رل میزنه 👻✨


دستورات گروه :


/lock

🔥• قفل گروه •🔥

/unlock

🔥• باز کردن گروه •🔥

/ban

🔥• بن کردن کاربر •🔥           

/mute

🔥• میوت کردن کاربر •🔥                        

/unmute

🔥• حذف میوت •🔥 

                """)
                    except:
                        pass
                if event.raw_text.startswith("/ban")and event.type == "Group":
                    acsess = await client(methods.groups.GetGroupAdminMembers(group_guid= event.object_guid ,start_id=None))
                    for admins_group in acsess.in_chat_members:
                        if event.message.author_object_guid in admins_group.member_guid:
                            command = event.raw_text.replace("/ban","").strip()
                            ids = command.replace("@","").strip()
                            usernames = await client(methods.extras.GetObjectByUsername(username=ids))
                            await client(methods.groups.BanGroupMember(event.object_guid,ids.user.user_guid))
                            await event.send_message(event.object_guid,message=f'🔥 کاربر {usernames.user.first_name} \n• از گروه بن شد •')

                if event.raw_text.startswith("/lock")and event.type == "Group":
                    acsess = await client(methods.groups.GetGroupAdminMembers(group_guid= event.object_guid ,start_id=None))
                    for admins_group in acsess.in_chat_members:
                        if event.message.author_object_guid in admins_group.member_guid:
                            await client(methods.groups.SetGroupDefaultAccess(event.objec_guid,access_list=None))
                            await client.send_message("🔥 گروه قفل شد 🔥")      

                if event.raw_text.startswith("/unlock")and event.type == "Group":
                    acsess = await client(methods.groups.GetGroupAdminMembers(group_guid= event.object_guid ,start_id=None))
                    for admins_group in acsess.in_chat_members:
                        if event.message.author_object_guid in admins_group.member_guid:
                            await client(methods.groups.SetGroupDefaultAccess(event.objec_guid,access_list=["AddMember","SendMessages"]))
                            await client.send_message("🔥 گروه باز شد 🔥")       

                if event.raw_text.startswith("/mute")and event.type == "Group":
                    acsess = await client(methods.groups.GetGroupAdminMembers(group_guid= event.object_guid ,start_id=None))
                    for admins_group in acsess.in_chat_members:
                        if event.message.author_object_guid in admins_group.member_guid:
                            command = event.raw_text.replace("/mute","").strip()
                            ids = command.replace("@","").strip()
                            usernames = await client(methods.extras.GetObjectByUsername(username=ids))
                            mutecount = mute.count(usernames.user.user_guid)
                            if mutecount == 1:
                                await event.reply(f"❌ کاربر {usernames.user.first_name}\n• قبلا میوت بود •")
                            elif mutecount == 0:
                                mute.append(usernames.user.user_guid)
                                await client.send_message(event.object_guid,message=f'🔥 کاربر {usernames.user.first_name}\n• میوت شد •')

                if event.raw_text.startswith("/unmute")and event.type == "Group":
                    acsess = await client(methods.groups.GetGroupAdminMembers(group_guid= event.object_guid ,start_id=None))
                    for admins_group in acsess.in_chat_members:
                        if event.message.author_object_guid in admins_group.member_guid:
                            command = event.raw_text.replace("/umute","").strip()
                            ids = command.replace("@","").strip()
                            usernames = await client(methods.extras.GetObjectByUsername(username=ids))
                            mute.remove(usernames.user.user_guid)
                            await client.send_message(event.object_guid,message=f'🔥 کاربر {usernames.user.first_name}\n• حذف میوت شد •')
                if event.raw_text.startswith("ربات") or event.raw_text.startswith("بات") and event.type == "Group":
                    try:
                        await event.reply(ch(['جونم ? ', 'بفرما', 'جون دلم؟‌', 'بگو', 'چی میخوای؟', 'زود بگو کارتو', 'خستم کردی دگ چیه ؟']))
                    except:
                        pass
                if event.message.author_object_guid in mute:
                    try:
                        await event.delete_messages()
                    except:
                        pass
                if event.raw_text.startswith("کی با کی رل میزنه") or event.raw_text.startswith("کی با کی رل میزنع") and event.type == "Group":
                    try:
                        dialogs = await client(methods.groups.GetGroupAllMembers(group_guid= event.object_guid ,search_text=None, start_id=None))
                        for i in range(2):
                            random = ch(dialogs.in_chat_members)
                            random1 = ch(dialogs.in_chat_members)
                            name = random.first_name
                            name1 = random1.first_name
                        if name == name1:
                            await event.delete_messages()
                        else:
                            await event.reply(f"""
این [ {name}]({random.member_guid})

با این [ {name1}]({random1.member_guid}) 

رل میزنه ❤️🗿       
                        """)
                     except:
                        pass
                if event.raw_text.startswith("کی با من رل میزنه") or event.raw_text.startswith("کی با من رل میزنع") and event.type == "Group":
                    try:
                        dialogs = await client(methods.groups.GetGroupAllMembers(group_guid= event.object_guid ,search_text=None, start_id=None))
                        random = ch(dialogs.in_chat_members)
                        name = random.first_name
                        await event.reply(f"این [ {name}]({random.member_guid}) باهات رل میزنه")
                    except:
                        pass
                if event.raw_text.startswith("کی منو دوست داره") or event.raw_text.startswith("با منو دوست دارع") and event.type == "Group":
                    try:
                        dialogs = await client(methods.groups.GetGroupAllMembers(group_guid= event.object_guid ,search_text=None, start_id=None))
                        random = ch(dialogs.in_chat_members)
                        name = random.first_name
                        await event.reply(f"این [ {name}]({random.member_guid}) باهات رل میزنه")
                    except:
                        pass
                if event.raw_text and event.type == "User" and not event.message.author_object_guid == admin.user.user_guid:
                    users = await client(methods.users.GetUserInfo(event.message.author_object_guid))
                    if event.raw_text == "/start":
                        try:
                            await client.send_message(event.object_guid,file_inline="bot.png",message=f"""
ســـلام کاربـــر ( {users.user.first_name} ) گرامـــی👋🏻🌹

بـه ربــات 𝖨𝖮 𝖣𝖨𝖦𝖨 خـوش آمـدید 

بـرای افـزودن ربــات بـه گـروه خـود از دسـتـور 

/help

اسـتـفـاده کنـیـد

مـوفـق بــاشـید ✌️
            """)
                        except:
                            pass
                    elif event.raw_text == "/help":
                        await client.send_message(event.object_guid,message=f"""
بـرای عـضو شـدن ربــات بـه گـروهـتـون از دسـتور جـویـن اسـتفـاده کـنـید 🔥

مـانـنـد‌:

/join لـینـک گـروه 👻


🔰 پـشـتـیـبـانـی:

**RUBIKA** 👇🏻\n@CipherX                               
                                
                                """)
                    elif event.raw_text.startswith("/join"):
                        try:
                            link = findall(r"https://rubika.ir/joing/\w{32}",event.raw_text)
                            if link:
                                for i in link:
                                    global Check_Join
                                    Check_Join = await client(methods.groups.GroupPreviewByJoinLink(link=i))

                                    if Check_Join.has_joined == True:
                                        await event.reply("درحـال حـاضـر تـو گـروه هـسـتـم ❤️😐")
                                    if Check_Join.has_joined == False:
                                        group = await client(methods.groups.JoinGroup(link=i))
                                        await client.send_message(event.object_guid,message=f"""
ربـات بـا موفـقیت عـضـو گـروه {group.group.group_title} شـد 🔥👇🏻


بـرای اجـرای درسـت ربـات ان را ادمـین کنـید •

بـرای اطـلاع از وضـعیت ربـات •

•‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍ ‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌کانال رو چک کنیـב  • 🔥👻

🔰 @Yes_GNG


مـشکـلی بـود پـی وی بـگـید 🗿❤️

**RUBIKA** 👇🏻

@CipherX
                                        """)
                                        await client.send_message(group.group.group_guid,message=f"""
ربـات بـامـوفـقـیت در گـروه {group.group.group_title} عـضـو شـد 🔥👇🏻


بـرای اجـرای ربـات دسـتـور 🔰

• /run  ‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌

رو ارسـال کـنـید •


بـا تـشکـر 𝗖𝗜𝗣𝗛𝗘𝗥-𝙓 🔥👻
""")
                        except:
                            pass
                    else:
                        await client.send_message(event.object_guid,file_inline="start.jpg",message=f"""
 🔥👻 دوسـت داری گـروهـت یـه ربـات هـوشـمنـد داشـتـه بـاشـه ؟\n\n• اونـم بـه صـورت کامـلا رایـگـان •\nرو پیام زیر کلیک کن\n• /start  \nبـرای هـمـایـت از مـا و دریـافـت وضـعـیـت ربـات
در کـانـال زیـر جـویـن شـویـد\n\n1 : @{Channel}\n\n🔰 پـشـتـیـبـانـی:\n**RUBIKA** 👇🏻\n@CipherX
                            
                            """)
            else:
                pass

            if event.raw_text.startswith(".bot") and event.type == "User":
                if event.message.author_object_guid in admin.user.user_guid: 
                    try:
                        CyA = event.raw_text.replace(".bot","").strip()
                        if CyA == "on":
                            await event.reply("ادمین بات شناسایی شد ✅\n\n• ربات روشن شد •")
                            open("BOT","w").write("on")
                        elif CyA == "off":
                            await event.reply("ادمین بات شناسایی شد ✅\n\n• ربات خاموش شد •")
                            open("BOT","w").write("off")
                            dialogs = await client(methods.chats.GetChats(start_id=None))
                            if dialogs.chats:
                                for index, dialog in enumerate(dialogs.chats, start=1):
                                    if methods.groups.SendMessages in dialog.access:
                                        await client.send_message(dialog.object_guid,message=f"[ربات برای دلایلی فعلا خاموش میشود....]{me_guid}")
                        else:
                            await event.reply("لطفا دستور رو درست وارد کنید ❌")
                    except:
                        pass
                else:
                    await client.send_message(event.object_guid,message="شما به عنوان ادمین ربات شناسایی نشدید ❌")
            elif event.raw_text == "امار" and event.type == "User":
                if event.message.author_object_guid in admin.user.user_guid:
                    try:
                        tedad = len(status)
                        await event.reply(f"""🔰 امار فعلی ربات :‌ {tedad}""")
                    except:
                        pass

        await client.run_until_disconnected()

asyncio.run(main())
