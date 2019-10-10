# FabSMD
This is a SMD (Steered Molecular Dynamics) plugin for FabSim3


## Installation
Simply type `fabsim localhost install_plugin:FabSMD` anywhere inside your FabSim3 install directory.

## Testing
1. To run a single job, type `fab <remote_machine> SMD:Rimonabant`, .
	> `fab <remote_machine> SMD:Rimonabant`
	> <br/><br/> `Rimonabant` is the sample config file, you can replace it with your own. To do that, just put your configuration folder in the `/FabSMD/config_files`. 
2. 	To run *N* jobs with exactly the same configuration (e.g., to account for stochasticity), just run:
	> `fab <remote_machine> SMD:Rimonabant,replicas=<N>`
3. To run the ensemble, you can type:
	> `fab <remote_machine> SMD_ensemble:Rimonabant`
	> <br/><br/> This command takes the files in the `/FabSMD/config_files` and copies them into the target `<remote_machine>` result directory as usual, but does this for each file in the `SWEEP` directory

4. You can also combine replicas with ensemble runs, e.g. using:
	> `fab <remote_machine> SMD_ensemble:Rimonabant,replicas=<N>`
