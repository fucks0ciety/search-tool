import os
import time

SEARCH = """
                                                                                                                  ?????         
         SSSSSS      EEEEEEEE        AAAAAAA        RRRRRRRRRRR          CCCCCCCCC      HHHHH      HHHHH         ????????       
        SSSS SSSS    EEEEEEEE       AAAAAAAAA       RRRRRRRRRRRR        CCCCCCCCCCC     HHHHH      HHHHH        ???   ????      
       SSSS   SSSS   EEE            AAAAAAAAA       RRRR    RRRR       CCCC     CCCC    HHHHH      HHHHH       ???     ????     
       SSSS          EEE           AAAA   AAAA      RRRR     RRRR     CCCC       CCCC   HHHHH      HHHHH       ???    ????      
        SSSS         EEEEEEEE      AAAA   AAAA      RRRR     RRRR    CCCC               HHHHHHHHHHHHHHHH              ????          
          SSSS       EEEEEEEE     AAAA     AAAA     RRRRRRRRRRR      CCCC               HHHHHHHHHHHHHHHH             ????       
            SSSS     EEEEEEEE     AAAAAAAAAAAAA     RRRRRRRRR        CCCC               HHHHHHHHHHHHHHHH           ????         
             SSSS    EEE         AAAAAAAAAAAAAAA    RRRR   RRRR      CCCC        CCCC   HHHHH      HHHHH          ????          
       SSSS   SSSS   EEE         AAAA       AAAA    RRRR    RRRR      CCCC      CCCC    HHHHH      HHHHH                        
        SSSS SSSS    EEEEEEEE   AAAA         AAAA   RRRR    RRRR       CCCCCCCCCCCC     HHHHH      HHHHH         @@@            
         SSSSSS      EEEEEEEE   AAAA         AAAA   RRRR     RRRR       CCCCCCCCCC      HHHHH      HHHHH         @@@     

VERSION: 1.0

"""


def print_ascii():
    for line in SEARCH.splitlines():
        print(line)
        time.sleep(0.05)

def search_file():
    file = input("\nfile name \n>")
    word = input("word for search \n>")
    count = 0
    count_words = 0

    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                count += 1
                if word in line:
                    count_words +=1
                    print(f"line:{count} -> {line}", end="")
            print(f"all:{count_words}")
    except Exception as e:
        print(f"error: {e}")
    

def main():
    print_ascii()
    search_file()

if __name__ == "__main__":
    main()
