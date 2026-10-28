def process_romeo(file):
    unique_words = set()

    try:
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                words = line.split()
                for word in words:
                    unique_words.add(word)

        result_list = sorted(list(unique_words))
        print(result_list)
    except FileNotFoundError:
        print(f"Файл {file} не найден.")


process_romeo('romeo.txt')