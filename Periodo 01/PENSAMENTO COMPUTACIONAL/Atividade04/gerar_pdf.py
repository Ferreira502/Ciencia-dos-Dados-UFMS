from pathlib import Path
import textwrap


OUTPUT = Path(__file__).with_name("Atividade04_EcoColeta.pdf")

PAGE_W = 595
PAGE_H = 842
MARGIN_X = 50
TOP_Y = 790
BOTTOM_Y = 60


def pdf_escape(text: str) -> str:
    return (
        text.replace("\\", "\\\\")
        .replace("(", "\\(")
        .replace(")", "\\)")
    )


class Page:
    def __init__(self):
        self.ops = []

    def text(self, x, y, size, text, font="F1"):
        safe = pdf_escape(text)
        self.ops.append(f"BT /{font} {size} Tf 1 0 0 1 {x} {y} Tm ({safe}) Tj ET")

    def rect(self, x, y, w, h):
        self.ops.append(f"{x} {y} {w} {h} re S")

    def fill_rect(self, x, y, w, h, gray=0.9):
        self.ops.append(f"{gray} g {x} {y} {w} {h} re f 0 g")

    def line(self, x1, y1, x2, y2):
        self.ops.append(f"{x1} {y1} m {x2} {y2} l S")

    def render(self) -> bytes:
        return "\n".join(self.ops).encode("latin-1", errors="replace")


def wrap_text(text: str, size: int, width: int) -> list[str]:
    chars = max(25, int(width / (size * 0.52)))
    return textwrap.wrap(text, width=chars, break_long_words=False, break_on_hyphens=False)


pages = []
page = Page()
y = TOP_Y


def new_page():
    global page, y
    pages.append(page)
    page = Page()
    y = TOP_Y


def ensure_space(lines_needed: int, size: int = 12, leading: int = 16):
    global y
    needed = lines_needed * leading + size
    if y - needed < BOTTOM_Y:
        new_page()


def add_heading(text: str, size: int = 18):
    global y
    ensure_space(2, size=size, leading=size + 6)
    page.text(MARGIN_X, y, size, text, font="F2")
    y -= size + 10


def add_paragraph(text: str, size: int = 12, extra_gap: int = 8):
    global y
    lines = wrap_text(text, size, PAGE_W - (2 * MARGIN_X))
    ensure_space(len(lines) + 1, size=size)
    for line in lines:
        page.text(MARGIN_X, y, size, line)
        y -= 16
    y -= extra_gap


def add_bullets(items: list[str], size: int = 12):
    global y
    for item in items:
        lines = wrap_text("- " + item, size, PAGE_W - (2 * MARGIN_X))
        ensure_space(len(lines) + 1, size=size)
        for idx, line in enumerate(lines):
            x = MARGIN_X if idx == 0 else MARGIN_X + 14
            page.text(x, y, size, line)
            y -= 16
    y -= 8


def add_numbered(items: list[str], size: int = 12):
    global y
    for idx, item in enumerate(items, start=1):
        lines = wrap_text(f"{idx}. {item}", size, PAGE_W - (2 * MARGIN_X))
        ensure_space(len(lines) + 1, size=size)
        for line_idx, line in enumerate(lines):
            x = MARGIN_X if line_idx == 0 else MARGIN_X + 16
            page.text(x, y, size, line)
            y -= 16
    y -= 8


add_heading("Atividade 04 - Pensamento Computacional", size=20)
add_heading("EcoColeta: jogo educativo em Scratch", size=16)

add_heading("1. Descricao do problema", size=14)
add_paragraph(
    "Um problema comum no cotidiano de escolas, bairros e espacos publicos e o descarte incorreto de residuos reciclaveis. "
    "Muitas pessoas querem colaborar com a coleta seletiva, mas ainda possuem duvidas sobre onde descartar papel, plastico, vidro e metal."
)
add_paragraph(
    "Na comunidade escolar, esse problema aparece principalmente em momentos de lanche, eventos e uso compartilhado de salas. "
    "Garrafas plasticas, latas e papeis sao jogados no lixo errado por falta de orientacao imediata e de uma forma simples de aprendizado."
)
add_bullets(
    [
        "falta de conhecimento sobre a separacao correta dos residuos;",
        "pouca estimulacao para aprender o tema de forma pratica;",
        "dificuldade de transformar orientacoes teoricas em uma acao rapida no dia a dia.",
    ]
)

add_heading("2. Solucao digital proposta", size=14)
add_paragraph(
    "A solucao proposta e um jogo educativo desenvolvido no Scratch chamado EcoColeta. Nele, o jogador deve arrastar um residuo ate a lixeira correta. "
    "Cada acerto gera pontos e uma mensagem positiva. Cada erro gera uma orientacao curta explicando a separacao correta."
)
add_paragraph(
    "A proposta usa uma ferramenta acessivel e visual para ensinar, de forma ludica, uma habilidade util para a escola e para a comunidade."
)

add_heading("3. Aplicacao dos pilares do PC", size=14)
add_paragraph("Decomposicao: o problema foi dividido em partes menores para facilitar o planejamento.")
add_bullets(
    [
        "identificar os tipos principais de residuos reciclaveis;",
        "definir as lixeiras correspondentes;",
        "criar a mecanica de interacao do jogador;",
        "registrar acertos, erros e pontuacao;",
        "exibir mensagens educativas e tela final.",
    ]
)
add_paragraph("Reconhecimento de padroes: foram observados comportamentos que se repetem.")
add_bullets(
    [
        "os mesmos tipos de residuos aparecem com frequencia no dia a dia;",
        "os erros de descarte costumam se repetir;",
        "o aprendizado melhora com retorno imediato sobre acerto ou erro.",
    ]
)
add_paragraph("Abstracao: o problema real foi simplificado para destacar apenas os elementos essenciais.")
add_bullets(
    [
        "foram considerados apenas quatro grupos principais: papel, plastico, vidro e metal;",
        "cada rodada apresenta um unico residuo por vez;",
        "o foco nao e representar todo o sistema da cidade, mas ensinar a decisao correta.",
    ]
)

new_page()

add_heading("3. Aplicacao dos pilares do PC", size=14)
add_paragraph("Desenvolvimento de algoritmos: o jogo segue uma sequencia logica de execucao.")
add_numbered(
    [
        "iniciar o jogo e zerar a pontuacao;",
        "definir o tempo da partida;",
        "sortear um residuo;",
        "mostrar o residuo ao jogador;",
        "verificar a lixeira escolhida;",
        "comparar a resposta com o tipo correto do item;",
        "atualizar pontuacao e mensagem de retorno;",
        "repetir o processo ate o tempo acabar;",
        "exibir o resultado final.",
    ]
)

add_heading("4. Representacao da solucao no Scratch", size=14)
add_paragraph(
    "A figura abaixo representa a organizacao da tela principal do projeto no Scratch. O residuo aparece na parte superior, "
    "o jogador o arrasta e depois clica na lixeira correspondente para validar a resposta."
)

stage_x = 80
stage_y = 360
stage_w = 430
stage_h = 280
page.rect(stage_x, stage_y, stage_w, stage_h)
page.text(stage_x + 150, stage_y + stage_h - 24, 16, "EcoColeta", font="F2")
page.text(stage_x + 20, stage_y + stage_h - 48, 11, "Tempo: 60")
page.text(stage_x + 320, stage_y + stage_h - 48, 11, "Pontuacao: 0")
page.text(stage_x + 70, stage_y + stage_h - 80, 11, "Arraste o lixo ate a lixeira certa e clique na lixeira.")

page.fill_rect(stage_x + 180, stage_y + 165, 70, 40, gray=0.85)
page.text(stage_x + 198, stage_y + 180, 11, "Lixo")
page.text(stage_x + 170, stage_y + 150, 10, "ator com varias fantasias")

bin_y = stage_y + 35
bin_w = 82
bin_h = 70
bin_labels = [("Papel", 100), ("Plastico", 195), ("Vidro", 290), ("Metal", 385)]
for label, x in bin_labels:
    page.rect(stage_x + x, bin_y, bin_w, bin_h)
    page.text(stage_x + x + 18, bin_y + 28, 11, label)

y = stage_y - 20
add_bullets(
    [
        "Cenario com titulo, tempo, pontuacao e instrucao curta.",
        "Ator Lixo com fantasias como jornal, garrafa plastica, vidro e lata.",
        "Quatro atores de lixeira: papel, plastico, vidro e metal.",
        "Feedback instantaneo com mensagens de acerto e erro.",
    ]
)

add_heading("5. Resultado esperado", size=14)
add_paragraph(
    "Espera-se que o jogo contribua para a conscientizacao sobre coleta seletiva, reforcando o aprendizado de forma ludica, rapida e acessivel. "
    "A proposta pode ser usada em sala de aula, feiras escolares ou atividades com a comunidade."
)

new_page()

add_heading("6. Roteiro de implementacao no Scratch", size=14)
add_paragraph("Variaveis do projeto: pontuacao, tempo, itemAtual e tipoAtual.")
add_paragraph("Atores do projeto: Lixo, Lixeira Papel, Lixeira Plastico, Lixeira Vidro e Lixeira Metal.")

code_lines = [
    "Palco:",
    "quando bandeira verde for clicada",
    "defina [pontuacao] para 0",
    "defina [tempo] para 60",
    "transmita [novo item]",
    "repita ate <tempo = 0>",
    "  espere 1 segundos",
    "  mude [tempo] por -1",
    "fim",
    "transmita [fim de jogo]",
    "",
    "Ator Lixo:",
    "quando eu receber [novo item]",
    "mostre",
    "va para x: 0 y: 120",
    "defina [itemAtual] para aleatorio entre 1 e 8",
    "troque a fantasia e defina [tipoAtual]",
    "",
    "Exemplo de lixeira:",
    "quando este ator for clicado",
    "se <tocando em [Lixo]> e <tipoAtual = papel> entao",
    "  mude [pontuacao] por 1",
    "  diga [Acertou!] por 1 segundos",
    "  transmita [acertou]",
    "senao",
    "  diga [Esse item nao vai aqui.] por 1 segundos",
    "fim",
]

for line in code_lines:
    ensure_space(1, size=10, leading=13)
    font = "F2" if line.endswith(":") else "F3"
    size = 11 if line.endswith(":") else 10
    x = MARGIN_X if line else MARGIN_X
    page.text(x, y, size, line, font=font)
    y -= 13

y -= 8
add_paragraph(
    "O roteiro completo de blocos foi salvo no arquivo scratch_blocos.md, com as falas e a logica de cada lixeira separadas para facilitar a montagem no editor."
)
add_paragraph(
    "Conclusao: a proposta atende ao problema identificado, aplica os quatro pilares do Pensamento Computacional e apresenta uma representacao clara de como a solucao seria implementada no Scratch."
)

pages.append(page)


def build_pdf(output_path: Path):
    font_objects = []
    for base_font in ["Helvetica", "Helvetica-Bold", "Courier"]:
        font_objects.append(
            f"<< /Type /Font /Subtype /Type1 /BaseFont /{base_font} /Encoding /WinAnsiEncoding >>".encode("latin-1")
        )

    objects = []
    objects.extend(font_objects)

    page_object_numbers = []
    content_object_numbers = []

    for p in pages:
        content = p.render()
        content_obj = f"<< /Length {len(content)} >>\nstream\n".encode("latin-1") + content + b"\nendstream"
        objects.append(content_obj)
        content_number = len(objects)
        content_object_numbers.append(content_number)

        page_dict = (
            f"<< /Type /Page /Parent 0 0 R /MediaBox [0 0 {PAGE_W} {PAGE_H}] "
            f"/Resources << /Font << /F1 1 0 R /F2 2 0 R /F3 3 0 R >> >> "
            f"/Contents {content_number} 0 R >>"
        ).encode("latin-1")
        objects.append(page_dict)
        page_object_numbers.append(len(objects))

    kids = " ".join(f"{n} 0 R" for n in page_object_numbers)
    pages_dict = f"<< /Type /Pages /Count {len(page_object_numbers)} /Kids [{kids}] >>".encode("latin-1")
    objects.append(pages_dict)
    pages_number = len(objects)

    for page_number in page_object_numbers:
        page_bytes = objects[page_number - 1].decode("latin-1").replace("/Parent 0 0 R", f"/Parent {pages_number} 0 R")
        objects[page_number - 1] = page_bytes.encode("latin-1")

    catalog = f"<< /Type /Catalog /Pages {pages_number} 0 R >>".encode("latin-1")
    objects.append(catalog)
    catalog_number = len(objects)

    pdf = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for idx, obj in enumerate(objects, start=1):
        offsets.append(len(pdf))
        pdf.extend(f"{idx} 0 obj\n".encode("latin-1"))
        pdf.extend(obj)
        pdf.extend(b"\nendobj\n")

    xref_pos = len(pdf)
    pdf.extend(f"xref\n0 {len(objects) + 1}\n".encode("latin-1"))
    pdf.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        pdf.extend(f"{offset:010} 00000 n \n".encode("latin-1"))

    trailer = f"<< /Size {len(objects) + 1} /Root {catalog_number} 0 R >>"
    pdf.extend(f"trailer\n{trailer}\nstartxref\n{xref_pos}\n%%EOF\n".encode("latin-1"))
    output_path.write_bytes(pdf)


if __name__ == "__main__":
    build_pdf(OUTPUT)
    print(f"PDF gerado em: {OUTPUT}")
