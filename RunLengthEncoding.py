'''
    Run-Length Encoding:
    Encode string as follows:
    
    Input:  XXXXTTTPPPPPPPPPP
    Output: 4X3T9P1P

    Time: O(N), where N is the number of elements in the input array
    Space: O(N), where N is the number of elements in the input array
    Space (Worst): O(2N) -> O(N), when all characts in array are distinct

    Last Practiced: 2022-03-13 08:42:45
'''

def runLengthEncoding(string):
    currentRunLength = 1
    encodedString = []
    
    for i in range(1,len(string)):
        currentChar = string[i]
        previousChar = string[i-1]
        
        if currentChar != previousChar or currentRunLength == 9:
            encodedString.append(str(currentRunLength))
            encodedString.append(previousChar)
            currentRunLength = 0
        currentRunLength += 1
    
    encodedString.append(str(currentRunLength))
    encodedString.append(string[len(string)-1])
    
    return "".join(encodedString)

print(runLengthEncoding("abcdefghijklmnopqrstuvwxyz"))