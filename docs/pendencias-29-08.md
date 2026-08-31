# Pendências — ARIA Pet & Co. · 29/08/2026

Fecha o ciclo aberto no [status-27-08.md](status-27-08.md) e no
[pedido-cliente.md](pedido-cliente.md). O que mudou desde então está no fim.

---

## 1. Bloqueadores de lançamento

### 🔴 O tema não está publicado
`ARIA v1 (GoodySEO)` está **UNPUBLISHED**. A loja roda o `Atelier`.
Home, PDP, guia de tamanhos, parcelamento e amostras de cor não estão no ar.
Além de publicar, faltam subir 7 arquivos alterados que só existem localmente.

### 🔴 Mensuração: nada instalado
GA4, GTM, Meta Pixel e verificação do Search Console: zero ocorrências.
Era o defeito nº 1 do diagnóstico de 11/08 e é o pilar 3 da proposta.
Sem isso não se mede venda, não se faz remarketing e o tráfego pago fica inviável.

### 🔴 Três das quatro políticas em 404
`/policies/terms-of-service`, `/policies/refund-policy` e `/policies/shipping-policy`.
Só a de privacidade responde. As páginas `/pages/troca-e-devolucao` e
`/pages/cuidados` existem e têm texto — falta levar o conteúdo para as políticas
oficiais no admin.

### 🟡 Rodapé legal incompleto
CNPJ **65.911.458/0001-48** recebido em 29/08 e já no rodapé. Faltam **razão
social** e **endereço físico**, também exigidos pelo Decreto 7.962/2013.

### 🔴 Peso irreal em 100% dos produtos
1 kg (padrão do Shopify) no Peitoral, Coleira e Porta Saquinho; 0 kg na Guia e
na Bandana. Frete errado no checkout, etiqueta e NF-e erradas no Bling.
**Trava a homologação com pedido-teste.**

### 🔴 Estoque zerado em 3 dos 5 produtos
Peitoral, Coleira e Porta Saquinho aparecem **esgotados** na loja desde 29/08,
quando o rastreamento foi ligado (pré-requisito do Bling). Antes disso vendiam
sem controle nenhum. Só Guia (250) e Bandana (155) têm saldo.

---

## 2. Depende da cliente

| # | Item | Trava |
|---|---|---|
| 1 | ~~CNPJ~~, razão social e endereço | Conformidade legal, rodapé |
| 2 | Peso real em gramas **e tamanho da embalagem** | Frete, etiqueta, NF-e, homologação |
| 3 | Estoque real das 36 variantes | 3 produtos esgotados na vitrine |
| 4 | Material, composição e ferragens | Ficha técnica na PDP (ela pediu no feedback) |
| 5 | Confirmar parcelamento até 6x sem juros | Bate com o gateway? |
| 6 | Porta Saquinho Preto: R$ 201 ou R$ 200? | Preço divergente nos dois sistemas |
| 7 | Assinatura: "Made to match." ou "Designed for every step"? | Home e página Sobre |
| 8 | Coleções por tipo (atual) ou por porte do pet (proposta pág. 7)? | Navegação do site |

Itens 1 a 4 já constavam do [pedido-cliente.md](pedido-cliente.md) de 21/08 e
nunca foram respondidos.

---

## 3. Nosso lado

| # | Item | Observação |
|---|---|---|
| 1 | Publicar o ARIA v1 | Depois de subir os 7 arquivos locais |
| 2 | Instalar GA4, GTM, Meta Pixel e Search Console | Pilar 3 da proposta |
| 3 | Preencher as 3 políticas no admin | Conteúdo já existe nas páginas |
| 4 | Decidir entre frete fixo de R$ 22 e cotação Frenet | Os dois estão ativos e aparecem juntos no checkout — o cliente escolhe o menor |
| 5 | Vincular a opção "Cor" da Coleira ao metacampo | No admin; é o único produto sem amostras de cor |
| 6 | Traduzir os valores de opção para o `/en` | Hoje o seletor mostra P/M/G enquanto o texto diz "sizes S, M and L" |
| 7 | Mapear situações no Bling e ligar status + rastreio | Última etapa da integração |
| 8 | Conferir o enquadramento dos heros no preview | Percentuais do art direction nunca foram vistos rodando |
| 9 | "Complete o conjunto" usa `related`, não complementares | Ela pediu produtos realmente complementares |

---

## 4. Resolvido desde o status de 27/08

- Feedback da cliente: home, cabeçalho, PDP, página Sobre e rodapé refeitos
- `/en` totalmente traduzido: produtos, coleções, páginas e menu
- Cor "Brown" → "Marrom" nos 5 produtos e nas descrições
- Amostras de cor no Peitoral, Guia e Porta Saquinho
- Filtros removidos da página de acessórios
- Parcelamento 6x implementado (o `payment_terms` nativo não funciona no Brasil)
- Páginas secundárias traduzidas: 404, carrinho, coleções, contato, senha
- Regra morta de enquadramento do hero corrigida
- **49 SKUs cadastrados** e rastreamento de estoque ativo
- **Integração Bling ↔ Shopify concluída** — ver [ops/estoque-pre-bling.md](../ops/estoque-pre-bling.md)
- CNPJ no rodapé: campo "Dados legais" no bloco de copyright, preenchido com
  `CNPJ 65.911.458/0001-48` (falta razão social e endereço)
