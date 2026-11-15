def generer_chiffres(base):
    '''
    Cette fonction retourne une chaine contenant tous les chiffres possibles pour une base donnée.
    Par exemple,
       si base est 2, la fonction retourne "01"
       si la base est 10, la fonction retourne "0123456789"
       si la base est 12, la fonction retourne "0123456789AB"
    '''
    chiffres = "0123456789ABCDEF"
    # validons que la base est valide
    assert  2 <= base <= len(chiffres), "generer_chiffres, valeur invalide"
    return chiffres[0:base]

def convertir_de_valeur_decimale_en_chiffre(valeur, base):
    '''
    Cette fonction transforme une valeur en base 10 vers le chiffre équivalent.
    Par exemple,
       1 est transformé en "1"
       10 est transformé en "A" si la base est 11 ou plus
    '''
    chiffres = generer_chiffres(base)
    # validons que la valeur est valide
    assert  0 <= valeur < len(chiffres), "convertir_de_valeur_decimale_en_chiffre, valeur invalide"
    return chiffres[valeur]

def convertir_de_chiffre_en_valeur_decimale(chiffre, base):
    '''
    Cette fonction retourne l'équivalent numérique d'un caractère.
    Par exemple,
       "1" est transformé en 1
       'A' est transformé en 10
    '''
    chiffres = generer_chiffres(base)
    assert chiffre in chiffres, "convertir_de_chiffre_en_valeur_decimale, chiffre invalide"
    # la position du chiffre == sa valeur décimale
    # index retourne l'indice ou la position où se trouve chiffre
    return chiffres.index(chiffre)

def est_valide(valeur, base):
    '''
    Cette fonction valide que la chaine valeur représente bien une valeur numérique.
    Par exemple, 123 en base 4 est valide mais 127 en base 5 ne l'est pas
    Une chaine vide est invalide.
    Elle retourne True ou False
    '''
    valeur=valeur.upper()
    if valeur == "" or valeur == '-' or valeur == '+':
        return False
    chiffres = generer_chiffres(base)
    if valeur[0] == '-' or valeur[0]=='+':
        valeur = valeur[1:]
    for caractere in valeur:
        if caractere not in chiffres:
            return False
    return True

def convertir_en_base_10(valeur, base):
    '''
    Cette fonction convertit une chaine en valeur numérique décimale.
    Elle fait l'équivalent de int(valeur, base) mais vous ne pouvez pas l'utiliser
    valeur est une chaine
    base est un entier
    Elle retourne un entier
    '''
    assert est_valide(valeur, base), "convertir_en_base_10, valeur ou base invalide"
    est_negatif = False
    valeur=valeur.upper()
    if valeur[0] == '-':
        est_negatif = True
        valeur = valeur[1:]
    elif valeur[0] == '+':
        valeur = valeur[1:]
    resultat = 0
    for caractere in valeur:
        valeur_decimale = convertir_de_chiffre_en_valeur_decimale(caractere, base)
        resultat = (resultat * base) + valeur_decimale
    if est_negatif:
        resultat = -resultat
    return resultat

def convertir_de_base_a_base(valeur, base_depart, base_fin):
    '''
    Cette fonction convertit une chaine d'une base en une autre base.
    valeur est une chaine
    base_depart est un entier
    base_fin est un entier
    Elle retourne une sous-chaine qui représente un entier en base base_fin
    '''
    decimale = convertir_en_base_10(valeur, base_depart)
    if decimale == 0:
        return "0"
    est_negatif = False
    if decimale < 0:
        est_negatif = True
        decimale = -decimale
    resultat = ""
    while decimale > 0:
        reste = decimale % base_fin
        chiffre = convertir_de_valeur_decimale_en_chiffre(reste, base_fin)
        resultat = chiffre + resultat
        decimale = decimale // base_fin
    if est_negatif:
        resultat = "-" + resultat
    return resultat

def saisir_entier(instructions, minimum, maximum, message_erreur):
    '''
    Cette fonction permet de saisir une valeur entère qui doit être dans la plage [minimum, maximum].
    instructions est une chaine
    minimum est un entier
    maximum est un entier
    message_erreur est une chaine
    Elle retourne un entier compris entre minimum et maximum
    La fonction doit boucler tant que la valeur est invalide
    '''
    valeur = int(input(instructions))
    while valeur < minimum or valeur > maximum:
        print(message_erreur)
        valeur = int(input(instructions))
    return valeur

def saisir_nombre(base, instructions, message_erreur):
    '''
    Cette fonction permet de saisir une chaine qui représente un entier de base base.
    base est un entier
    instructions est une chaine
    message_erreur est une chaine.
    Elle retourne une chaine qui représente un entier valide par rapport à la base.
    Utilisez est_valide
    La fonction doit boucler tant que la valeur est invalide
    '''
    valeur = input(instructions)
    while not est_valide(valeur, base):
        print(message_erreur)
        valeur = input(instructions)
    return valeur

def additionner(valeur1, valeur2, base):
    '''
    Cette fonction permet d'additionner deux valeurs de base base.
    valeur1 est une chaine représentant un entier de base base
    valeur2 est une chaine représentant un entier de base base
    base est un entier.
    Elle retourne une chaine qui représente un entier valide par rapport à la base.
    '''
    valeur1 = convertir_en_base_10(valeur1, base)
    valeur2 = convertir_en_base_10(valeur2, base)
    somme_decimale = valeur1 + valeur2
    return convertir_de_base_a_base(str(somme_decimale), 10, base)

def soustraire(valeur1, valeur2, base):
    '''
    Cette fonction permet de soustraire deux valeurs de base base (valeur1 - valeur2).
    valeur1 est une chaine représentant un entier de base base
    valeur2 est une chaine représentant un entier de base base
    base est un entier.
    Elle retourne une chaine qui représente un entier valide par rapport à la base.
    '''
    valeur1 = convertir_en_base_10(valeur1, base)
    valeur2 = convertir_en_base_10(valeur2, base)
    soustraction_decimale = valeur1 - valeur2
    return convertir_de_base_a_base(str(soustraction_decimale), 10, base)

def multiplier(valeur1, valeur2, base):
    '''
    Cette fonction permet de multiplier deux valeurs de base base.
    valeur1 est une chaine représentant un entier de base base
    valeur2 est une chaine représentant un entier de base base
    base est un entier.
    Elle retourne une chaine qui représente un entier valide par rapport à la base.
    '''
    valeur1 = convertir_en_base_10(valeur1, base)
    valeur2 = convertir_en_base_10(valeur2, base)
    multiplication_decimale = valeur1 * valeur2
    return convertir_de_base_a_base(str(multiplication_decimale), 10, base)


def diviser_reste(valeur1, valeur2, base):
    '''
    Cette fonction permet de diviser deux valeurs de base base (valeur1 /% valeur2).
    valeur1 est une chaine représentant un entier de base base
    valeur2 est une chaine représentant un entier de base base
    base est un entier.
    Elle retourne deux valeurs (deux chaines) qui représentent des entiers valides par rapport à la base.
    return partie_entière, reste

    Si le dénominateur est 0, veuillez retourner "division par zéro", "0"
    '''
    valeur1 = convertir_en_base_10(valeur1, base)
    valeur2 = convertir_en_base_10(valeur2, base)
    if valeur2 == 0:
        return "division par zéro", "0"
    else:
        division_entiere = valeur1 // valeur2
        reste = valeur1 % valeur2
        return convertir_de_base_a_base(str(division_entiere), 10, base), convertir_de_base_a_base(str(reste), 10, base)

def diviser(valeur1, valeur2, base):
    '''
    Cette fonction permet de diviser deux valeurs de base base (valeur1 / valeur2).
    valeur1 est une chaine représentant un entier de base base
    valeur2 est une chaine représentant un entier de base base
    base est un entier.
    Elle retourne une valeur (une chaine) qui représente un flottant par rapport à la base.

    Si le dénominateur est 0, veuillez retourner "division par zéro"

    diviser("2", "1", 10) doit retourner "2.0" et non 2 ni "2. ni 2.0000"
    '''
    valeur1 = convertir_en_base_10(valeur1, base)
    valeur2 = convertir_en_base_10(valeur2, base)
    if valeur2 == 0:
        return "division par zero"
    if (valeur1<0 and valeur2>0)or(valeur1>0 and valeur2<0):
        valeur1=abs(valeur1)
        valeur2=abs(valeur2)
        division_entiere = valeur1 // valeur2
        reste = valeur1 % valeur2
        resultat = convertir_de_base_a_base(str(division_entiere), 10, base)
        if reste == 0:
            return resultat + '.0'
        else:
            resultat += "."
            for compteur_decimal in range(4):
                if reste == 0:
                    break
                else:
                    reste *= base
                    chiffre_decimale = reste // valeur2
                    reste %= valeur2
                    resultat += convertir_de_valeur_decimale_en_chiffre(chiffre_decimale, base)
        return '-'+resultat
    else:
        division_entiere = valeur1 // valeur2
        reste = valeur1 % valeur2
        resultat = convertir_de_base_a_base(str(division_entiere), 10, base)
        if reste == 0:
            return resultat + '.0'
        else:
            resultat += "."
            for compteur_decimal in range(4):
                if reste == 0:
                    break
                else:
                    reste *= base
                    chiffre_decimale = reste // valeur2
                    reste %= valeur2
                    resultat += convertir_de_valeur_decimale_en_chiffre(chiffre_decimale, base)
        return resultat

def encoder_base64(chaine):
    '''
    Cette fonction permet d'encoder une chaine en base64
    chaine est une chaine.
    Elle retourne une chaine.
    '''
    table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    binaire = ""
    for caractere in chaine:
        bin_caractere = convertir_de_base_a_base(str(ord(caractere)), 10, 2)
        while len(bin_caractere) < 8:
            bin_caractere = "0" + bin_caractere
        binaire += bin_caractere

    while len(binaire) % 6 != 0:
        binaire += "0"

    resultat = ""
    position = 0
    while position < len(binaire):
        morceau = binaire[position: position + 6]
        indice = convertir_en_base_10(morceau, 2)
        resultat += table[indice]
        position += 6

    while len(resultat) % 4 != 0:
        resultat += "="

    return resultat

def decoder_base64(chaine):
    '''
    Cette fonction permet de décoder une chaine encodé en base64
    chaine est une chaine.
    Elle retourne une chaine.
    '''
    table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    chaine_epuree = chaine.replace("=", "")

    binaire = ""
    for caractere in chaine_epuree:
        indice = table.index(caractere)
        bin_indice = convertir_de_base_a_base(str(indice), 10, 2)
        while len(bin_indice) < 6:
            bin_indice = "0" + bin_indice
        binaire += bin_indice

    resultat = ""
    position = 0
    while position + 8 <= len(binaire):
        morceau = binaire[position: position + 8]
        valeur_decimale = convertir_en_base_10(morceau, 2)
        resultat += chr(valeur_decimale)
        position += 8

    return resultat


# on suppose que convertir_de_base_a_base fonctionne correctement
def tester_additionner():
    for base in range(2, 16+1):
        valeur1 = 20 + base
        valeur2 = 15 + 2*base
        reponse1 = valeur1 + valeur2

        # deux valeurs positives
        valeur1 = convertir_de_base_a_base(str(valeur1), 10, base)
        valeur2 = convertir_de_base_a_base(str(valeur2), 10, base)
        reponse1 = convertir_de_base_a_base(str(reponse1), 10, base)
        message_erreur = f"{valeur1} + {valeur2} == {reponse1}, #{base}"
        assert additionner(valeur1, valeur2, base) == reponse1, message_erreur

        # une valeur positive et une négative
        valeur1 = 20 + base
        valeur3 = -(15 + 2*base)
        reponse2 = valeur1 + valeur3
        valeur1 = convertir_de_base_a_base(str(valeur1), 10, base)
        valeur3 = convertir_de_base_a_base(str(valeur3), 10, base)
        reponse2 = convertir_de_base_a_base(str(reponse2), 10, base)
        message_erreur = f"{valeur1} + {valeur3} == {reponse2}, #{base}"
        assert additionner(valeur1, valeur3, base) == reponse2, message_erreur

    # cas particuliers (valeur1, valeur2, base, réponse attendue)
    cas = (("0", "0", 10, "0"),
           ("1", "1", 2, "10"),
           ("FF", "1", 16, "100"),
           ("A", "B", 12, "19"),
           ("-5", "3", 10, "-2"),
           ("-5", "-3", 10, "-8"),
           ("-A", "A", 16, "0"))
    for v1, v2, base, attendu in cas:
        message_erreur = f"{v1} + {v2} == {attendu}, base {base}"
        assert additionner(v1, v2, base) == attendu, message_erreur

def tester_soustraire():
    for base in range(2, 16+1):
        valeur1 = 20 + base
        valeur2 = 15 + 2*base
        reponse1 = valeur1 - valeur2

        # deux valeurs positives
        valeur1 = convertir_de_base_a_base(str(valeur1), 10, base)
        valeur2 = convertir_de_base_a_base(str(valeur2), 10, base)
        reponse1 = convertir_de_base_a_base(str(reponse1), 10, base)
        message_erreur = f"{valeur1} - {valeur2} == {reponse1}, #{base}"
        assert soustraire(valeur1, valeur2, base) == reponse1, message_erreur

        # une valeur positive et une négative
        valeur1 = 20 + base
        valeur3 = -(15 + 2*base)
        reponse2 = valeur1 - valeur3
        valeur1 = convertir_de_base_a_base(str(valeur1), 10, base)
        valeur3 = convertir_de_base_a_base(str(valeur3), 10, base)
        reponse2 = convertir_de_base_a_base(str(reponse2), 10, base)
        message_erreur = f"{valeur1} - {valeur3} == {reponse2}, #{base}"
        assert soustraire(valeur1, valeur3, base) == reponse2, message_erreur

    # cas particuliers (valeur1, valeur2, base, réponse attendue)
    cas = (("0", "0", 2, "0"),
           ("A", "A", 16, "0"),
           ("1", "10", 2, "-1"),
           ("100", "1", 16, "FF"),
           ("5", "-3", 10, "8"),
           ("-5", "-3", 10, "-2"))
    for v1, v2, base, attendu in cas:
        message_erreur = f"{v1} - {v2} == {attendu}, base {base}"
        assert soustraire(v1, v2, base) == attendu, message_erreur

def tester_multiplier():
    for base in range(2, 16+1):
        valeur1 = 20 + base
        valeur2 = 15 + 2*base
        reponse1 = valeur1 * valeur2

        # deux valeurs positives
        valeur1 = convertir_de_base_a_base(str(valeur1), 10, base)
        valeur2 = convertir_de_base_a_base(str(valeur2), 10, base)
        reponse1 = convertir_de_base_a_base(str(reponse1), 10, base)
        message_erreur = f"{valeur1} * {valeur2} == {reponse1}, #{base}"
        assert multiplier(valeur1, valeur2, base) == reponse1, message_erreur

        # une valeur positive et une négative
        valeur1 = 20 + base
        valeur3 = -(15 + 2*base)
        reponse2 = valeur1 * valeur3
        valeur1 = convertir_de_base_a_base(str(valeur1), 10, base)
        valeur3 = convertir_de_base_a_base(str(valeur3), 10, base)
        reponse2 = convertir_de_base_a_base(str(reponse2), 10, base)
        message_erreur = f"{valeur1} * {valeur3} == {reponse2}, #{base}"
        assert multiplier(valeur1, valeur3, base) == reponse2, message_erreur

    # cas particuliers (valeur1, valeur2, base, réponse attendue)
    cas = (("0", "5", 10, "0"),
           ("1", "7", 8, "7"),
           ("11", "11", 2, "1001"),
           ("FF", "FF", 16, "FE01"),
           ("-3", "3", 10, "-9"),
           ("-3", "-3", 10, "9"))
    for v1, v2, base, attendu in cas:
        message_erreur = f"{v1} * {v2} == {attendu}, base {base}"
        assert multiplier(v1, v2, base) == attendu, message_erreur

def tester_diviser_fractionnaire():
    reponses = ['0.1', '0.1111', '0.2', '0.2222', '0.3', '0.3333', '0.4', '0.4444', '0.5', '0.5555', '0.6', '0.6666', '0.7', '0.7777', '0.8']
    for base in range(2, 16+1):
        valeur1 = 1
        valeur2 = 2
        message_erreur = f"{valeur1} / {valeur2} == {reponses[base - 2]}, #{base}"
        # deux valeurs positives
        valeur1 = convertir_de_base_a_base(str(valeur1), 10, base)
        valeur2 = convertir_de_base_a_base(str(valeur2), 10, base)
        assert diviser(valeur1, valeur2, base) == reponses[base - 2], message_erreur

    # cas particuliers (valeur1, valeur2, base, réponse attendue)
    cas = (("2", "1", 10, "2.0"),
           ("7", "1", 10, "7.0"),
           ("1", "4", 10, "0.25"),
           ("1", "3", 10, "0.3333"),
           ("A", "4", 16, "2.8"),
           ("-1", "2", 10, "-0.5"),
           ("-1", "4", 10, "-0.25"),
           ("1", "-4", 10, "-0.25"))
    for v1, v2, base, attendu in cas:
        message_erreur = f"{v1} / {v2} == {attendu}, base {base}"
        assert diviser(v1, v2, base) == attendu, message_erreur

def tester_diviser_avec_reste():
    for base in range(2, 16+1):
        valeur1 = 20 + base
        valeur2 = 15 + 2*base
        reponse1 = (convertir_de_base_a_base(str(valeur1 // valeur2), 10, base),
                    convertir_de_base_a_base(str(valeur1 % valeur2), 10, base))
        # deux valeurs positives
        valeur1 = convertir_de_base_a_base(str(valeur1), 10, base)
        valeur2 = convertir_de_base_a_base(str(valeur2), 10, base)


        message_erreur = f"{valeur1} / {valeur2} == {reponse1}, #{base}"
        assert diviser_reste(valeur1, valeur2, base) == reponse1, message_erreur

        # une valeur positive et une négative
        valeur1 = 20 + base
        valeur3 = -(15 + 2*base)
        reponse2 = (convertir_de_base_a_base(str(valeur1 // valeur3), 10, base),
                    convertir_de_base_a_base(str(valeur1 % valeur3), 10, base))
        valeur1 = convertir_de_base_a_base(str(valeur1), 10, base)
        valeur3 = convertir_de_base_a_base(str(valeur3), 10, base)

        message_erreur = f"{valeur1} / {valeur3} == {reponse2}, #{base}"
        assert diviser_reste(valeur1, valeur3, base) == reponse2, message_erreur

    # cas particuliers (valeur1, valeur2, base, (quotient, reste) attendus)
    cas = (("10", "3", 10, ("3", "1")),
           ("3", "5", 10, ("0", "3")),
           ("5", "5", 10, ("1", "0")),
           ("FF", "10", 16, ("F", "F")),
           ("1010", "11", 2, ("11", "1")))
    for v1, v2, base, attendu in cas:
        message_erreur = f"{v1} /% {v2} == {attendu}, base {base}"
        assert diviser_reste(v1, v2, base) == attendu, message_erreur

def tester_est_valide():
    assert est_valide("ABC", 13), "erreur base 13"
    # est invalide car C n'est pas valide
    assert not est_valide("ABC", 12), "erreur base 12"
    assert est_valide("120", 3), "erreur"
    # est invalide car 3 ne peut pas représenter un chiffre en base 3
    assert not est_valide("123", 3), "erreur base 3"

    # chaine vide
    assert not est_valide("", 10), "erreur chaine vide"
    # valeurs négatives
    assert est_valide("-101", 2), "erreur négatif base 2"
    assert not est_valide("-102", 2), "erreur négatif invalide base 2"
    # minuscules acceptées
    assert est_valide("abc", 16), "erreur minuscules base 16"
    assert est_valide("ff", 16), "erreur minuscules ff base 16"
    # limites de chaque base
    assert est_valide("FF", 16), "erreur FF base 16"
    assert not est_valide("G", 16), "erreur G base 16"
    assert est_valide("9", 10), "erreur 9 base 10"
    assert not est_valide("A", 10), "erreur A base 10"
    assert est_valide("1", 2), "erreur 1 base 2"
    assert not est_valide("2", 2), "erreur 2 base 2"
    # caractères qui ne sont pas des chiffres
    assert not est_valide("12.5", 10), "erreur point"
    assert not est_valide("1 2", 10), "erreur espace"


def tester_convertir_en_base_10():
    bases = (8, 9, 10, 11, 12, 16)
    valeurs = ("111", "111", "111", "111", "111", "ABC")
    reponses = (73, 91, 111, 133, 157, 2748)

    for i in range(len(bases)):
        message_erreur = f"tester_convertir_en_base_10 #{i}"
        # valeur positive
        assert convertir_en_base_10(valeurs[i], bases[i]) == reponses[i], message_erreur
        # valeur négative
        assert convertir_en_base_10("-" + valeurs[i], bases[i]) == -reponses[i], message_erreur

    # cas particuliers (valeur, base, réponse attendue)
    cas = (("0", 2, 0),
           ("0", 16, 0),
           ("-0", 10, 0),
           ("1", 2, 1),
           ("1010", 2, 10),
           ("FF", 16, 255),
           ("ff", 16, 255),
           ("-FF", 16, -255),
           ("777", 8, 511),
           ("10", 16, 16),
           ("10", 2, 2))
    for valeur, base, attendu in cas:
        message_erreur = f"convertir_en_base_10 {valeur} base {base}"
        assert convertir_en_base_10(valeur, base) == attendu, message_erreur

    # un chiffre invalide pour la base doit déclencher une AssertionError
    erreur_levee = False
    try:
        convertir_en_base_10("12", 2)
    except AssertionError:
        erreur_levee = True
    assert erreur_levee, "convertir_en_base_10 devrait refuser '12' en base 2"

def tester_convertir_de_base_a_base():
    bases_de_depart = (8, 9, 10, 11, 12, 16)
    bases_finales = (3, 4, 5, 6, 7, 8)

    valeurs = ("111", "111", "111", "111", "111", "111")
    reponses = ("2201", "1123", "421", "341", "313", "421")

    for i in range(len(bases_de_depart)):
        message_erreur = f"tester_convertir_de_base_a_base {bases_de_depart[i]} {bases_finales[i]} #{i}"
        # valeur positive
        assert convertir_de_base_a_base(valeurs[i], bases_de_depart[i], bases_finales[i]) == reponses[i], message_erreur
        # valeur négative
        assert convertir_de_base_a_base("-"+valeurs[i], bases_de_depart[i], bases_finales[i]) == "-" + reponses[i], message_erreur

    # cas particuliers (valeur, base de départ, base finale, réponse attendue)
    cas = (("0", 10, 2, "0"),
           ("-0", 10, 2, "0"),
           ("0", 2, 16, "0"),
           ("101", 10, 10, "101"),
           ("1010", 2, 10, "10"),
           ("10", 10, 2, "1010"),
           ("255", 10, 16, "FF"),
           ("FF", 16, 10, "255"),
           ("FF", 16, 2, "11111111"),
           ("11111111", 2, 16, "FF"),
           ("ff", 16, 8, "377"),
           ("-255", 10, 16, "-FF"),
           ("-FF", 16, 2, "-11111111"))
    for valeur, depart, fin, attendu in cas:
        message_erreur = f"convertir_de_base_a_base {valeur} {depart} -> {fin}"
        assert convertir_de_base_a_base(valeur, depart, fin) == attendu, message_erreur

    # aller-retour : convertir puis revenir doit redonner la valeur de départ
    for base in range(2, 16+1):
        for nombre in (0, 1, 7, 100, 255, 4096, -42):
            en_base = convertir_de_base_a_base(str(nombre), 10, base)
            assert convertir_de_base_a_base(en_base, base, 10) == str(nombre), \
                f"aller-retour {nombre} base {base}"

def tester_encoder_base64():
    chaines = (
        "Bonjour!!!!",
        "Salut les amis",
        "Au revoir",
        "Que je suis content de vous voir")
    reponses = ("Qm9uam91ciEhISE=",
                "U2FsdXQgbGVzIGFtaXM=",
                "QXUgcmV2b2ly",
                "UXVlIGplIHN1aXMgY29udGVudCBkZSB2b3VzIHZvaXI=")

    for i in range(len(chaines)):
        message_erreur = f"tester_encoder_base64 {chaines[i]} {reponses[i]} #{i}"
        # valeur positive
        assert encoder_base64(chaines[i]) == reponses[i], message_erreur

    # cas particuliers : chaine vide et différents types de padding (=)
    cas = (("", ""),
           ("A", "QQ=="),
           ("AB", "QUI="),
           ("ABC", "QUJD"),
           ("Hello, World!", "SGVsbG8sIFdvcmxkIQ=="),
           ("1234567890", "MTIzNDU2Nzg5MA=="))
    for chaine, attendu in cas:
        message_erreur = f"tester_encoder_base64 '{chaine}' {attendu}"
        assert encoder_base64(chaine) == attendu, message_erreur

def tester_decoder_base64():
    chaines = (
        "Bonjour!!!!",
        "Salut les amis",
        "Au revoir",
        "Que je suis content de vous voir")
    reponses = ("Qm9uam91ciEhISE=",
                "U2FsdXQgbGVzIGFtaXM=",
                "QXUgcmV2b2ly",
                "UXVlIGplIHN1aXMgY29udGVudCBkZSB2b3VzIHZvaXI=")

    for i in range(len(chaines)):
        message_erreur = f"tester_decoder_base64 {chaines[i]} {reponses[i]} #{i}"
        # valeur positive
        assert decoder_base64(reponses[i]) == chaines[i], message_erreur

    # cas particuliers : chaine vide et différents types de padding (=)
    cas = (("", ""),
           ("QQ==", "A"),
           ("QUI=", "AB"),
           ("QUJD", "ABC"),
           ("SGVsbG8sIFdvcmxkIQ==", "Hello, World!"),
           ("MTIzNDU2Nzg5MA==", "1234567890"))
    for chaine, attendu in cas:
        message_erreur = f"tester_decoder_base64 {chaine} '{attendu}'"
        assert decoder_base64(chaine) == attendu, message_erreur

    # aller-retour : encoder puis décoder doit redonner la chaine de départ
    for chaine in ("a", "ab", "abc", "abcd", "Bonjour tout le monde!", "0123456789"):
        message_erreur = f"aller-retour base64 '{chaine}'"
        assert decoder_base64(encoder_base64(chaine)) == chaine, message_erreur

# Exécution de tous les tests
tester_est_valide()
tester_convertir_en_base_10()
tester_convertir_de_base_a_base()
tester_additionner()
tester_soustraire()
tester_multiplier()
tester_diviser_avec_reste()
tester_diviser_fractionnaire()

tester_encoder_base64()
tester_decoder_base64()

while True:
    print("- 1 pour convertir")
    print("- 2 pour la calculatrice")
    print("- 3 pour encoder en base64")
    print("- 4 pour decoder de la base64")
    print("- 5 pour quitter")
    choix = saisir_entier("Votre choix: ", 1, 5, "SVP, saisir une valeur entre 1 et 5")
    match choix:
        case 1:
            base = saisir_entier("Choisir une base (entre 2 et 16): ", 2, 16, "SVP, saisir une base entre 2 et 16")
            valeur = saisir_nombre(base, f"Saisir une valeur en base {base}: ", f"SVP, saisir une valeur en base {base}")
            base_fin = 2
            while base_fin <= 16:
                print(f"{valeur} en base {base} est egal a {convertir_de_base_a_base(valeur, base, base_fin)} en base {base_fin}")
                base_fin += 1
        case 2:
            base = saisir_entier("Choisir une base (entre 2 et 16): ", 2, 16, "SVP, saisir une base entre 2 et 16")
            valeur_1 = saisir_nombre(base, f"Saisir une premiere valeur en base {base}: ", f"SVP, saisir une valeur en base {base}")
            valeur_2 = saisir_nombre(base, f"Saisir une deuxieme valeur en base {base}: ", f"SVP, saisir une valeur en base {base}")
            operation = input("Quelle operation (+, -, *, /, /%): ")
            while operation not in ["+", "-", "*", "/", "/%"]:
                print("SVP, saisir une operation parmi les suivantes: (+, -, *, /, /%)")
                operation = input("Quelle operation (+, -, *, /, /%): ")
            else:
                match operation:
                    case '+':
                        print(f"{valeur_1} + {valeur_2} = {additionner(valeur_1, valeur_2, base)}")
                    case '-':
                        print(f"{valeur_1} - {valeur_2} = {soustraire(valeur_1, valeur_2, base)}")
                    case '*':
                        print(f"{valeur_1} * {valeur_2} = {multiplier(valeur_1, valeur_2, base)}")
                    case '/':
                        print(f"{valeur_1} / {valeur_2} = {diviser(valeur_1, valeur_2, base)}")
                    case '/%':
                        print(f"{valeur_1} /% {valeur_2} = {diviser_reste(valeur_1, valeur_2, base)}")
        case 3:
            chaine_a_encoder = input("Saisir la chaîne à encoder en base64 : ")
            while chaine_a_encoder == "":
                print("SVP, saisir une valeur une valeur valide")
                chaine_a_encoder = input("Saisir la chaîne à encoder en base64 : ")
            resultat_enc = encoder_base64(chaine_a_encoder)
            print(f"Résultat encodé : {resultat_enc}")
        case 4:
            chaine_a_decoder = input("Saisir la chaîne à décoder de la base64 : ")
            while chaine_a_decoder == "":
                print("SVP, saisir une valeur une valeur valide")
                chaine_a_decoder = input("Saisir la chaîne à décoder de la base64 : ")
            resultat_dec = decoder_base64(chaine_a_decoder)
            print(f"Résultat décodé : {resultat_dec}")
        case 5:
            print("Au revoir!!!")
            break