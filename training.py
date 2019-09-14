
def msg_to_mom():

    """ get the authentication code"""

auth_code = "f658fb2ddd2a015563ef71ad14c92c00"
sid_code = "ACaf18626d11d23e66e284ba99f2614bfd"

client_codes = (auth_code, sid_code)

"""create the contacts"""

contact_info = {"Mom": "+19736777572", "Dad": "+18622168531"}

for key, value in contact_info.item():
    msg_loved_ones = client_codes.messages.create(
        body = "Good Morning",
        from_= "whatsapp:+19736412137",
        to= "whatsapp:" + value,
    )
    print(msg_loved_ones)
