from itertools import combinations

kevin_likes = {"Halsey", "Taylor Swift", "Mitski", "Joji", 
"Shawn Mendes", "Sabrina Carpenter", "Nicky Minaj", 
"Conan Gray", "One Direction", "Justin Bieber"}

stuart_likes = {"Kendrick Lamar", "Steve Lacy", "Tyler the Creator", 
"Joji", "TheWeeknd", "Coldplay", "Kanye West", 
"Travis Scott", "Frank Ocean", "Brent Faiyaz"}

bob_likes ={"Conan Gray", "Joji", "Dove Cameron", "Mitski", 
"Arctic Monkeys", "Steve Lacy", "Kendrick Lamar", 
"Isabel LaRosa", "Shawn Mendes", "Coldplay"}

edith_likes = {"Metallica", "Billie Eilish", "TheWeeknd", "Mitski", 
"NF", "Conan Gray", "Kendrick Lamar", "Nicky Minaj", 
"Kanye West", "Coldplay"}

DJs = [
    ('Kevin', kevin_likes), ('Stuart', stuart_likes),
    ('Bob', bob_likes), ('Edith', edith_likes)
]

def overlap_cal(set1,set2):
    common = set1 & set2
    overlap1 = len(common)/len(set1)
    overlap2 = len(common)/len(set2)
    return overlap1, overlap2

pairs= list(combinations(DJs,2))

satisfying_pairs = []

for(dj1, set1), (dj2, set2) in pairs:
    overlap1, overlap2 = overlap_cal(set1,set2)
    if overlap1 >= 0.3 and overlap2>= 0.3:
        overlap = (overlap1 + overlap2)/2
        satisfying_pairs.append(((dj1,dj2), overlap))       

for(dj1,dj2), overlap in satisfying_pairs:
    print(f'{dj1} and {dj2} have an total overlap of {overlap*100:.2f}%')
