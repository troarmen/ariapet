# Auditoria de catálogo e conteúdo — ARIA Pet & Co.

**Data:** 21/08/2026
**Fonte:** Shopify Admin API, leitura direta da loja `whksn2-s2.myshopify.com` (www.ariapet.co)
**Escopo:** produtos, variantes, coleções, páginas, políticas e dados cadastrais
**Natureza:** somente leitura — nenhum dado da loja foi alterado

Este documento substitui e detalha o diagnóstico de 11/08 que consta na proposta comercial.
Onde houver divergência, vale o que está aqui.

---

## 1. Panorama

| Item | Estado hoje |
|---|---|
| Produtos | **7** (5 ativos, 2 arquivados) — a proposta prevê até 15 |
| Variantes | 73 |
| Coleções | **1** (`Página inicial`, 4 produtos) |
| Páginas | 5, todas publicadas |
| Políticas legais | **1 de 4** (só privacidade) |
| Idiomas | 1 (`pt-BR`) |
| Mercados | 1 (`Brasil`) |
| Metafields próprios | **0** |

---

## 2. Inventário de produtos

| Produto | Handle | Status | Preço | Variantes | Fotos | SKU | Peso | Estoque |
|---|---|---|---|---|---|---|---|---|
| Harness | `harness` | Ativo | 200,00 | 12 | 4 | ✗ | 1 kg ⚠ | 0 |
| Guia | `leash` | Ativo | 220,00 | 12 | 2 | ✓ | 0 kg ⚠ | 250 |
| Collar | `collar` | Ativo | 220,00 | 12 | **1** | ✗ | 1 kg ⚠ | 0 |
| Poop Bag | `poop-bag` | Ativo | 200–201 | 12 | **1** | ✗ | 1 kg ⚠ | 0 |
| Aurora By ARIA | `aurora-by-aria-1` | Ativo | 280,00 | 1 | 2 | ✓ | 0 kg ⚠ | 155 |
| Aurora By ARIA | `aurora-by-aria` | Arquivado | 200,00 | 12 | 4 | ✗ | 1 kg ⚠ | 0 |
| Khalil By ARIA | `khalil-by-aria` | Arquivado | 200–201 | 12 | 4 | ✗ | 1 kg ⚠ | 0 |

---

## 3. Bloqueadores de venda

Problemas que impedem ou corrompem uma venda real. Prioridade máxima.

### 3.1 A loja praticamente não consegue vender hoje
Das 73 variantes, apenas **4 têm estoque**: `Guia / Preto` nos três tamanhos (100/100/50) e a
`Aurora` ativa (155). Todas as demais estão em **0** — incluindo os quatro produtos ativos
inteiros de Harness, Collar e Poop Bag. Na prática, um visitante que escolher qualquer cor
que não seja o preto da guia não consegue comprar.

### 3.2 Peso incorreto em 100% dos produtos
Nenhum produto tem peso real cadastrado:

- **1 kg** (valor padrão do Shopify, nunca ajustado): Harness, Collar, Poop Bag e os dois arquivados.
  Uma coleira de couro não pesa 1 kg — o frete calculado sai caro demais e a margem é comida no envio.
- **0 kg**: Guia e Aurora. Transportadora pode recusar a cotação ou devolver valor inválido.

Isso afeta o frete no checkout **e** a etiqueta gerada pelo Bling. É correção obrigatória antes do lançamento.

### 3.3 Faltam 3 das 4 políticas legais — e é isso que gera o 404
Só existe a **Política de privacidade**. Não existem `Termos de Serviço`, `Política de reembolso`
nem `Política de envio`.

**Correção ao diagnóstico de 11/08:** os 404 de "Termos de Serviço", "Trocas" e "Envio" não são
links quebrados do tema — são links corretos apontando para políticas que nunca foram escritas.
A página `Troca e Devolução` até existe e está publicada, mas o rodapé aponta para
`/policies/refund-policy`, que não existe. Ou seja: escrever as políticas resolve os três 404 de uma vez.

### 3.4 CNPJ ausente
O endereço da loja está cadastrado no admin (R. Pedro Micheli, 118 — Cipava, Osasco/SP, 06075-180,
tel. 11986928108), mas o campo de razão social está **vazio** e não há CNPJ em lugar nenhum.
O Decreto 7.962/2013 exige CNPJ e endereço físico visíveis no site. Depende da cliente informar.

---

## 4. Problemas de catálogo

### 4.1 Conteúdo em inglês numa loja em português
Cinco produtos têm descrição escrita em inglês (`Elegance and comfort in every detail…`),
e três têm o **título** em inglês: `Harness`, `Collar`, `Poop Bag`. A loja é `pt-BR` e vende
para o Brasil. Só a `Aurora` ativa tem descrição em português bem escrita — é o padrão de
qualidade a seguir para as outras.

A página institucional também está com título em inglês: `Our Story`.

### 4.2 Nomenclatura inconsistente entre produtos
| Produto | Opção 1 | Opção 2 | Cores |
|---|---|---|---|
| Harness | Cor | **Tamanho do acessório** | Preto, Caramelo, Off White, **Brown** |
| Guia | Cor | Tamanho | Preto, **Brown**, Off White, Caramelo |
| Collar | **Tamanho** | **Cor** | Off White, **Brown**, **Black**, **Caramel** |
| Poop Bag | Cor | **Tamanho do acessório** | Preto, Caramelo, Off White, **Brown** |

Três problemas de uma vez: o nome da opção varia (`Tamanho` vs `Tamanho do acessório`),
a ordem das opções está invertida no Collar, e as cores misturam português e inglês —
`Brown` aparece ao lado de `Preto` em todos, e o Collar está inteiramente em inglês.
Isso quebra filtro por cor, quebra a navegação e aparece feio na página de produto.

**Vocabulário a padronizar:** Preto · Caramelo · Off White · Marrom.

### 4.3 Uma foto para doze variantes
`Collar` e `Poop Bag` têm **1 imagem** cada para 12 variantes em 4 cores. `Guia` tem 2.
A referência da proposta (Pagerie) trabalha com 6 a 16 imagens por produto, e a promessa
central é foto por cor. **Isto depende de produção de fotos pela cliente** — é a dependência
externa mais pesada do projeto e precisa começar já.

### 4.4 Duplicidade e produtos órfãos
Existem dois produtos chamados `Aurora By ARIA`: o arquivado (`aurora-by-aria`, 12 variantes,
4 fotos, R$ 200) e o ativo (`aurora-by-aria-1`, variante única, 2 fotos, R$ 280). O handle
sujo com `-1` prejudica a URL. `Khalil By ARIA` está arquivado com descrição idêntica à da
Aurora — texto copiado, não adaptado.

Definir com a cliente: Khalil volta ao catálogo? A Aurora vende por cor/tamanho ou em peça única?

### 4.5 Preços com resíduo de teste
`Poop Bag` e `Khalil` têm variantes a **R$ 201,00** e outras a R$ 200,00 dentro do mesmo produto,
sem diferença de tamanho que justifique. Parece resto de teste de cadastro.

---

## 5. Problemas de SEO e dados estruturados

- **Título e descrição de SEO vazios em 7 de 7 produtos** e na única coleção. O Google está
  usando o título cru do produto — daí "Harness" e "Collar" competirem sem contexto de marca.
- **`productType` vazio em todos os produtos.** Sem isso não há categorização, e o dado
  estruturado de produto fica pobre para o Google Shopping.
- **`tags` vazias em todos.** Sem tags não é possível montar coleção automática por porte.
- **Uma coleção só** (`Página inicial`), sem SEO. A navegação por porte do pet prometida na
  proposta não existe em nenhuma forma ainda.
- **Nenhum metafield próprio.** Os únicos metafields são os padrão do Shopify
  (`material`, `animal-type`, `color-pattern`, `accessory-size`, `fabric`,
  `pet-control-accessory-features`), todos do tipo `list.metaobject_reference`.
  **A tabela de medidas não tem onde morar** — precisamos criar a estrutura de metafields.

---

## 6. O que já está certo

Vale registrar o que não precisa ser tocado:

- **Padrão de SKU do produto `Guia`**: `AR-LS-BLK-S` → marca, tipo, cor, tamanho. É um padrão
  bom e consistente. Serve de modelo para os outros seis produtos.
- **Descrição da `Aurora` ativa**: português correto, tom editorial, com composição e medida
  (`55 × 55 cm, 80% viscose, 20% seda`). É a régua de qualidade para as demais.
- **Nomenclatura `Aurora by ARIA` / `Khalil by ARIA`**: a cliente já acertou o caminho de dar
  nome próprio a cada peça. Falta estender a Harness, Collar, Guia e Poop Bag.
- **Endereço e telefone** cadastrados no admin. Falta só o CNPJ e publicar no site.
- **Paleta de cores** coerente e contida (preto, caramelo, off white, marrom) — exatamente a
  direção neutra que a referência estética pede.

---

## 7. Dependências da cliente

Itens que travam o cronograma e não dependem de nós:

| # | O que precisamos | Trava o quê | Urgência |
|---|---|---|---|
| 1 | **CNPJ e razão social** | Conformidade legal, lançamento | Alta |
| 2 | **Medidas reais** de cada peça, por tamanho | Tabela de medidas, ficha técnica, PDP | Alta |
| 3 | **Peso real** de cada peça | Frete no checkout, etiqueta no Bling | Alta |
| 4 | **Fotos por cor** dos 4 produtos ativos | Vitrine, PDP, promessa central da proposta | Alta — maior prazo |
| 5 | Decisão sobre `Khalil` e sobre a `Aurora` duplicada | Estrutura do catálogo | Média |
| 6 | Definição dos **portes de pet** atendidos por tamanho (P/M/G) | Coleções por porte, navegação | Média |
| 7 | Texto de **trocas, devolução e prazo de envio** | Políticas legais, os três 404 | Média |

---

## 8. Nota de escopo

A proposta prevê **até 15 produtos** reescritos. O catálogo real tem **7** (ou 5, se os
arquivados não voltarem). Há folga confortável dentro do contratado — se a cliente quiser
lançar peças novas junto com o site, cabe no escopo já pago, desde que o material chegue
a tempo.
