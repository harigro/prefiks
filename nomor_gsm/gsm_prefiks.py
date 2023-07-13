# kelas untuk mengenali awal nomor ponsel dan operatornya

class Prefiks:
    def __init__(self, telepon_seluler: str) -> None:
        """
        len(telepon_seluler) > 4
        """
        self.telepon = telepon_seluler
        self.data = dict([("indosat", ['0814','0815','0816','0855','0856','0857','0858']),
                     ("xl", ['0817','0818','0819','0859','0878','0877']),
                     ("axis", ['0838','0837','0831','0832']),
                     ("telkomsel", ['0812','0813','0852','0853','0821','0823','0822','0851']),
                     ("smartfren", ['0881','0882','0883','0884','0885','0886','0887','0888']),
                     ("three", ['0896','0897','0898','0899','0895'])])

    def prefiks(self) -> str:
        for i in self.data:
            for j in self.data[i]:
                if j in self.telepon:
                    return i
                break
