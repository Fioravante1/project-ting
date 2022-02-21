def exists_word(word, instance):
    word_list = []
    for index in range(len(instance.data)):
        file = instance.search(index)
        for line in file["linhas_do_arquivo"]:
            repeat_lines = []
            if word.lower() in line.lower():
                repeat_lines.append({"linha": index + 1})

    if repeat_lines:
        word_list.append({
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": repeat_lines,
        })
    return word_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
