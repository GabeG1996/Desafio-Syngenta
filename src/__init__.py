from pyparsing import *
from my_module import get_cheapest_hotel
from colorama import init, Back, Fore

weekdays = {
    'mon':0, 
    'tues':0, 
    'wed':0, 
    'thur':0, 
    'fri':0,
    'sat':1, 
    'sun':1
}

afiliation = {
    'Regular':0,
    'Rewards':1
}

def main():
    
    init(autoreset=True)
    
    input_shape = Word(alphas) + ':' + Word(nums) + Word(alphas) + Word(nums) + '(' + Word(alphas) + ')' + ',' + Word(nums) + Word(alphas) + Word(nums) + '(' + Word(alphas) + ')' + ',' + Word(nums) + Word(alphas) + Word(nums) + '(' + Word(alphas) + ')'
    
    print('\nEntre com os dados de filiação e datas desejadas. Seguindo o exemplo a seguir:')
    print('\n\t', Back.WHITE+Fore.BLACK+ 'Ex: Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)')
    
    text = input('\nEntrada:')
    
    try:
        data = input_shape.parse_string(text)
    
    except ParseException:
        print('\n\t', Back.RED+'ERRO: texto informado esta fora do padrão exigido. Reescreva e tente novamente.')
    
    else:
        af = afiliation[data[0]]
        days = [weekdays[data[6]], weekdays[data[13]], weekdays[data[20]]]
        
        print('\n\t', Back.GREEN+Fore.BLACK+get_cheapest_hotel(af, days))

if __name__ == "__main__":
    main()