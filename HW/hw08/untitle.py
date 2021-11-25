from hw08_data import *
def street_fighter_champ(tutors):
    if len(tutors) == 1:
        return tutors[0]
    def helper(tutors):
        for i in range(len(tutors)):
            if isinstance(tutors[i][0], tuple) == False:
                helper(tutors[i])
            else:
                if tutors[i][0][1] > tutors[i][1][1]:
                    tutors[i] = tutors[i][0]
                elif tutors[i][0][1] == tutors[i][1][1] and tutors[i][0][2] > tutors[i][1][2]:
                    tutors[i] = tutors[i][0]
                else:
                    tutors[i] = tutors[i][1]
            
    while isinstance(tutors[0], list):
            helper(tutors)
            
    if tutors[0][1] > tutors[1][1]:
        tutors = tutors[0]
    elif tutors[0][1] == tutors[1][1] and tutors[0][2] > tutors[1][2]:
        tutors = tutors[0]
    else:
        tutors = tutors[1]       
    return tutors
        
        
tutors1 = [Arda]
tutors2 = [Yuxuan, Arda]
tutors5 = [[[[Yuxuan, Arda],[Etsu, Nabi]],\
[[Wesley, Cecilia],[Aaron, Prem]]], [[[Chase, Sudiksha],[Jonathan, Iman]],\
[[Aragorn, Sauron],[Neo, Morpheus]]]]
tutors3 = [[Yuxuan, Arda],[Etsu, Nabi]]
street_fighter_champ(tutors3)
