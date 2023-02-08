import math
import random
mx = 1000
mn = -1000

def minimax(depth, idx, maximize, vals, alpha, beta, tardepth):
	if depth == tardepth:
		return values[idx]
	if maximize:
		best = mn
		best = max(minimax(depth+1,idx*2,False,vals,alpha,beta,tardepth),minimax(depth+1,idx*2+1,False,vals,alpha,beta,tardepth))
		if(best < beta):
			alpha = max(alpha, best)
		return best
	else:
		best = mx
		best = min(minimax(depth+1,idx*2,True,vals,alpha,beta,tardepth),minimax(depth+1,idx*2+1,True,vals,alpha,beta,tardepth))
		if(best > alpha):
			beta = min(beta, best)
		return best
		

#if __name__ == "__main__":
values = random.sample(range(1,50),8)
print("Values:",values)
treedepth = math.log(len(values),2)
Result = minimax(0, 0, True, values, mn, mx, treedepth)
print("Result:- ",Result)