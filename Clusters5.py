#------------------------------------------------
# Author: Alex Tseng
# Purpose: To create a program that can read a 
#		   pdb file and remove residues, 
#		   substrates, and cofactors to make a
#		   cluster for Gaussian.
# Last Updated: April 23, 2018
#------------------------------------------------
# Patch Number: 0.4
# Patch Notes: Remade from Clusters3.py.
#			   Added definitions to shorten
#   		   the length of code.
#------------------------------------------------

pdb_file= input("Please enter the pdb file > \n")
pdb_file_out= input("Please enter/name the output file > \n")

# definitions:
# remove spaces:
def rmspace():
	many_space="  "
	global lines
	while many_space in lines:
		new_temporary_line= lines.split("  ")
		lines= " ".join(new_temporary_line)

# copy the wanted data to the new file:
def copylines():
	rmspace()
	global lines
	atom_identity= str(lines.split(" ")[2])
	atom_identity= atom_identity[:1]
	x_coor= str(lines.split(" ")[5])
	y_coor= str(lines.split(" ")[6])
	z_coor= str(lines.split(" ")[7])
	new_line= atom_identity+" "+x_coor+" "+y_coor+" "+z_coor
	keep_file.write(new_line)
	keep_file.write("\n")

#-------------------------------------------------
#Start of program
number= int(input("How many to copy? (All residues + All substrates + All cofactors) > \n"))
with open(pdb_file) as original_file:
	with open(pdb_file_out, "a+") as keep_file:
		for i in range(number):
			choice= input("What to copy? (Residue/Substrate/Cofactor) > \n")
			choice= choice.lower()
			while not (choice == "residue" or choice == "substrate" or choice == "cofactor"):
				choice= input("What to copy? (Residue/Substrate/Cofactor) > \n")
			identity= input("What is its identity? (Must be abbreviated the same as in the pdb file.) > \n")
			identity= identity.upper()
			if choice == "residue":
				identity_number= input("What is the residue number? > \n")
				identity_number= " "+identity_number+" "
				original_file.seek(0)
				for lines in original_file:
					if identity in lines and identity_number in lines:
						copylines()
			elif choice == "substrate" or choice == "cofactor":
				check= " "+identity+" "
				original_file.seek(0)
				for lines in original_file:
					if check in lines:
						copylines()
