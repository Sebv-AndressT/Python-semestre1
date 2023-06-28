superficie1 = 23890
habitantes1 = 1556805
superficie2 = 48583
habitantes2 = 828708
densidad1 = float(habitantes1/superficie1)
densidad2 = float(habitantes2/superficie2)
censo = {
    "id region 1":8,
    "nombre 1":"BioBio",
    "superficie 1 (Km2)":superficie1,
    "habitantes 1":habitantes1,
    "id region 2":10,
    "nombre 2":"los lagos",
    "superficie(km2) 2":superficie2,
    "habitantes 2":habitantes2,
}
print(censo)

censo["densidad 1"] = round(densidad1, 1)
censo["densidad 2"] = round(densidad2, 1)
print(censo)

censo["capital 1"] = ("capitad de region biobio: concepcion")
censo["capital 2"] = ("capital de region los lagos : puerto montt")
print(censo)

censo["comunas 1"] = ("Lota, Lebu, Los Ángeles")
censo["comunas 2"] = ("Castro, Puerto Varas, Purranque")
print(censo)

censo["provincias 1"] = ("Biobío, Arauco, Concepción")
censo["provincias 2"] = ("Osorno, Llanquihue, Chiloé, Palena")
print(censo)

