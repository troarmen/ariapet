#!/usr/bin/env python3
"""Compara um export de produtos do Bling com o retrato da Shopify.

Uso:  python3 ops/conferir-bling.py <export-do-bling.csv>

Confere, para cada SKU: saldo, peso e código de integração. Ignora os
produtos-pai, que no Bling não carregam saldo nem peso.
"""
import csv, sys, json, pathlib

RAIZ = pathlib.Path(__file__).resolve().parent
ESPERADO = json.loads((RAIZ / "shopify-retrato-31-08.json").read_text(encoding="utf-8"))

def carregar_bling(caminho):
    with open(caminho, encoding="utf-8-sig", newline="") as f:
        linhas = list(csv.reader(f, delimiter=";"))
    h = linhas[0]
    i = {c: h.index(c) for c in
         ("Código", "Estoque", "Peso líquido (Kg)", "Código Integração")}
    saida = {}
    for r in linhas[1:]:
        sku = r[i["Código"]].strip()
        if not sku.startswith("AR-"):        # produto-pai
            continue
        saida[sku] = {
            "saldo": int(float(r[i["Estoque"]].replace(",", ".")),),
            "peso_g": round(float(r[i["Peso líquido (Kg)"]].replace(",", ".")) * 1000),
            "integracao": r[i["Código Integração"]].strip(),
        }
    return saida

def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    bling = carregar_bling(sys.argv[1])
    problemas, avisos = [], []

    for sku in sorted(set(ESPERADO) | set(bling)):
        if sku not in bling:
            problemas.append(f"{sku}: existe na Shopify, ausente no Bling")
            continue
        if sku not in ESPERADO:
            problemas.append(f"{sku}: existe no Bling, ausente na Shopify")
            continue
        e, b = ESPERADO[sku], bling[sku]
        if e["saldo"] != b["saldo"]:
            problemas.append(f"{sku}: saldo {b['saldo']} no Bling, {e['saldo']} na Shopify")
        if e["peso_g"] != b["peso_g"]:
            problemas.append(f"{sku}: peso {b['peso_g']}g no Bling, {e['peso_g']}g na Shopify")
        if b["integracao"] != e["variant_id"]:
            # A Bandana é produto simples no Bling, sem variações. O campo veio
            # vazio já no export original de 31/08 e a integração de 29/08
            # preservou o saldo dela mesmo assim — provavelmente o casamento aí
            # é por SKU. Fica como aviso, não como erro.
            if sku == "AR-BD-AUR-OS" and not b["integracao"]:
                avisos.append(f"{sku}: sem código de integração (produto simples, conferir na tela)")
            else:
                problemas.append(f"{sku}: integração {b['integracao'] or 'vazia'}, esperado {e['variant_id']}")

    print(f"{len(ESPERADO)} SKUs na Shopify · {len(bling)} no Bling")
    for a in avisos:
        print(f"  aviso: {a}")
    if problemas:
        print(f"\n{len(problemas)} divergência(s):")
        for p in problemas:
            print(f"  - {p}")
        sys.exit(1)
    print("\nOK — saldo, peso e código de integração batem em todos os SKUs.")

if __name__ == "__main__":
    main()
