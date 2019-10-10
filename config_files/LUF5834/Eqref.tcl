# open VMD in correct folder with this command:
# vmd -e Eqref.tcl  -parm7 *_complex.prmtop -pdb *_complex.pdb -dispdev text
# Setting the pdb with the right beta and occupancy for SMD ref
set allatoms [atomselect top all]
$allatoms set beta 0
$allatoms set occupancy 0
set restrainedtwo [atomselect top "sidechain"]
$restrainedtwo set occupancy 2
set restrained [atomselect top "backbone or resname LIG"]
$restrained set occupancy 5
$allatoms writepdb $argv.ref
quit
