import random
import requests
import string

# list of 482 different names
names = [
  "Josefine", "Wioleta", "Solfrid", "Albert", "Erika", "Anabella", "Tatiana",
  "Augustyna", "Dennis", "Oskar", "Alexander", "Mareike", "Erika", "Beulah",
  "Emilio", "Farrell", "Onyx", "Deryck", "Róża", "Montague", "Otto", "Audrea",
  "Ângelo", "Niclas", "Arlie", "Sverre", "Amalia", "Helga", "Andrea",
  "Lillian", "Brand", "Delores", "Sylvia", "Nettie", "Kip", "Tora", "Arvid",
  "Colomba", "Seven", "Ginevra", "Storm", "Mabelle", "Adorján", "Etel",
  "Ireneusz", "Lavender", "Wilfreda", "Birdie", "Hall", "Maurizia", "Bishop",
  "Marvyn", "Leontina", "Sebastiana", "Jacenty", "Mari", "Jolyon", "Anneka",
  "Mack", "Mauro", "Sullivan", "Esko", "Robert", "Nichola", "Lynette",
  "Justice", "Manu", "Natalia", "Karolina", "Frans", "Melva", "Glória",
  "Ambrogio", "Adelle", "Julius", "Monica", "Väinö", "Kristin", "Dayton",
  "Tim", "Dione", "Teodor", "Markus", "Mccann", "Christopher", "Hammond",
  "Mariam", "Rogers", "Karim", "Reyes", "Cade", "Gates", "Callum", "Connolly",
  "Connie", "Pham", "Rory", "Haines", "Bianca", "Valdez", "Karol", "Gentry",
  "Josiah", "Santiago", "Emily", "Reid", "Nathan", "Fernandez", "Patricia",
  "Bridges", "Cai", "Dejesus", "Randy", "Slater", "Diane", "Decker",
  "Cordelia", "O'Brien", "Aliyah", "Bishop", "Shannon", "Coleman", "Grace",
  "Knowles", "Julie", "Dixon", "Tabitha", "Pope", "Cecily", "Gay", "Cormac",
  "Hobbs", "Priya", "Herrera", "Kate", "Adams", "Cameron", "Obrien", "Rahul",
  "Macias", "Amira", "Sanders", "Zohaib", "Giles", "Lili", "Mejia", "Alan",
  "Alvarez", "Tammy", "Tran", "Dan", "Carlson", "Nellie", "Raymond", "Harmony",
  "Levy", "Kimberley", "Gonzales", "Yash", "Townsend", "Aston", "Nixon",
  "Jenson", "Knox", "Salma", "Webster", "Luc", "Booth", "Cheryl", "Dunn",
  "Dhruv", "Potter", "Abu", "Gallegos", "Everly", "Chapman", "Myles",
  "Montgomery", "Lawrence", "Petersen", "Fynn", "Ware", "Virgil", "Soto",
  "Whitney", "Boyd", "Nelson", "Knapp", "Harriett", "Archer", "Lloyd",
  "Robertson", "Roseanna", "Blanchard", "Tilly", "King", "Safwan", "Weeks",
  "Lucille", "Hendricks", "Alexandra", "Bowen", "Olive", "Shaw", "Lina",
  "Morrow", "Donna", "Mcgrath", "Ronald", "Joyce", "Angela", "Phillips",
  "Bill", "O'Moore", "Roy", "Lane", "Caleb", "Jennings", "Maja", "Sheppard",
  "Ahmed", "Pena", "Honey", "Silva", "Tessa", "Stark", "Marjorie", "Johnson",
  "Faris", "Escobar", "Malachi", "Flynn", "Seren", "Mack", "Wendy", "Marquez",
  "Archie", "Suarez", "Tasneem", "Osborne", "Remi", "Hart", "Sid", "Gomez",
  "Trey", "Mckee", "Anisa", "Wright", "Asad", "Mckenzie", "Marco", "Mcclure",
  "Yuvraj", "Estes", "Keira", "Burgess", "Brian", "Bush", "Maximilian", "Love",
  "Coral", "Schwartz", "Maximus", "Lambert", "Filip", "Leon", "Carys", "Ali",
  "Mary", "Daniel", "Bronte", "Holland", "Marnie", "Blankenship", "Faizan",
  "Ayers", "Kingsley", "Perry", "Johnny", "Sloan", "Wilma", "Salazar", "Macy",
  "Craig", "Anas", "Cox", "Abdirahman", "Shaw", "Ameer", "Fox", "Zachariah",
  "Lawson", "Juliet", "Mueller", "Zoya", "Parks", "Ruben", "Best", "Robyn",
  "Preston", "Gloria", "Johnston", "Aishah", "Wood", "Gemma", "Boyd", "Sylvie",
  "Buchanan", "Aidan", "Montes", "Mahdi", "Cain", "Catrin", "Eaton", "Jonah",
  "Aguilar", "Anton", "Cummings", "Clara", "Wilcox", "Jason", "Valentine",
  "Harley", "Valdez", "Cassandra", "Hensley", "Thalia", "Fleming", "Krish",
  "Bartlett", "Deborah", "Chase", "Joanne", "Macias", "Bartosz", "Odonnell",
  "Euan", "Khan", "Stanley", "Sherman", "Oscar", "Bernard", "Scarlet",
  "Dunlap", "Lana", "Cantrell", "Ada", "Ponce", "Dante", "Kelly", "Ben",
  "Wheeler", "Duncan", "Stuart", "Daniella", "Mcpherson", "Hazel", "Leon",
  "Jaden", "Lucas", "Mila", "Knight", "Aryan", "Rowe", "Theo", "Curtis",
  "Trey", "Swanson", "Kaan", "Vega", "Erik", "Peterson", "Reid", "Jefferson",
  "Amie", "Sheppard", "Neve", "Jacobs", "Felicity", "Tran", "Leighton",
  "Dillon", "Hari", "Pennington", "Anjali", "Cisneros", "Estelle", "Castro",
  "Ameera", "Simon", "Kaitlyn", "Christensen", "Autumn", "Owen", "Drew",
  "Hewitt", "Claude", "Martinez", "Carlos", "Aguirre", "Mustafa", "Cline",
  "Lilly", "Terry", "Kareem", "Avila", "Rose", "Burke", "Marie", "Carson",
  "Ria", "Gates", "Finnian", "Merrill", "Harriet", "Hardy", "Belle",
  "Petersen", "Livia", "Dunn", "Zara", "Myers", "Liberty", "Mcknight", "Aoife",
  "Clay", "Stevie", "Moon", "Nathan", "Chen", "Nicole", "Lloyd", "Nellie",
  "Lowery", "Sumayyah", "Rasmussen", "Elmer", "Horn", "Louise", "Oconnor",
  "Calum", "Dyer", "Jermaine", "Chapman", "Luisa", "Barrett", "Allen",
  "Jackson", "Nataniel", "Carr", "Faizan", "Lynn", "Kristian", "Steele",
  "Alexandre", "Mcclain", "Chantelle", "Stafford", "Mia", "Rhodes", "April",
  "Rocha", "Beau", "Kidd", "Leland", "Holman", "Brett", "Bradley", "Sadia",
  "Gallegos", "Rhys", "Prince", "Allan", "Clements", "Ayrton", "Kramer",
  "Gabriel", "Mata", "Rafferty", "Griffith", "Dennis", "Turner"
]

# random mail endings
mail = [
  "@yandex.com", "@gmail.com", "@live.com", "@outlook.com", "@yahoo.com",
  "@aol.com", "@protonmail.com", "gmail.se", "@live.se", "@outlook.se",
  "@yahoo.se"
]


# generate random email address
def generate_email():
  return random.choice(names) + "." + random.choice(names) + random.choice(
    mail)


# generate random password
def generate_password():
  return ''.join(
    random.choice(string.ascii_letters + string.digits) for i in range(10))


# send 10000 post requests
for i in range(10000):
  data = {"userName": generate_email(), "password": generate_password()}
  response = requests.post("https://example.com", data=data)
  # print(response.status_code)

  print(data)
