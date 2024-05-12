import MDAnalysis as mda

#load simulaiton files
simulacio = mda.Universe('../input/system.psf','../MD_100ns_v2/MD.dcd')

#select protein
proteina = simulacio.select_atoms("protein")

#print data
for ts in simulacio.trajectory:
    temps_actual = ts.time
    frame_actual = ts.frame
    rgir = proteina.radius_of_gyration()
    print(f"Frame: {frame_actual:4d},Time {temps_actual:4.0f} ps, R= {rgir:.4f} A")

