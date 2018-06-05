import itchat

itchat.auto_login(hotReload=True)

itchat.send('Hello, filehelper', toUserName='filehelper')
itchat.send('~', toUserName='房主十月')
itchat.send('~', toUserName='@3101e9a75cd8a3b5b66f19abff4ffc2490bd28acc9a6e4838689185de752dfb0')
# @cc593e852d478d7cddb338db0752a6be94bbc311754966a8b769516ae7eb3c3b

print(itchat.search_friends(name='宴宴雁雁'))



@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    print(msg.text)
# itchat.run()

    # import itchat
    #
    # @itchat.msg_register(itchat.content.TEXT)
    # def text_reply(msg):
    #     return msg.text
    #
    # itchat.auto_login()
    # itchat.run()
