highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(",")
print(highlighted_poems_list)

highlighted_poems_stripped = []
for each in highlighted_poems_list:
  highlighted_poems_stripped.append(each.strip())

print(highlighted_poems_stripped)

highlighted_poems_details = []

for each in highlighted_poems_stripped:
  highlighted_poems_details.append(each.split(':'))

poets = []
titles = []
dates = []

for each in highlighted_poems_details:
  poets.append(each[1])
  titles.append(each[0])
  dates.append(each[2])

for i in range(len(poets)):
  print("The poem {TITLE} was published by {POET} in {DATE}.".format(TITLE=titles[i], POET=poets[i], DATE=dates[i]))
