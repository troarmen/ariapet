# Home — estrutura e copy

**Data:** 21/08/2026
**Arquivo:** `theme/templates/index.json`
**Status:** primeira versão construída · **copy provisória, sujeita a aprovação**

---

## O que havia antes

O Horizon de fábrica entrega a home em dois blocos: um hero com o texto
"Browse our latest products" e um botão "Shop all", seguido de uma grade de **8 produtos em
4 colunas**. Tudo em inglês, e a grade inteira de uma vez — exatamente o que o brief da
referência descarta: *"curadoria em blocos curtos, nunca a grade inteira de uma vez"*.

---

## A estrutura nova

Quatro tempos, com ritmo editorial alternando foto cheia e respiro branco:

| # | Seção | Papel | Imagem |
|---|---|---|---|
| 1 | **Abertura** | Hero de altura grande, gradiente de baixo para cima | `Aria7137.jpg` (2051×1641) |
| 2 | **A coleção** | Curadoria de **4 produtos**, 4 colunas, fundo branco | — |
| 3 | **Editorial · marca** | Faixa com foto sangrada, leva para a história da marca | `Aria7097.jpg` (2051×3076) |
| 4 | **Editorial · tamanhos** | Faixa centralizada, leva para o guia de tamanhos | `Aria8046.jpg` (2097×3146) |

Nos três blocos com foto, a imagem sangra de ponta a ponta e o texto se apoia na calha da
página — alinhado com a grade de produtos da seção 2.

O quarto bloco não é enfeite: o brief diz que a navegação existe para *"resolver a dúvida de
tamanho antes da compra"*. Como as coleções por porte ainda não existem, o guia de tamanhos
ocupa esse papel na home desde já.

---

## Copy provisória

Escrita para aprovação, não para publicar. Tom contido, sem adjetivo empilhado.

| Seção | Rótulo | Título | Botão |
|---|---|---|---|
| Abertura | ACESSÓRIOS PARA PETS | O essencial, elevado. | Ver a coleção |
| A coleção | — | A coleção | Ver tudo |
| Marca | A MARCA | Design autoral, para o passeio de todo dia. | Nossa história |
| Tamanhos | ANTES DE COMPRAR | Encontre o tamanho certo. | Guia de tamanhos |

**"O essencial, elevado."** não é invenção nossa — é a tradução da própria descrição que a
cliente já usa na coleira (*"An essential, elevated"*). Usar a voz que a marca já tem
costuma render aprovação mais rápida do que propor uma voz nova.

---

## Detalhes de execução

**Cartão de produto reformatado.** O padrão do Horizon põe título e preço em corpo 16
regular. Mudei para o título em **rótulo caixa alta 12px com tracking aberto** e o preço em
corpo 14 — a hierarquia da referência, onde a foto domina e o texto se comporta.

**Proporção retrato.** `image_ratio` saiu de `adapt` para `portrait`. Com `adapt`, cada card
assume a proporção da própria foto e a grade fica desalinhada — as fotos da ARIA variam de
1478×1971 a 2240×2987. Retrato fixo dá a régua vertical que a referência tem.

**Respiro.** Padding vertical da seção de produtos em 88px (padrão era 48), gap entre
colunas 16 e entre linhas 32. Contenção também é espaço vazio.

**Gradiente, não véu.** A abertura usa `overlay_style: gradient` de baixo para cima com
`#14141459`. Escurece só o pé da imagem, onde o texto se apoia, e deixa o topo da foto
limpo. Véu sólido sobre a imagem inteira achata a foto.

**`section_width` no hero é sobre o texto, não sobre a foto.** O container da mídia é
`section--full-width` fixo no código do Horizon — a imagem sangra sempre, em qualquer
configuração. O ajuste `section_width` governa apenas o `hero__content-wrapper`:
em `page-width` ele recebe `grid-column: 2 / 3` e respeita a calha; em `full-width` ele
encosta na borda da tela. Os três blocos usam `page-width`.

---

## Imagens: a descoberta

A auditoria de 11/08 registrou que faltam fotos. É verdade **nos produtos**, mas não na loja:
a biblioteca de arquivos tem cerca de **15 fotos editoriais em alta resolução** que não estão
atreladas a produto nenhum — `Aria7064`, `Aria7097`, `Aria7135`, `Aria7137`, `Aria7196`,
`Aria7286`, `Aria8046`, `Aria8113`, `Aria8161`, `A2`, entre outras, de 2050 a 2240px de
largura.

O problema real não é ausência de foto: é **foto não distribuída**. As três usadas na home
saíram daí, sem custo e sem espera.

Ficam de fora, deliberadamente: `Gemini_Generated_Image_*.png` e `ChatGPT_Image_*.png`.
São imagens geradas por IA e não entram em vitrine de marca premium.

### O que a biblioteca contém, de fato

Existe uma **campanha fotográfica completa** ali dentro: modelo de terno bege, um golden
retriever e um lulu da pomerânia usando as bandanas ARIA, sobre fundo infinito terracota.
Mais uma série em preto e branco e alguns retratos de produto. Nada disso estava sendo usado.

**Primeira escolha, errada.** A abertura foi para `Aria8161.jpg` só porque era a de maior
resolução. É um macro extremo do logo gravado no couro: bonito como detalhe de acabamento,
sem produto, sem pet e sem contexto. Em tela cheia vira um borrão marrom. Escolher foto por
resolução, sem olhar, não funciona.

**Critério corrigido:** cada imagem foi aberta e avaliada por enquadramento, espaço negativo
para o texto e adequação ao papel do bloco.

| Bloco | Imagem | Por quê |
|---|---|---|
| Abertura | `Aria7137` | Única de proporção larga (1,25:1) que corta bem em tela cheia. Modelo e retriever, ambos com peças ARIA, e fundo vazio no alto à esquerda. |
| Marca | `Aria7097` | Retrato em preto e branco, modelo e lulu com a bandana do monograma. É a foto mais editorial do acervo — e P&B é literalmente a paleta do brief. |
| Tamanhos | `Aria8046` | O cão de costas com a coleira off-white no pescoço, com um campo enorme de fundo vazio. O assunto da foto *é* a coleira no pescoço: casa exatamente com "encontre o tamanho certo". |

---

## Logo no header

O logo vem de `settings.logo` / `settings.logo_inverse` — **ajuste de tema**, portanto
isolado no nosso arquivo e invisível para a loja publicada.

| Ajuste | Valor |
|---|---|
| `logo` | `PNG-Main.png` — versão marrom, a cor primária da marca |
| `logo_inverse` | `PNG-White.png` — para o header sobre foto |
| `logo_height` | 44 (era 36) · mobile 32 |
| `enable_transparent_header_home` | **ligado** |

O logo é uma serifa de alto contraste com a silhueta do cão embutida no "R", e "Pet & Co."
em caixa alta espaçada logo abaixo. Ou seja: a marca **já era** Playfair + rótulo espaçado.
Os tokens de tipografia não impuseram uma direção nova — só alinharam a loja ao logo que
ela já tinha.

O header transparente na home estava desligado, e `home_color_scheme` já vinha em `inverse`.
Ligando o transparente, o header flutua sobre a foto de abertura e o Horizon troca
automaticamente para o logo branco — que é o motivo de existir uma versão branca no acervo.

---

## O que ainda falta na home

- **Foto por cor no cartão de produto** — depende de produção nova.
- **Coleções por porte do pet** — dependem da definição de porte por tamanho.
- **Menu de quatro itens** — hoje são cinco (INICIO, LOJA, SOBRE, CONTATO, ESSENCIAL).
  Não pode ser mexido agora: menu é dado de loja, compartilhado com o tema publicado.
- **Segundo bloco de curadoria** — só faz sentido com mais produtos ativos. Hoje são 5.
- **R$ 201,00 aparecendo na vitrine** — o resíduo de teste apontado na auditoria já está
  visível na home. Correção de catálogo, não de tema.

---

## Onde ver

- **Local, com hot reload:** http://127.0.0.1:9292
- **No domínio da loja:** `https://whksn2-s2.myshopify.com/?preview_theme_id=151334289544`
  (tema de desenvolvimento — exige estar logado como staff)

A loja publicada continua no `Atelier`, intacta.
