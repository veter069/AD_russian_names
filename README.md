# AD_russian_names
![image](https://github.com/veter069/AD_russian_names/assets/4894034/e313cc25-92d2-40da-ad10-e3d6fb9c51fc)
Хороший человек с канала https://t.me/pathsecure сделал транслитерацию словарю https://github.com/sorokinpf/russian_names/blob/master/russian_surnames.txt. В ходе тестирования было выявлено, что в инфраструктуре для AD используются логины по маске "IvanovII" фамилия полностью и 1е символы имени и отчества. Скриптом gener.py https://github.com/veter069/AD_russian_names добавлены 2 буквы английского алфавита во всех возможных комбинациях, к списку фамилий на латинице. В результате перебора имен с Kebrute имеем 450+ действительных логина для спрея паролей.
