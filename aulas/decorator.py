def upper_letter(f):
    def upper(msg):
        return f(msg).upper()
    return upper

@upper_letter
def say(msg):
    return msg

fala = say('teste')
print(fala)
