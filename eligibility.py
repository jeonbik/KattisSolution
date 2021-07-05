from sys import stdin

num = int(stdin.readline())
for _ in range(num):
  name, post_secondary, D0B,courses = stdin.readline().split()
  ps = post_secondary[0]+ post_secondary[1]+post_secondary[2]+post_secondary[3]
  Db = D0B[0]+D0B[1]+D0B[2]+D0B[3]
  if int(ps) >=2010 or int(Db)>=1991:
    print(name,"eligible")
  elif int(courses) >=41:
    print(name,"ineligible")
  else:
    print(name,"coach petitions")