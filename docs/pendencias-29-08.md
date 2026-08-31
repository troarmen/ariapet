# Pendências — ARIA Pet & Co. · 29/08/2026

Fecha o ciclo aberto no [status-27-08.md](status-27-08.md) e no
[pedido-cliente.md](pedido-cliente.md). O que mudou desde então está no fim.

---

## 1. Bloqueadores de lançamento

### 🔴 O tema não está publicado
`ARIA v1 (GoodySEO)` está **UNPUBLISHED**. A loja roda o `Atelier`.
Home, PDP, guia de tamanhos, parcelamento e amostras de cor não estão no ar.
Os arquivos já estão todos no tema (31/08) — falta só publicar, o que tem de
ser feito no admin: a Shopify bloqueia publicação de tema via API.

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

### 🟡 Peso resolvido, falta a embalagem
As 49 variantes receberam o peso real em 31/08 (ver seção 4). Falta o
**tamanho da embalagem** — a Frenet cota por peso *e* cubagem, então sem as
dimensões a cotação continua imprecisa. **Ainda trava a homologação.**

### 🔴 Guia com 250 unidades e só 60 produzidas
A Guia está com **100 / 100 / 50 no Preto** e zero nas outras três cores.
O controle de produção diz **60 no total, 15 por cor**. São ~190 unidades
vendáveis a mais do que existe, **numa loja que está no ar**. Número de teste
que ficou. Corrigir tem prioridade sobre publicar o tema.

### 🟡 Porta Saquinho ainda zerado
Aguarda a quebra por tamanho. O controle traz 60 no total, 15 por cor, sem
dizer como dividir entre P, M e G — mesma questão do P/M/G em produto de
medida fixa.

### 🟡 Bandana: 155 na loja, 104 no controle
Sobram 51. Pode ser produção posterior ao documento ou saldo desatualizado.

---

## 2. Depende da cliente

| # | Item | Trava |
|---|---|---|
| 1 | ~~CNPJ~~, razão social e endereço | Conformidade legal, rodapé |
| 2 | ~~Peso real em gramas~~ e tamanho da embalagem | Frete, etiqueta, NF-e, homologação |
| 3 | ~~Estoque de Coleira e Peitoral~~; falta Guia, Porta Saquinho e conferir Bandana | Guia hoje vende 250 com 60 produzidas |
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
| 1 | Publicar o ARIA v1 | Arquivos já subidos; falta o QA no preview e o clique no admin |
| 2 | Instalar GA4, GTM, Meta Pixel e Search Console | Pilar 3 da proposta |
| 3 | Preencher as 3 políticas no admin | Conteúdo já existe nas páginas |
| 4 | Decidir entre frete fixo de R$ 22 e cotação Frenet | Os dois estão ativos e aparecem juntos no checkout — o cliente escolhe o menor |
| 5 | Ligar as opções soltas ao metacampo | Coleira (Cor + Tamanho) e Guia (Tamanho); sem isso não há amostra de cor nem tradução do seletor |
| 6 | ~~Traduzir os valores de opção para o `/en`~~ | Feito nos metaobjects (Black/Brown/Caramel, S/M/L); só aparece nos produtos do item 5 depois que forem ligados |
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
- Tema sincronizado: 9 arquivos no ARIA v1, repositório e tema byte a byte iguais
- **Estoque de Coleira e Peitoral** (31/08), do controle de produção:
  25 (P) / 15 (M) / 5 (G) em cada uma das quatro cores — 180 por produto.
  "Bege"/"Caramel" do controle = **Caramelo** no catálogo.
- **Peso real nas 49 variantes** (31/08), medido na balança pela cliente:

  | Produto | P | M | G |
  |---|---|---|---|
  | Peitoral | 161 g | 228 g | 284 g |
  | Coleira | 78 g | 81 g | 104 g |
  | Guia | 168 g (medida fixa, igual nos três tamanhos) |||
  | Porta Saquinho | 46 g (medida fixa, igual nos três tamanhos) |||
  | Bandana | 52 g (tamanho único) |||

  Peso da peça sem embalagem: o peso do saco/caixa entra uma vez só na
  configuração da Frenet, senão contaria duas vezes.
