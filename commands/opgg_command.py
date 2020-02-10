import commands.base_command
import requests 
from bs4 import BeautifulSoup
from utils import get_emoji

class OPGG(commands.base_command.BaseCommand):

    def __init__(self):
        description = "Displays OPGG info of given summoner (use '_' instead of spaces)"
        params = ["nickname"]
        super().__init__(description, params)

    async def handle(self, params, message, client):
        try:
            nick = str(params[0])
            nick.replace('_','+')
        except ValueError:
            await message.channel.send("Please, provide valid numbers")
            return

        url='https://eune.op.gg/summoner/userName=' + nick

        resp=requests.get(url) 

        #SOLO DUO
        if resp.status_code==200: 
            print("Successfully opened the web page")  
     
            soup=BeautifulSoup(resp.text,'html.parser')     
            l=soup.find("div",{"class":"TierRankInfo"}) 


            SoloDuoRank = []
            LpSoloDuo = []
            SoloDuoWR=""
            for i in l.findAll("div"): 
                SoloDuoRank.append(i.text)
            for j in l.findAll("span"): 
                LpSoloDuo.append(j.text)

            if len(LpSoloDuo) == 0:
                LpSoloDuo.append("Unranked")
                SoloDuoWR="Win Rate -"
            else:
                SoloDuoWR = LpSoloDuo[4]
        else: 
            print("Error")
        
        #FLEX
        if resp.status_code==200: 
     
            soup=BeautifulSoup(resp.text,'html.parser')     
            l=soup.find("div",{"class":"sub-tier"}) 


            FlexRank = []
            FlexLp=""
            FlexWR=""
            for i in l.findAll("div"): 
                FlexRank.append(i.text)

            if len(FlexRank) > 3:
                FlexWR=FlexRank[4].lstrip().rstrip()
                if FlexRank[3][2:3] == "P":
                    FlexLp=FlexRank[3][0:3].strip()
                elif FlexRank[3][3:4] == "P":
                    FlexLp=FlexRank[3][0:4].strip()
                elif FlexRank[3][4:5] == "P":
                    FlexLp=FlexRank[3][0:5].strip()
            else:
                FlexLp="Unranked"
                FlexWR = "Win Rate -"

        #NICKNAME
        if resp.status_code==200: 
     
            soup=BeautifulSoup(resp.text,'html.parser')     
            l=soup.find("div",{"class":"Information"}) 


            Name=""
            for i in l.findAll("span",{"class":"Name"}): 
                Name = i.text


        else: 
            print("Error")


        await message.channel.send(message.author.mention+"\n"+
            get_emoji(":small_orange_diamond:")+f"** Nickname: **" + Name + "\n"+
            get_emoji(":military_medal:")+f"** Solo/Duo Rank: **"+SoloDuoRank[1].strip()+"\t"+
            get_emoji(":gem:")+f"** Points: **" + LpSoloDuo[0].strip()+"\t"+
            get_emoji(":trophy:")+f"** Win Rate: **" + SoloDuoWR[len(SoloDuoWR)-4:len(SoloDuoWR)]+"\n"+
            get_emoji(":military_medal:")+f"** Flex Rank: **" +FlexRank[2].strip()+"\t"+
            get_emoji(":gem:")+f"** Points: **" + FlexLp+"\t"+
            get_emoji(":trophy:")+f"** Win Rate: **" + FlexWR[len(FlexWR)-4:len(FlexWR)]+"\n"
        )