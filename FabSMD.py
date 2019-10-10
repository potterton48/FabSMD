# -*- coding: utf-8 -*-
#
# This source file is part of the FabSim software toolkit, which is distributed under the BSD 3-Clause license.
# Please refer to LICENSE for detailed information regarding the licensing.
#
# This file contains FabSim definitions specific to FabSMD.

from base.fab import *
from pprint import pprint as pp
# Add local script, blackbox and template path.
add_local_paths("FabSMD")


@task
def SMD(config, **args):
    """Submit a single SMD job to the remote queue.
    The job results will be stored with a name pattern as defined in the environment,
    """
    update_environment(args)
    with_config(config)
    if (hasattr(env, 'namd_option') == False):
        env.namd_option = ""
    execute(put_configs, config)

    job(dict(script='SMD'), args)


@task
def SMD_ensemble(config="dummy_test", **args):
    # Submits an ensemble of SMD jobs.

    path_to_config = find_config_file_path(config)
    print("local config file path at: %s" % path_to_config)
    sweep_dir = path_to_config + "/SWEEP"
    if (hasattr(env, 'namd_option') == False):
        env.namd_option = ""
    env.script = 'SMD'

    run_ensemble(config, sweep_dir, **args)
