class Aluno:
    Universidade = ("UniGrande")

    def __init__(self, matricula: int, nome: str) -> None:
      self.matricula = matricula
      self.nome = nome
      self.creditos_cursados = 0
      self. mgp = 0.0
    def apresentar(self):
        return f"{self.matricula} - {self.nome}"


Aluno_1 = Aluno(2026001,  "david gheta")
Aluno_2 = Aluno(20260002, "galo cego")


class Professor:
    Universidade = ("UniGrande")

    def __init__(self, matricula: int, nome: str, email, str) -> None:
        self.matricula
        self.nome
        self.email

    def apresentar(self):
        return F"{self.matricula} - {self.nome} - {self.email}"

professor_1 = Professor(20260003,  "Renan barbosa",  "fofinho@gmail.com")

