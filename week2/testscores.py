# input 3 test scores then display them and the average score
# no error control needed 
# no checking for valid vaules 
test1 = float(input("input first test score and press enter"))
test2 = float(input("input second test score and press enter"))
test3 = float(input("input third test score and press enter"))

print(" first test score:", test1 , "\n Second test score:" , test2 , "\n third test score", test3 )

avgTest = float((test1 + test2 + test3) / 3)

print("Avg test score:", avgTest)