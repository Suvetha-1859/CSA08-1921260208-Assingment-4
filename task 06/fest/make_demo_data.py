import os
os.makedirs("input", exist_ok=True)
files = {
 "CSE.txt": """192311001,Anitha R,CSE,anitha@simats.edu,Dance;Singing
192311002,Karthik S,CSE,karthik@simats.edu,Quiz
192311003,Meena K,CSE,meena.simats.edu,Drama
192311001,Anitha R,CSE,anitha@simats.edu,Dance
""",
 "ECE.txt": """192312001,Rahul V,ECE,rahul@simats.edu,Singing;Quiz
192312002,Divya P,ECE

192312003,Suresh M,ECE,suresh@simats.edu,Dance
""",
 "MECH.txt": """192313001,Arun T,MECH,arun@simats.edu,Drama
192311002,Karthik S,MECH,karthik@simats.edu,Quiz
""",
 "CIVIL.txt": """192314001,Lakshmi N,CIVIL,lakshmi@@simats.edu,Dance
192314002,Vimal D,CIVIL,vimal@simats.edu,Singing;Drama
""",
}
for name, text in files.items():
    with open(os.path.join("input", name), "w", encoding="utf-8") as f:
        f.write(text)
print("demo input files created")
