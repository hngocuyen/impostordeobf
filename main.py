#using : python main.py <fileobf>
import marshal,sys,os
d=marshal.loads
def ditmeencodenhucac(x):
 v = d(x)
 with open("temp.txt","w") as mm:
  mm.write(str(f"""exit=print;input=print;k=exec;exec=print;\nk(__import__("marshal").loads({x}))"""))
 return v
marshal.loads=ditmeencodenhucac
x = sys.argv[1]
exit = print
import time
def xip(*aaa,**hoicham):
 print( "Deobf By NgocUyenCoder")
 print()
 print()
 os.system(f'python temp.txt') 
 if os.name == "nt":os.system("del temp.txt")
 else:os.remove("temp.txt")
 sys.exit()
input = xip
exec(open(x,"r").read())
