def write_to_file(file_path: str, writing: str):
    with open(file_path, "a+") as file:
        file.write(writing + '\n')


write_to_file("example.txt", "HELLO WORLD")