import sys
import re

def markdown_para_html(texto: str) -> str:

    # Cabeçalhos 
    for nivel in range(3, 0, -1):
        padrao = rf'^{"#" * nivel}\s+(.*)$'
        texto = re.sub(padrao, rf'<h{nivel}>\1</h{nivel}>', texto, flags=re.MULTILINE)

    # Listas numeradas
    item_lista_pattern = r'^\d+\.\s+(.*)$'
    texto = re.sub(item_lista_pattern, r'<li>\1</li>', texto, flags=re.MULTILINE)

    bloco_lista_pattern = r'((?:<li>.*</li>\n?)+)'
    texto = re.sub(bloco_lista_pattern, r'<ol>\n\1</ol>', texto)

    # Imagens
    img_pattern = r'!\[([^\]]+)\]\(([^)]+)\)'
    texto = re.sub(img_pattern, r'<img src="\2" alt="\1"/>', texto)

    # Links
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    texto = re.sub(link_pattern, r'<a href="\2">\1</a>', texto)

    # Negrito 
    negrito_pattern = r'\*\*([^*]+)\*\*'
    texto = re.sub(negrito_pattern, r'<b>\1</b>', texto)

    # Itálico
    italico_pattern = r'\*([^*]+)\*'
    texto = re.sub(italico_pattern, r'<i>\1</i>', texto)

    return texto


def main():
    if len(sys.argv) > 1:
        ficheiro_entrada = sys.argv[1]
    else:
        ficheiro_entrada = "exemplo.md"

    if ficheiro_entrada.endswith(".md"):
        ficheiro_saida = ficheiro_entrada[:-3] + ".html"
    else:
        ficheiro_saida = ficheiro_entrada + ".html"

    try:
        with open(ficheiro_entrada, "r", encoding="utf-8") as f:
            conteudo_md = f.read()
    except FileNotFoundError:
        print(f"Erro: O ficheiro '{ficheiro_entrada}' não foi encontrado.")
        return

    conteudo_html = markdown_para_html(conteudo_md)

    with open(ficheiro_saida, "w", encoding="utf-8") as f:
        f.write(conteudo_html)

    print(f"Sucesso! Ficheiro convertido gravado em: '{ficheiro_saida}'")


if __name__ == "__main__":
    main()