def afficheTemps(temps0,temps1,temps2,temps3): 

  j = 0
  h = 0
  m = 0
  s = 0

  if temps0 == 0 :
        j = ""
  elif temps0 == 1 :
        j = ""
  else :
        j = "s"


  if temps1 == 0 :
        h = ""
  elif temps1 == 1 :
        h = ""
  else :
        h = "s"


  if temps2 == 0 :
        m = ""
  elif temps2 == 1 :
        m = ""
  else :
        m = "s"


  if temps3 == 0 :
        s = ""
  elif temps3 == 1 :
        s = ""
  else :
        s = "s"
    
  
  return afficheTemps

afficheTemps((1, 0, 14, 23))
print("votre temps correspond à :", temps0,"jour"+j, temps1, "heure"+h, temps2, "minute"+m, temps3, "seconde"+s)