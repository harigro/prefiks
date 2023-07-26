#! /home/harigro/Documents/gui/aplikasi_basisdata/alat/bin/python3

from faker import Faker
import phonenumbers

class Operator:
    def __init__(self) -> None:
        self.indosat = ['0814','0815','0816','0855','0856','0857','0858']
        self.xl = ['0817','0818','0819','0859','0878','0877']
        self.axis = ['0838','0837','0831','0832']
        self.telkomsel = ['0812','0813','0852','0853','0821','0823','0822','0851']
        self.smartfren = ['0881','0882','0883','0884','0885','0886','0887','0888']
        self.three = ['0896','0897','0898','0899','0895']

        self.indosat_nol = ['814','815','816','855','856','857','858']
        self.xl_nol = ['817','818','819','859','878','877']
        self.axis_nol = ['838','837','831','832']
        self.telkomsel_nol = ['812','813','852','853','821','823','822','851']
        self.smartfren_nol = ['881','882','883','884','885','886','887','888']
        self.three_nol = ['896','897','898','899','895']

class Prefiks:
    def __init__(self, telepon_seluler: str) -> None:
        """
        len(telepon_seluler) > 4
        """
        self.telepon = telepon_seluler
        self.data = dict([("indosat", Operator().indosat),
                     ("xl", Operator().xl),
                     ("axis", Operator().axis),
                     ("telkomsel", Operator().telkomsel),
                     ("smartfren", Operator().smartfren),
                     ("three", Operator().three)])

    def prefiks(self) -> str:
        for i in self.data:
            for j in self.data[i]:
                if j in self.telepon:
                    return i
                break


def telepon(prefiks_nol: str= "812"):
    fake = Faker(locale="id_iD")
    nomor = '{0}{1}'.format(prefiks_nol, fake.msisdn()[5:])
    nomor_seri = phonenumbers.parse(nomor, "ID")
    return phonenumbers.format_number(nomor_seri, phonenumbers.PhoneNumberFormat.NATIONAL)