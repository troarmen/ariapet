# Remapeamento do Bling após a reestruturação de 31/08/2026

**Loja:** Aria Pet & co (`whksn2-s2` · ariapet.co)
**Motivo:** a Guia e o Porta Saquinho viraram tamanho único. O catálogo saiu de
**49 para 33 SKUs**: 16 apagados e 8 renomeados. A integração casa por SKU, então
o mapeamento no Bling está quebrado.

---

## ⚠️ Fazer o passo 1 antes de qualquer outra coisa

O toggle **"Atualizar o estoque no canal de venda" (Bling → Shopify) está ligado**
no canal `ARIA — Shopify`. O Bling ainda tem a estrutura velha: 53 registros, os
SKUs antigos, e a Guia com 250 unidades no Preto.

A loja hoje tem **635 unidades** que o Bling não conhece. Se a sincronização rodar
antes do remapeamento, o Bling grava os números dele por cima e o trabalho de
31/08 se perde — é exatamente o risco que o [estoque-pre-bling.md](estoque-pre-bling.md)
descreveu antes da primeira integração.

---

## Ordem segura

### 1. Desligar a sincronização de estoque
Canal `ARIA — Shopify` → desligar **"Atualizar o estoque no canal de venda"**.
Só religar no passo 6.

### 2. Excluir no Bling as 16 variações que não existem mais

**Guia** — `AR-LS-BLK-M`, `AR-LS-BLK-G`, `AR-LS-BRW-M`, `AR-LS-BRW-G`,
`AR-LS-OFF-M`, `AR-LS-OFF-G`, `AR-LS-CML-M`, `AR-LS-CML-G`

**Porta Saquinho** — `AR-PB-BLK-M`, `AR-PB-BLK-G`, `AR-PB-CML-M`, `AR-PB-CML-G`,
`AR-PB-OFF-M`, `AR-PB-OFF-G`, `AR-PB-BRW-M`, `AR-PB-BRW-G`

### 3. Renomear os 8 SKUs que sobraram (perderam o sufixo de tamanho)

| Antes | Depois |
|---|---|
| `AR-LS-BLK-S` | `AR-LS-BLK` |
| `AR-LS-BRW-S` | `AR-LS-BRW` |
| `AR-LS-OFF-S` | `AR-LS-OFF` |
| `AR-LS-CML-S` | `AR-LS-CML` |
| `AR-PB-BLK-S` | `AR-PB-BLK` |
| `AR-PB-CML-S` | `AR-PB-CML` |
| `AR-PB-OFF-S` | `AR-PB-OFF` |
| `AR-PB-BRW-S` | `AR-PB-BRW` |

Os produtos-pai da Guia e do Porta Saquinho passam a ter 4 variações cada,
não 12.

### 4. Lançar saldo e peso no Bling

Estado real da loja em 31/08 — o Bling tem de refletir isto antes de voltar a
mandar estoque. O peso é o que gera etiqueta e NF-e corretas.

| SKU | Produto | Variante | Saldo | Peso |
|---|---|---|---|---|
| `AR-HN-BLK-S` | Peitoral | Preto / P | 25 | 161 g |
| `AR-HN-BLK-M` | Peitoral | Preto / M | 15 | 228 g |
| `AR-HN-BLK-G` | Peitoral | Preto / G | 5 | 284 g |
| `AR-HN-CML-S` | Peitoral | Caramelo / P | 25 | 161 g |
| `AR-HN-CML-M` | Peitoral | Caramelo / M | 15 | 228 g |
| `AR-HN-CML-G` | Peitoral | Caramelo / G | 5 | 284 g |
| `AR-HN-OFF-S` | Peitoral | Off White / P | 25 | 161 g |
| `AR-HN-OFF-M` | Peitoral | Off White / M | 15 | 228 g |
| `AR-HN-OFF-G` | Peitoral | Off White / G | 5 | 284 g |
| `AR-HN-BRW-S` | Peitoral | Marrom / P | 25 | 161 g |
| `AR-HN-BRW-M` | Peitoral | Marrom / M | 15 | 228 g |
| `AR-HN-BRW-G` | Peitoral | Marrom / G | 5 | 284 g |
| `AR-CL-BLK-S` | Coleira | P / Preto | 25 | 78 g |
| `AR-CL-CML-S` | Coleira | P / Caramelo | 25 | 78 g |
| `AR-CL-OFF-S` | Coleira | P / Off White | 25 | 78 g |
| `AR-CL-BRW-S` | Coleira | P / Marrom | 25 | 78 g |
| `AR-CL-BLK-M` | Coleira | M / Preto | 15 | 81 g |
| `AR-CL-CML-M` | Coleira | M / Caramelo | 15 | 81 g |
| `AR-CL-OFF-M` | Coleira | M / Off White | 15 | 81 g |
| `AR-CL-BRW-M` | Coleira | M / Marrom | 15 | 81 g |
| `AR-CL-BLK-G` | Coleira | G / Preto | 5 | 104 g |
| `AR-CL-CML-G` | Coleira | G / Caramelo | 5 | 104 g |
| `AR-CL-OFF-G` | Coleira | G / Off White | 5 | 104 g |
| `AR-CL-BRW-G` | Coleira | G / Marrom | 5 | 104 g |
| `AR-LS-BLK` | Guia | Preto | 15 | 168 g |
| `AR-LS-CML` | Guia | Caramelo | 15 | 168 g |
| `AR-LS-OFF` | Guia | Off White | 15 | 168 g |
| `AR-LS-BRW` | Guia | Marrom | 15 | 168 g |
| `AR-PB-BLK` | Porta Saquinho | Preto | 15 | 46 g |
| `AR-PB-CML` | Porta Saquinho | Caramelo | 15 | 46 g |
| `AR-PB-OFF` | Porta Saquinho | Off White | 15 | 46 g |
| `AR-PB-BRW` | Porta Saquinho | Marrom | 15 | 46 g |
| `AR-BD-AUR-OS` | Bandana | tamanho único | 155 | 52 g |

**33 SKUs · 635 unidades.** Os 480 de produtos batem com o controle de produção
da cliente; a Bandana está com 155 contra 104 no controle — confirmar com ela
antes de lançar, o número certo pode ser 104.

### 5. Conferir SKU a SKU
Bling e Shopify têm de ter os mesmos 33 códigos, sem sobra dos dois lados.

### 6. Religar "Atualizar o estoque no canal de venda"

### 7. Conferir pela API
Peço a leitura das 33 variantes e comparo com esta tabela.

---

## Não mexer

Continuam desligados de propósito, como no [estoque-pre-bling.md](estoque-pre-bling.md):
sincronização de status do pedido, rastreamento automático, importação de imagens
e exportação de preços. E os botões manuais "Sincronizar estoque/preços do sistema
na loja virtual" seguem proibidos — os produtos-pai têm preço R$ 0,00 no Bling.
