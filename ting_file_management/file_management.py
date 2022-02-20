import sys

# https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python


def txt_importer(path_file):
    try:
        if not path_file.endswith('.txt'):
            return sys.stderr.write('Formato inválido\n')
        with open(path_file, 'r') as file:
            return file.read().split('\n')
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
