class Etudiant:
    def __init__(self, nom, numero, note_intra, note_final):
        self.nom = nom
        self.numero = numero
        self.note_intra = note_intra
        self.note_final = note_final

    def moyenne(self):
        return (self.note_intra + self.note_final) / 2

class Classe:
    pass

if __name__ == '__main__':
    etudiant1 = Etudiant('Alice', '1234', 76, 54)
    etudiant2 = Etudiant('Bob', '5678', 87, 65)
    etudiant3 = Etudiant('Carl', '9012', 88, 65)

    print(etudiant1.moyenne())

    ift1004 = Classe()

    print(ift1004)