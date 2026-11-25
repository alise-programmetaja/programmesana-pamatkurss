## Ievade
1. Programma pajautā spēlētājam ievadīt savu vārdu.
2. Programma pajautā spēlētājam ievadīt vienu skaitli no 1 līdz 12.

## Apstrāde
3. Programma izveido vienu slepenu nejaušu skaitli no 1 līdz 12.
4. Programma salīdzina spēlētāja ievadīto skaitli ar vienu slepeno izvēlēto skaitli.
5. Programma piešķir spēlētājam 5 punktus, ja skaitļi sakrīt.
6. Programma piešķir spēlētājam 0 punktus, ja skaitļi nesakrīt.

## Izvade
7. Programma parāda ekrānā spēlētāja vārdu un ziņojumu, vai skaitlis ir uzminēts.
8. Programma parāda ekrānā iegūto summu ar punktu skaitu.





 ## |     mainīgā vārds    |           datu tips                 |                 ko glabā                   |
 ### |   `speletaja_vards`  |              `str`                  |              Spēlētāja vārds               |
 ### |   `minets_skaitlis`  |              `int`                  | Spēlētāja minētais skaitlis (no 1 līdz 12) |
 ### |   `minets_skaitlis`  |              `int`                  | Spēlētāja minētais skaitlis (no 1 līdz 12) |
 ### |   `minets_skaitlis`  |              `int`                  | Spēlētāja minētais skaitlis (no 1 līdz 12) |
 ### | `slepenais_skaitlis` |              `int`                  | Programmas uzģenerētais nejaušais skaitlis |
 ### |       `punkti`       |              `int`                  |       Spēlētāja iegūtais punktu skaits     |

`punkti = 5- abs(slepenais_skaitlis - minets_skaitlis)`

*(Piezīme: funkcija `abs()` aprēķina starpību bez mīnusa zīmes, lai punkti nesanāktu negatīvi, jo tuvāk uzminēts, jo vairāk punktu).*
## Dati
  * **Nāk no `input()`:** `speletaja_vards`, `minets_skaitlis`
  * **Tiek izrēķināts / uzģenerēts programmā:** `slepenais_skaitlis`, `punkti`
