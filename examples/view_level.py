# =============================================================================
# Copyright 2022-2023. Codex Laboratories LLC. All Rights Reserved.
# 
# Created By: Tyler Fedrizzi
# Created On: 6 December 2022
#
# Description: Run a Simulation in View Only mode, allowing you to view
#              the level that is selected.
# =============================================================================
import argparse
import os
import sys

# Taken from https://docs.python-guide.org/writing/structure/
# Add the root folder to our path to access SWARM
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.swarm import SWARM

SIMULATION_NAME = "example"

argpaser = argparse.ArgumentParser("SWARM Simulation Platform",
                                   usage="Run a simulation using a specific map name.",
                                   description="This system represents the client in the SWARM simulation platform. This connects to the core SWARM platform and manages the processing of running a simulation.")
argpaser.add_argument("--map-name", default="SWARMHome", help='The name of the environment to run. Use `list_envs.py` to see which environments are supported')
argpaser.add_argument("--ip-address", default="127.0.0.1", help='The remote IP address of the SWARM Server provided by Codex Labs')

args = argpaser.parse_args()

sim_manager = SWARM(ip_address=args.ip_address)

sim_manager.setup_simulation(args.map_name)

new_simulation = sim_manager.build_simulation(SIMULATION_NAME)

# Please note that the level that will loaded is the one you select
# in the Environment section of the settings file, with the name
# "StartingLevelName"
sim_manager.run_view_only_simulation(args.map_name, SIMULATION_NAME)

print("Finished!")