from pystyle import System, Anime, Colorate, Colors, Write, Center
from pytube import YouTube

ytbascii = """

,---.    ,---..-------.   .-'''-.    
|    \  /    |\  _(`)_ \ /   _   \   
|  ,  \/  ,  || (_ o._)||__/` '.  |  
|  |\_   /|  ||  (_,_) /   .--'  /   
|  _( )_/ |  ||   '-.-' ___'--._ _\  
| (_ o _) |  ||   |    |   |  ( ` )  
|  (_,_)  |  ||   |    |   `-(_{;}_) 
|  |      |  |/   )     \     (_,_)  
'--'      '--'`---'      `-..__.-'   
                                     

"""

ytbascii2 = """

,---.    ,---..-------.   .-'''-.            ______         ,-----.    .--.      .--.,---.   .--.  .---.       ,-----.       ____     ______         .-''-.  .-------.     
|    \  /    |\  _(`)_ \ /   _   \          |    _ `''.   .'  .-,  '.  |  |_     |  ||    \  |  |  | ,_|     .'  .-,  '.   .'  __ `. |    _ `''.   .'_ _   \ |  _ _   \    
|  ,  \/  ,  || (_ o._)||__/` '.  |         | _ | ) _  \ / ,-.|  \ _ \ | _( )_   |  ||  ,  \ |  |,-./  )    / ,-.|  \ _ \ /   '  \  \| _ | ) _  \ / ( ` )   '| ( ' )  |    
|  |\_   /|  ||  (_,_) /   .--'  /          |( ''_'  ) |;  \  '_ /  | :|(_ o _)  |  ||  |\_ \|  |\  '_ '`) ;  \  '_ /  | :|___|  /  ||( ''_'  ) |. (_ o _)  ||(_ o _) /    
|  _( )_/ |  ||   '-.-' ___'--._ _\         | . (_) `. ||  _`,/ \ _/  || (_,_) \ |  ||  _( )_\  | > (_)  ) |  _`,/ \ _/  |   _.-`   || . (_) `. ||  (_,_)___|| (_,_).' __  
| (_ o _) |  ||   |    |   |  ( ` )         |(_    ._) ': (  '\_/ \   ;|  |/    \|  || (_ o _)  |(  .  .-' : (  '\_/ \   ;.'   _    ||(_    ._) ''  \   .---.|  |\ \  |  | 
|  (_,_)  |  ||   |    |   `-(_{;}_)        |  (_.\.' /  \ `"/  \  ) / |  '  /\  `  ||  (_,_)\  | `-'`-'|___\ `"/  \  ) / |  _( )_  ||  (_.\.' /  \  `-'    /|  | \ `'   / 
|  |      |  |/   )     \     (_,_)         |       .'    '. \_/``".'  |    /  \    ||  |    |  |  |        \'. \_/``".'  \ (_ o _) /|       .'    \       / |  |  \    /  
'--'      '--'`---'      `-..__.-'          '-----'`        '-----'    `---'    `---`'--'    '--'  `--------`  '-----'     '.(_,_).' '-----'`       `'-..-'  ''-'   `'-'   
                                                                                                                                                                           

"""


def init():
 System.Clear()
 System.Title("Youtube MP3 Downloader")
 System.Size(200, 50)
 Anime.Fade(text=Center.Center(ytbascii), color=Colors.yellow_to_red, mode=Colorate.Diagonal, enter=True)

def main():
 System.Clear() 
 print('\n'*2)
 print(Colorate.Diagonal(Colors.yellow_to_red, Center.XCenter(ytbascii2)))
 print('\n'*3)

 link = Write.Input("Entrer le lien de la vidéo ->", Colors.yellow_to_red, interval=0.005, input_color=Colors.white)

 video = YouTube(link)
 stream = video.streams.get_audio_only()
 stream.download()


 if not link.strip():
  Colorate.Error("Veuillez inscrire un lien youtube.")
  return

 if link.strip():
    Write.Input("Vidéo Installé avec succes", Colors.yellow_to_red, interval=0.005, input_color=Colors.white) 
    exit()
 print()   


if __name__ == '__main__':
    init()
    while True:
        main()