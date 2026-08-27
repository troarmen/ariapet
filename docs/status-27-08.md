# Status do tema ARIA v1 — 27/08/2026

**Tema auditado:** `ARIA v1 (GoodySEO)` · ID `151345037448` · não publicado
**Método:** leitura do HTML renderizado no preview + Admin API + `theme pull` para diff
**Loja publicada:** continua no `Atelier`, intacta

Auditoria feita depois da rodada de retrabalho do sócio (arquivos alterados em 27/08,
entre 19:58 e 21:10). Substitui a [auditoria de 21/08](auditoria-catalogo.md) no que
diverge.

---

## 1. O que avançou

Comparando com o estado de 21/08. O salto é grande.

### Catálogo reescrito
Todos os produtos ativos foram renomeados para português com foco em busca, e os handles
acompanharam:

| Antes | Agora | Handle |
|---|---|---|
| Harness | Peitoral para Cachorro ARIA | `peitoral-para-cachorro` |
| Collar | Coleira para Cachorro ARIA | `coleira-para-cachorro` |
| Guia | Guia para Cachorro ARIA | `guia-para-cachorro` |
| Poop Bag | Porta Saquinho para Cachorro ARIA | `porta-saquinho-para-cachorro` |
| Aurora By ARIA | Bandana para Cachorro Aurora By ARIA | `bandana-para-cachorro-aurora` |

O `productType` — vazio em 100% dos produtos na auditoria anterior — está preenchido
em todos: Peitoral, Coleira, Guia, Porta Saquinho, Bandana.

### SEO em português: feito, e bem feito
Título e descrição escritos e específicos em **todos** os 5 produtos ativos e nas
**6 coleções**. Amostra:

- `Peitoral para Cachorro com Ajuste Confortável | Aria Pet & Co.`
- `Todos os Acessórios para Cachorro | Aria Pet & Co.`
- `Guia para Cachorro de 230 cm`

Na auditoria de 21/08 isso era zero de sete.

### Fotos finalmente distribuídas
O acervo parado no Files foi para os produtos:

| Produto | Antes | Agora |
|---|---|---|
| Coleira | **1** | **13** |
| Guia | 2 | 10 |
| Porta Saquinho | **1** | **9** |
| Peitoral | 4 | 8 |

### Coleções criadas
De uma (`Página inicial`) para seis, todas com SEO próprio: Acessórios para Cachorro,
Coleiras, Peitorais, Guias, Porta Saquinhos, Bandanas.

### Guia de tamanhos: resolvido
As três tabelas estão completas, com números reais — o defeito "tabela de medidas sem
números" do diagnóstico de 11/08 **está corrigido**:

```
Coleira    P 28–38 · M 34–50 · G 42–62 cm de pescoço · tira 2,0–2,5 cm
Peitoral   pescoço 32–42 / 40–50 / 48–62 · tórax 38–58 / 55–75 / 70–85 cm
Guia 230 × 2,0 cm   ·   Porta saquinho 8 × 5 cm
```

A PDP também traz as medidas: 29 valores no corpo da página.

### Camada técnica de SEO
Quatro snippets novos, escritos à mão:

```
snippets/structured-data.liquid   (268 linhas)
snippets/breadcrumbs.liquid       (131 linhas)
snippets/hero-art-direction.liquid (85 linhas)
snippets/seo-defaults.liquid       (14 linhas)
```

Verificado no HTML renderizado da PDP: `Product`, `Offer`, `availability` e
`BreadcrumbList` presentes. Na home, `Organization`. Canonical correto em todas as páginas.

### Versão em inglês no ar
`/en` responde 200, com navegação traduzida (ACCESSORIES › COLLARS, HARNESSES, LEASHES,
POOP BAG HOLDERS, BANDANAS) e seletor de idioma. O locale `en` está publicado.
`hreflang` implementado com `x-default`, `pt` e `en`.

---

## 2. O que falta

Em ordem de gravidade.

### 🔴 Bloqueadores de lançamento

**1. Mensuração: nada instalado.**
Zero ocorrências de GA4, GTM, Meta Pixel e verificação do Search Console — conferido no
HTML da home e da PDP. Este era o **defeito nº 1 do diagnóstico** e é o pilar 3 da
proposta ("GA4, GTM, Meta Pixel e Search Console instalados"). Sem isso não se mede venda,
não se faz remarketing e não se calcula custo de aquisição. E os adicionais de tráfego
pago, que a proposta condiciona a isso, ficam inviáveis.

**2. Peso irreal em 100% dos produtos.**
Nada mudou desde 21/08:

| Produto | Peso cadastrado |
|---|---|
| Peitoral, Coleira, Porta Saquinho | **1 kg** (padrão do Shopify, 36 variantes) |
| Guia, Bandana | **0 kg** |

Frete calculado errado no checkout e etiqueta errada no Bling. **Trava a homologação com
pedido-teste e NF da semana 6.**

**3. Estoque zerado em 4 dos 5 produtos ativos.**
Só há estoque em Guia preta (250 no total) e Bandana (155). Peitoral, Coleira e Porta
Saquinho estão em **0 em todas as variantes** — e são justamente os que ganharam foto e
SEO. Na prática, a loja divulga o que não pode vender.

**4. Três das quatro políticas ainda em 404.**
Conferido por requisição: `/policies/terms-of-service`, `/policies/refund-policy` e
`/policies/shipping-policy` retornam **404**. Só a de privacidade responde 200. Mesmo
defeito do diagnóstico de 11/08.

**5. CNPJ ausente.**
Nenhuma ocorrência de CNPJ, razão social ou endereço no rodapé. Exigência do
Decreto 7.962/2013.

### 🟡 Escopo contratado ainda aberto

**6. SEO do `/en` não foi traduzido.**

| | Título | Descrição |
|---|---|---|
| Home PT | `Acessórios para Pet com Design Autoral \| Aria Pet & Co.` | escrita |
| Home /en | `Aria Pet & co – Aria Pet & co` | **ausente** |

O título caiu no padrão do tema, duplicado. A proposta promete "versão em inglês em /en,
com hreflang **e SEO traduzido**". O hreflang está feito; o SEO não. O conteúdo dos
produtos também continua em português dentro do `/en`.

**7. SKU ausente em 36 variantes.**
Só Guia (`AR-LS-BLK-S`…) e Bandana (`AR-BD-AUR-OS`) têm SKU. Peitoral, Coleira e Porta
Saquinho estão sem. O padrão da Guia é bom e serve de modelo — falta aplicar.

**8. Nenhum metafield próprio.**
As medidas existem como **texto** na descrição e no guia, não como **dado**. Sem metafield
não há ficha técnica estruturada, não dá para filtrar por medida, e o dado não alimenta
Google Shopping corretamente. Os únicos metafields são os padrão do Shopify e o
`global.title_tag` / `description_tag` gerados pelo SEO.

**9. Tags vazias em todos os produtos.**
Sem tag não se monta coleção automática nem filtro.

### 🔵 Divergências a confirmar

**10. As coleções são por tipo de produto, não por porte do pet.**
Foram criadas Coleiras, Peitorais, Guias, Porta Saquinhos e Bandanas. A proposta (pág. 7)
diz "Coleções organizadas por porte do pet", e o brief estético justifica: *"coleções
organizadas por porte do pet, não por tipo de produto: resolve a dúvida de tamanho antes
da compra"*.

Pode ter sido pedido da cliente na rodada de mudanças — **não estou tratando como erro**,
mas precisa ser uma decisão registrada, não um esquecimento.

**11. `Made to match.` em inglês no meio da home em português.**
Título do segundo bloco da home. Provavelmente intencional como assinatura de marca, mas
destoa do resto da página, que está todo em português.

### ⚪ Não verificável desta conexão

**12. Bling e gateway de pagamento.**
A consulta de apps instalados retorna `access denied` neste acesso. Pix, cartão,
parcelamento e a integração do Bling precisam ser conferidos direto no admin.

---

## 3. Placar contra a proposta (pág. 7)

| Item do escopo | Situação |
|---|---|
| Redesign de home, PDP e coleções | ✅ feito |
| Coleções organizadas por porte do pet | ⚠️ feitas por tipo de produto |
| Produtos reescritos: material, medidas, peso e SKU | ⚠️ texto e medidas sim; **peso e SKU não** |
| Versão em inglês em /en, hreflang e SEO traduzido | ⚠️ /en e hreflang sim; **SEO não** |
| Dados estruturados, títulos e sitemap | ✅ feito |
| GA4, GTM, Meta Pixel e Search Console | ❌ **nada instalado** |
| Pagamento: Pix, cartão e parcelamento | ❓ verificar no admin |
| Bling: pedidos, estoque e nota fiscal | ❓ verificar no admin |
| Homologação: pedido-teste com baixa e NF | ❌ **travada pelo peso e pelo estoque** |
| Políticas, CNPJ e guia de tamanhos | ⚠️ guia ✅ · **políticas e CNPJ ❌** |

---

## 4. Estado do repositório

Rodei `shopify theme pull` do tema `ARIA v1` por cima de `theme/`, com a árvore limpa no
commit `ARIA V1`. O git mostra o que o sócio mudou:

```
16 arquivos modificados, 4 novos
1.371 inserções, 216 remoções
```

Maiores diffs: `templates/index.json` (+936 linhas), `snippets/meta-tags.liquid` (+263),
`templates/product.json` (+188), `sections/footer-group.json` (+125).

**As alterações estão sem commit.** O trabalho dele veio do editor de temas direto na
Shopify, então o repositório era a cópia desatualizada — agora está sincronizado, mas
precisa de commit para virar marco.

Continuam intactos, como deixamos em 22/08: `config/settings_data.json` (tokens de design,
paleta e logo), `sections/header-group.json` e `snippets/header-drawer.liquid` (acordeão
do menu).
