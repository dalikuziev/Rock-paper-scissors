import random as r
import emoji
print("Tosh, qog'oz, qaychi o'yiniga xush kelibsiz!")
you = int(input("Qaysi birini tanlaysiz? iltimos raqam kiriting: tosh(0) qog'oz(1) qaychi(2): "))
komputer = r.randint(0, 2)

if you > 2 or you < 0:
  print("Siz qoidani buzdingiz!")
elif you == 0 and komputer == 2:
  print(f"Siz toshni tanladingiz:\n{emoji.rock}\nkompyuter esa qaychini tanladi:\n{emoji.scissors}\nsiz yutdingiz.")
elif you == 2 and komputer == 0:
  print(f"Siz qaychini tanladingiz:\n{emoji.scissors}\nkompyuter esa toshni tanladi:\n{emoji.rock}\nsiz yutqazdingiz.")
elif you > komputer:
  if you == 1:
    print(f"Siz qog'ozni tanladingiz:\n{emoji.paper}\nkompyuter esa toshni tanladi:\n{emoji.rock}\nsiz yutdingiz.")
  else:
    print(f"Siz qaychini tanladingiz:\n{emoji.scissors}\nkompyuter esa toshni tanladi:\n{emoji.paper}\nsiz yutdingiz.")
elif you < komputer:
  if you == 0:
    print(f"Siz toshni tanladingiz:\n{emoji.rock}\nkompyuter esa qog'ozni tanladi:\n{emoji.paper}\nsiz yutqazdingiz.")
  else:
    print(f"Siz qog'ozni tanladingiz:\n{emoji.paper}\nkompyuter esa qaychini tanladi:\n{emoji.scissors}\nsiz yutqazdingiz.")
elif you == komputer:
  if you == 0:
    print(f"Siz toshni tanladingiz:\n{emoji.rock}\nkompyuter ham toshni tanladi:\n{emoji.rock}\ndurrang.")
  elif you == 1:
    print(f"Siz qog'ozni tanladingiz:\n{emoji.paper}\nkompyuter ham qog'ozni tanladi:\n{emoji.paper}\ndurrang.")
  else:
    print(f"Siz qaychini tanladingiz:\n{emoji.scissors}\nkompyuter ham qaychini tanladi:\n{emoji.scissors}\ndurrang.")
