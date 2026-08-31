# Retrato do estoque antes da integração com o Bling

**Data:** 29/08/2026 · **Loja:** Aria Pet & co (`whksn2-s2` · ariapet.co)
**Motivo:** o Bling está vazio. Se a sincronização de estoque for ligada antes de
o saldo existir lá, o Bling grava 0 por cima destes números e eles se perdem.
Este arquivo é a cópia de segurança para reconstituir manualmente se isso ocorrer.

Todas as 49 variantes estão com rastreamento de estoque **ativo** e SKU preenchido.

## Saldo diferente de zero — o que há a perder

| SKU | Produto | Variante | Saldo |
|---|---|---|---|
| `AR-LS-BLK-S` | Guia | Preto / P | **100** |
| `AR-LS-BLK-M` | Guia | Preto / M | **100** |
| `AR-LS-BLK-G` | Guia | Preto / G | **50** |
| `AR-BD-AUR-OS` | Bandana | tamanho único | **155** |

**Total: 405 unidades.** Nenhuma outra variante tem saldo.

## Saldo zero (45 variantes)

Peitoral `AR-HN-*`, Coleira `AR-CL-*`, Porta Saquinho `AR-PB-*` — 36 variantes,
todas em 0, rastreamento ligado em 29/08/2026 (antes disso a Shopify não
controlava estoque e os três eram compráveis sem limite).

Guia `AR-LS-BRW-*`, `AR-LS-OFF-*`, `AR-LS-CML-*` — 9 variantes em 0.

## Ordem segura na integração

1. Importar produtos da Shopify para o Bling
2. Conferir se a importação trouxe o saldo das 4 linhas acima
3. Se não trouxe, lançar os 405 no Bling **antes** de ligar a sincronização
4. Só então ativar a sincronização de estoque

Ligar o passo 4 antes do 3 zera a Guia e a Bandana na loja.

---

## Resultado da integração — 29/08/2026

Integração Bling ↔ Shopify concluída. Conferência pela API **depois** de ligar a
sincronização de estoque:

| Verificação | Resultado |
|---|---|
| Guia (`AR-LS-BLK-S/M/G`) | 100 · 100 · 50 — **250 preservadas** |
| Bandana (`AR-BD-AUR-OS`) | **155 preservadas** |
| 49 SKUs | íntegros, nenhum alterado |
| Preços | inalterados |
| Rastreamento de estoque | ativo nos 5 produtos |

Nenhuma escrita indevida do Bling para a loja. O retrato acima continua válido
como referência.

### Estado dos toggles no canal `ARIA — Shopify`

Ligados:
- Integração automática de pedidos
- Atualizar o estoque no canal de venda (Bling → Shopify)
- Data da venda = "Data da venda" (preserva a data fiscal)

Desligados de propósito:
- Sincronize o status do pedido com o sistema — **dispara e-mail ao cliente**;
  só ligar depois de mapear as situações e validar no pedido-teste
- Sincronizar rastreamento automaticamente — ligar junto com o de status
- Importar/exportar imagens — a Shopify é a fonte da verdade das fotos
- Exportação de preços — nunca no sentido Bling → loja

Nunca usar os botões manuais "Sincronizar estoque/preços do sistema na loja
virtual" da tela de Produtos: os produtos-pai têm preço R$ 0,00 no Bling.

### Limpeza feita

Os arquivados `Aurora By ARIA` e `Khalil By ARIA` vieram na importação (26
registros, 24 variações sem código) e foram excluídos. Bling ficou com 53
registros = 4 pais × 13 + Bandana.
