''' Program for computing the forward kinematics transformation
	matrix, given the values of the DH parameters theta, a, d and
	alpha.

	The program allows 2 choices :
		1. Compute full transformation matrix and get position vector
		2. Compute T {i} to {j}
		3. Compute T {k-1} to {k}
'''
import numpy as np 
np.set_printoptions(precision=2)

def T_k(theta_k, a_k, d_k, alpha_k) :
	T_cur = np.eye(4)
	
	T_cur[0,0] = np.cos(theta_k)
	T_cur[0,1] = -np.cos(alpha_k) * np.sin(theta_k)
	T_cur[0,2] = np.sin(alpha_k) * np.sin(theta_k)
	T_cur[0,3] = a_k * np.cos(theta_k)

	T_cur[1,0] = np.sin(theta_k)
	T_cur[1,1] = np.cos(alpha_k) * np.cos(theta_k)
	T_cur[1,2] = -np.sin(alpha_k) * np.cos(theta_k)
	T_cur[1,3] = a_k * np.sin(theta_k)

	T_cur[2,1] = np.sin(alpha_k) 
	T_cur[2,2] = np.cos(alpha_k)
	T_cur[2,3] = d_k

	return T_cur

def T(theta, a, d, alpha, start, end) :
	T_old = np.eye(4)

	for i in range(start, end):
		T_new = T_k(theta[i], a[i], d[i], alpha[i])
		T_old = np.dot(T_old,T_new)

	return T_old

def main():

	print("\nChoose 1 or 2 : ")
	print("\n\t 1. T {0} to {n}")
	print("\n\t 2. T {i} to {j}")
	print("\n\t 3. T {k-1} to {k}")

	choice = int(raw_input())

	if choice==1 or choice==2:
		print("\nEnter value of theta as : theta1, theta2, etc ")
		theta = raw_input()

		print("\nEnter value of 'a' as : a1, a2, etc ")
		a = raw_input()

		print("\nEnter value of 'd' as : d1, d2, etc ")
		d = raw_input()

		print("\nEnter value of alpha as : alpha1, alpha2, etc ")
		alpha = raw_input()

		theta = theta.split(",")
		a = a.split(",")
		d = d.split(",")
		alpha = alpha.split(",")

		theta = [int(i)*np.pi/180 for i in theta]
		a = [int(i) for i in a]
		d = [int(i) for i in d]
		alpha = [int(i)*np.pi/180 for i in alpha]

		if choice==1 :
			T_mat = T(theta, a, d, alpha, 0, len(theta))

			print("\nThe transformation matrix is given as T = {}".format(T_mat))
			print("\nThe position coordinate is given as P = {}".format(T_mat[:-1, -1]))
			print("\nOrientation relative to the base of the manipulator R = {}".format(T_mat[:-1, :-1]))

		else :
			print("\nEnter the value of i (0 to n-1):")
			i = int(raw_input())

			print("\nEnter the value of j (1 to n) :")
			j = int(raw_input())

			T_mat = T(theta, a, d, alpha, i, j)

			print("\nThe transformation matrix is given as T = {}".format(T_mat))
			print("\nThe position coordinate is given as P = {}".format(T_mat[:-1, -1]))
			print("\nOrientation relative to the base of the manipulator R = {}".format(T_mat[:-1, :-1]))

	elif choice==3:
		print("\nEnter the value of theta_k (degrees) :")
		theta = int(raw_input())*np.pi/180

		print("\nEnter the value of 'a_k' :")
		a = float(raw_input())

		print("\nEnter the value of 'd_k' :")
		d = float(raw_input())

		print("\nEnter the value of alpha_k (degrees) :")
		alpha = int(raw_input())*np.pi/180

		T_mat = T_k(theta, a, d, alpha)

		print("\nThe transformation matrix is given as T = {}".format(T_mat))

		print("\nThe position coordinate is given as P = {}".format(T_mat[:-1, -1]))
		print("\nOrientation relative to the base of the manipulator R = {}".format(T_mat[:-1, :-1]))

	else :
		print("\n\n\t\tWrong value of choice!!!!!!")		
main()








