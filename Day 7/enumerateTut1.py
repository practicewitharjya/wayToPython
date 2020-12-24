# numberlist = [1,2,4,6,8,9,60,89]
# for num in numberlist:
#     print(num)

# skillist = ["Python", "Java","C", "HTML"]
# for skil in skillist:
#     print(skil)

# for i in range(1,8):
#     print(i,": Hello")

skillist = ["Python", "Java","C", "HTML"]
enumerateSkil = enumerate(skillist)  #Here start point is by default: 0
print(list(enumerateSkil))

enumerateSkil = enumerate(skillist, 50) #Here start point is 50
print(list(enumerateSkil))