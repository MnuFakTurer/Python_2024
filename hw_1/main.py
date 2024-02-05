with open("File.txt", "w") as file:
    text_write = " - STAR WARS | REBELS |" "\n - STAR WARS | AHSOKA |"

    file.write(text_write)

with open("File.txt") as file:
    content = file.read()
    print(content)
