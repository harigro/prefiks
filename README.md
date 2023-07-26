# Prefiks
Pustaka untuk generator nomor telepon berdasarkan prefiks nomor telepon seluler semua operator 
di indonesia

## Cara menggunakan nomor_gsm

```python
from nomor_gsm.gsm_prefiks import Operator, Prefiks, telepon

operator = Operator()
nomor = telepon(operator.xl_nol[0])
pp = Prefiks(nomor)

print("Nomor {0} dan operatornya {1}".format(nomor, pp.prefiks()))
```
