# Tokens de design — ARIA sobre Horizon

**Data:** 21/08/2026
**Arquivo alterado:** `theme/config/settings_data.json`
**Referência:** brief estético da proposta comercial (p. 06)

Tradução do brief da referência para os tokens do tema. Este é o alicerce: tudo que for
construído depois — home, PDP, coleções — herda daqui e fica coerente sozinho.

---

## O ponto de partida era o oposto do briefing

O Horizon de fábrica vem configurado assim:

| Token | Horizon padrão | Conflito com o brief |
|---|---|---|
| Fonte de título | Inter **n7** (bold) | O brief pede **serifa de alto contraste em peso regular** |
| h1 | 56 px | "títulos contidos… o premium vem da contenção, não do tamanho" |
| Raio de botão | 14 px | Editorial premium não tem canto arredondado |
| Raio de selo | 100 px (pílula) | idem |
| `scheme-3` | Verde `#eef1ea` | "nenhuma cor saturada" |
| `scheme-4` | Azul `#e1edf5` | idem |
| Rótulos (h5/h6) | Caixa normal | "rótulos em caixa alta com espaçamento aberto" |

---

## Tipografia

```
Título      Playfair Display n4   serifa de alto contraste, peso REGULAR
Corpo       Inter n4
Rótulo      Inter n4 · CAIXA ALTA · espaçamento aberto
```

Playfair Display é serifa didone de alto contraste — a modulação forte entre traço grosso e
fino é exatamente o que dá o ar editorial da referência. Usada em **n4** e não em bold: é a
diferença entre parecer caro e parecer gritado.

### Escala — contida

| Nível | Antes | Agora | Entrelinha | Tracking | Caixa |
|---|---|---|---|---|---|
| h1 | 56 | **40** | tight | tight | normal |
| h2 | 48 | **32** | tight | tight | normal |
| h3 | 32 | **24** | normal | tight | normal |
| h4 | 24 | **20** | normal | normal | normal |
| h5 | 14 | **12** | loose | **loose** | **CAIXA ALTA** |
| h6 | 12 | **12** | loose | **loose** | **CAIXA ALTA** |
| corpo | 14 | **16** | loose | — | — |

Tracking apertado nos títulos: serifa de alto contraste em corpo grande pede aproximação,
senão as letras boiam. Tracking aberto só nos rótulos, que é onde o brief pede respiro.
Corpo sobe de 14 para 16 — descrição editorial precisa ser lida, não decifrada.

---

## Paleta

> "Preto, branco e um único neutro quente. Nenhuma cor saturada — exatamente a direção
> que a ARIA já escolheu."

| Esquema | Cor | Uso |
|---|---|---|
| `scheme-1` | `#FFFFFF` branco | Padrão |
| `scheme-2` | `#F2EDE6` neutro quente | Seções alternadas, blocos de respiro |
| `scheme-3` | `#E3D9CC` neutro quente médio | Ênfase sem contraste duro *(era verde)* |
| `scheme-4` | `#FAF8F5` off-white quente | Transição suave *(era azul)* |
| `scheme-5` | `#1C1A18` preto quente | Bloco editorial escuro *(era `#333333` cinza frio)* |
| `scheme-6` | transparente | Overlay do hero, tinta clara sobre foto |

Duas decisões que valem explicação:

**A tinta nunca é `#000000`.** Preto puro sobre branco puro vibra na tela e endurece a
serifa. A tinta é `#141414` — preto quente, quase imperceptível como diferença, muito
perceptível como sensação.

**O escuro é `#1C1A18`, não cinza.** O Horizon usava `#333333`, um cinza neutro-frio que
briga com o neutro quente da marca. O novo é preto amarronzado: fica na mesma família da
paleta em vez de introduzir uma sétima cor pela porta dos fundos.

---

## Formas

Todo raio de canto foi zerado. Editorial premium é reto.

| Token | Antes | Agora |
|---|---|---|
| Botão primário e secundário | 14 | **0** |
| Selo (badge) | 100 | **0** |
| Card | 4 | **0** |
| Campo de formulário | 4 | **0** |
| Popover | 14 | **0** |
| Botão de variante | 14 | **0** |
| Amostra de cor (swatch) | 32 | **0** |
| Texto do selo | normal | **CAIXA ALTA** |
| Efeito de hover no card | none | none *(mantido)* |
| Largura da página | narrow | **normal** |

`page_width` sai de `narrow` para `normal` porque o brief pede foto grande. Não fui para
`wide`: em tela grande o layout solta demais e perde a contenção. Seções específicas de
hero podem ir a largura total individualmente, sem mexer no padrão.

---

## Verificação

Renderizado em `http://127.0.0.1:9292`, HTTP 200, zero erro de Liquid:

- `--font-heading--family: "Playfair Display", serif` ✓
- Arquivos servidos: `playfairdisplay_n4`, `n7`, `i4`, `i7` ✓
- Fundos: `#FFFFFF`, `#FAF8F5`, `#F2EDE6`, `#E3D9CC`, `#1C1A18`, transparente ✓
- Tinta de título: apenas `#141414` e branco — nenhum preto puro remanescente ✓

---

## O que ainda não foi feito

Estes tokens são a base, não a vitrine. Continuam pendentes:

- **Conteúdo da home ainda é o padrão do Horizon**, em inglês: "Browse our latest products",
  "Shop all", "View all". A home real depende das fotos da cliente.
- **Estrutura de seções da home** — o brief pede curadoria em blocos curtos de 4 produtos,
  nunca a grade inteira. Hoje está um hero + uma grade de 8.
- **Menu de quatro itens** e coleções por porte do pet: dependem da definição de porte
  (Anexo D do [pedido à cliente](pedido-cliente.md)).
- **Metafields da ficha técnica** — a tabela de medidas ainda não tem onde morar.
- **Nomenclatura das peças** — nome próprio por produto, à la `Aurora by ARIA`.

---

## Como reverter

Backup do estado original em `settings_data.json.bak`, fora do repositório
(no scratchpad da sessão). O script que aplica os tokens é idempotente: roda de novo
sobre o backup e produz o mesmo resultado.
