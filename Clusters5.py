#------------------------------------------------
# Author: Alex Tseng
# Purpose: To create a program that can read a 
#		   pdb file and remove residues, 
#		   substrates, and cofactors to make a
#		   cluster for Gaussian.
# Last Updated: April 23, 2018
#------------------------------------------------
# Patch Number: 0.5
# Patch Notes: Remade from Clusters4.py.
#			   Creates temporary files before
#			   transfering to new file.
#------------------------------------------------

import tempfile
pdb_file= input("Please enter the pdb file > \n")
pdb_file_out= input("Please enter/name the output file > \n")
natoms= int(0)

# copies all the data from pdb_file and changes it so that everything is now 1 space apart.
temporary= tempfile.TemporaryFile()
with open(pdb_file) as f:
	many_space= "  "
	for lines in f:
		while many_space in lines:
			new_temporary_line= lines.split("  ")
			lines= " ".join(new_temporary_line)
		temporary.write(lines)
# to debug, uncomment this:
#		temporary.read()

# definitions:
# copy the wanted data to the new file:
def copylines(b,c,d):
	if d != "":
		e= b+" "+d
		for lines in temporary:
			if d in lines:
				broken_line= lines.split(" ")
				atom_identity= broken_line[:2]
				x_coor= broken_line[:5]
				y_coor= broken_line[:6]
				z_coor= broken_line[:7]
				new_line= str(atom_identity, x_coor, y_coor, z_coor, "\n")
				keep_file.write(new_line)

			
# user inputs
def user_input():
	a= input("How much to copy? (All residues + All substrates + All cofactors)")
	with open(pdb_file_out, "a+") as keep_file:
	for i in range(a):
		b= input("What to copy? Residue/Substrate/Cofactor > \n")
		b= b.lower()
		c= input("What is its identity? (Must be abbreviated the same as in the pdb file.) > \n")
		if b == "residue":
			d= input("What is the residue number? > \n")

user_input()

