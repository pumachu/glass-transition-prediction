# Protocol for glass-transition temperature prediction
This is a repository for the paper:

**Kun-Han Lin**, Leanne Paterson, Falk May and **Denis Andrienko** Glass transition temperature prediction of disordered molecular solids, *submitted*

The contents will be introduced as following.

### INPUT_FILES
This folder contains input files for Gaussian (**GAUSSIAN/**), DDEC6 (**DDEC6/**) and Gromacs (**GROMACS/**) computations.
In **GROMACS** folder, there are three input files corresponding to the three steps in generating simulated amorphous morphology and cooling:   
```
a. Geometry optimizaion (em.mdp)  
b. Heating and compressing (heating.mdp)   
c. Cooling (cooling.mdp)   
```
### ANALYZING_SCRIPTS
This folder contains python scripts for Tg fitting and creating R<sup>2</sup>-Temperautre plots for various fitting ranges.  
**Usage for R2-T_plot.py:**  
```
python R2-T_plot.py energy.xvg
```
The input file *energy.xvg* is the Gromacs output that contains the information of density and temperautre. The output of the python script is the R<sup>2</sup>-Temperature plot for differnt fitting ranges as shown below:  

<img src='https://i.imgur.com/NaynZFf.png' alt='alt text' width=700>

**Usage for Tg_fit_plot.py:**  
```
python Tg_fit_plot.py energy.xvg
```
The output of the python script is the ρ-Temperature plot and the fitted Tg using different fitting ranges:

```
python Tg_fit_plot.py energy.xvg
```

```
Fitting Range1:[ 405.0 , 555.0 )  
Fitting Range2:[ 24.0 , 174.0 )  
Fitting size:  150 Tg:  70.17  
Fitting Range1:[ 412.0 , 612.0 )  
Fitting Range2:[ 14.0 , 214.0 )  
Fitting size:  200 Tg:  81.23  
Fitting Range1:[ 401.0 , 651.0 )  
Fitting Range2:[ 2.0 , 252.0 )  
Fitting size:  250 Tg:  87.60  
Fitting Range1:[ 401.0 , 701.0 )  
Fitting Range2:[ 1.0 , 301.0 )  
Fitting size:  300 Tg:  101.31  
```

<img src='https://i.imgur.com/pm4Xwh6.png' alt='alt text' width=500>

### MATERIALS_DATA
This folder contains data of 26 organic semiconductors investigated in this work. The files in the subdirectory are explained in the table below:  

| Subfolder     | File          | Explanation  |  
| :-----------: |:-------------:| :-----------:|  
| STRUCTURE     | nN.xyz        | XYZ coordinate of the molecule in neutral ground state |  
| GAS_PHASE_QM  | nN.log        | Gaussian log file |  
| DDEC6         | DDEC*         | Output files from DDEC6 calculations; see details [here](https://sourceforge.net/projects/ddec/files/) |  
| FORCEFIELD    | .top and .ff  | topology and forcefield parameters for gromacs simulations | 
| RHO-T         | energy.xvg    | Gromacs output containing information of density and temperature during the cooling process | 










