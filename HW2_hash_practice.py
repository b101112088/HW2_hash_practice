dictionary={}
with open("hw2_data.txt","r") as file:
    for line in file:
        word=line.strip()
        if word not in dictionary: #還沒出現過這個字
            dictionary[word]=1 #字典中加入這個字，且出現次數為1
        else: #這個字已經出現過
            dictionary[word]+=1 #這個字的出現次數加1
print("總共出現", len(dictionary.keys()),"個不重複的英文字") #字典有幾個keys就是有幾個不同的英文字
print("以下是每個英文字母出現次數")
for i in dictionary:
    print(i,"出現",dictionary[i],"次")
