
for i in range(2,21):
    #for j in range(1,10):
     with open(f'multiplication.txt{i}','w') as f:
      for j in range(1,10):
         f.write(f"{i}x{j}={i*j}\n")