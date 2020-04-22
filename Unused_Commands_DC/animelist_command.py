import commands.base_command
import requests 
from bs4 import BeautifulSoup 

class Animelist(commands.base_command.BaseCommand):

    def __init__(self):
        description = "Displays a set of anime worth watching. number1 is lower border of list and number2 is higher border of list. Mximum range of displayed titles can be 40"
        params = ["number1","number2"]
        super().__init__(description, params)

    async def handle(self, params, message, client):
        try:
            number1 = int(params[0])
            number2 = int(params[1])
        except ValueError:
            await message.channel.send("Please, provide valid numbers")
            return

        url='https://myanimelist.net/topanime.php?limit=' + str(number1-1)
        animelist = []
      
        #open with GET method 
        resp=requests.get(url) 
        
        #http_respone 200 means OK status 
        if resp.status_code==200: 
            print("Successfully opened the web page")  
        
            # we need a parser,Python built-in HTML parser is enough . 
            soup=BeautifulSoup(resp.text,'html.parser')     
    
            # l is the list which contains all the text i.e news  
            l=soup.find("table",{"class":"top-ranking-table"}) 
        
            #now we want to print only the text part of the anchor. 
            #find all the elements of a, i.e anchor 
            for i in l.findAll("a",{"class":"hoverinfo_trigger fl-l fs14 fw-b"}): 
                animelist.append(i.text)
        else: 
            print("Error") 

        if(number2 > number1 + 40):
            await message.channel.send("**Set of anime to display was too large, please tighten desired anime range.**")
            return
        if(number1<=0 or number2<=0):
            await message.channel.send("**Invalid range of list.**")
            return
        if(number1>number2):
            await message.channel.send("**Wrong order of arguments.**")
            return

        msg = ""
        tmp = number1
        i=0
        while i <= number2 - number1:
            iterator = str(tmp)
            msg += iterator + ". " + animelist[i] + "\n"
            tmp+=1
            i+=1

        await message.channel.send("**"+message.author.mention + "\n"+msg+"**")
        
