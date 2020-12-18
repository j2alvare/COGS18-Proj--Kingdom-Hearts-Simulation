"""Classes used throughout project"""
class LetsPlay():
    """Displays the user's data as a dictionary pair.
    
    Parameters
    ---------
    username: str
    password: str
    volue: str
    status: str
    display: str
    
    """
    def __init__(self,username,password,volume,status,display,start):
        self.username = username
        self.password = password
        self.volume = volume
        self.status = status
        self.display = display
        self.start = start
        
    def display(username, password, volume, status, display):
        game_data = {'User:': username,
                     'Password:': password,
                     'Edition:': volume,
                     'Status:' : status,
                     'Show game data?:': display  
        }
        
        for key,value in game_data.items():
    
            print(key,value)
        
        return display

    
    def begin_game(start):
    
        if start == 'Begin':
            print('Welcome to Kingdom Hearts!') 
        else:
            print('Cannot Start')