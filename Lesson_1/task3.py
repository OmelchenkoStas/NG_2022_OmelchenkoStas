inputseconds = int(input())
print(f"{int(inputseconds/60/60/24)}d,{int(inputseconds/60/60%24)}h,{int(inputseconds/60%60)}m,{int(inputseconds%60)}s")