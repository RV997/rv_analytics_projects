r = True
while(r):
    print("for exit enter exit")
    search = input("search: ")
    if search == "exit":
        r = False
    else:
        with open("searchbox_dataset.txt", "a") as f:
             f.write(search)
             f.write('\n')

