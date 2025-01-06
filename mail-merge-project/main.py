PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    # print(names)

with open("./Input/Letters/starting_letter.docx") as letter_file:
    letter_content = letter_file.read()
    # print(letter_content)
    for name in names:
        strip_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, strip_name)
        with open(f"./Output/ReadyToSend/letter_for_{strip_name}.docx", mode="w") as completed_mail_file:
            completed_mail_file.write(new_letter)
