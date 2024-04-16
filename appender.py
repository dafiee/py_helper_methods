"""Appends @ebo.co.ug to emails"""

mails = []

try:
    with open('source.txt', 'r', encoding='utf-8') as sourceList:
        mails = sourceList.readlines()

    with open('list.txt', 'a', encoding='utf-8') as mailList:
        for mail in mails:
            mailList.write(f"{mail}@ebo.co.ug".replace("\n", "")+"\n")
except OSError as e:
    print(f"An Error occured!\n {e.__traceback__}")
