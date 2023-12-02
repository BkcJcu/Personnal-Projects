

while True:
    mot = input("Veuillez rentrer un mot : ")

    def est_palindrome(mot):
        palindrome = False
        motinversee = ""
        for i in range((len(mot) - 1), -1, -1):
            print(i)
            motinversee += mot[i]
        
        print(motinversee)
        if motinversee == mot:
            palindrome = True
        else :
            pass
        return palindrome

    
    print(est_palindrome(mot))


""" version simplifiée

def est_palindrome(mot):
mot_inversee = ""
for i in range(len(mot) - 1, -1, -1):
    mot_inversee += mot[i]

return mot_inversee == mot

while True:
    mot = input("Veuillez rentrer un mot : ")
    print(est_palindrome(mot))

    
    
    
"""