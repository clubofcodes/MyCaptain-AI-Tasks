def str_encode(s):
    #stores output string
    encoding = ""
    i = 0
    while i < len(s):
        #count occurrences of character at index i
        count = 1
        while i+1 < len(s) and s[i]==s[i+1]:
            count = count+1
            i = i+1
        encoding += str(count)+s[i]
        i=i+1
    return encoding

if __name__ == "__main__":
    
    print("Output : ",str_encode(input("Enter Your String : ")))