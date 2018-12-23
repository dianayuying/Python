"""
There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollars bill. A ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to each person and give the change if he initially has no money and sells the tickets strictly in the order people follow in the line?

Return YES, if Vasya can sell a ticket to each person and give the change with the bills he has at hand at that moment. Otherwise return NO.
"""
def tickets(people):
    m25, m50 = 0,0
    result = "YES"
    for i in people:
        if i==25: m25+=1
        elif i==50:
            if m25==0:
                result="NO"
                break
            else:
                m50+=1
                m25-=1
        elif i==100:
            if m25==0:
                result="NO"
                break
            elif m50==0:
                if m25<3:
                    result="NO"
                    break
                else:
                    m25-=3
            else:
                if m50>0:
                    m50-=1
                    m25-=1
                else:
                    m25-=3
        else:
            result="NO"
            break
    
    return result
