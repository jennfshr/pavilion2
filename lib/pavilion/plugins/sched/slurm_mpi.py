from pavilion.schedulers import SchedulerPlugin
from pavilion.schedulers import SchedulerPluginError
from pavilion.schedulers import SchedulerVariables
from pavilion.schedulers import dfr_var_method
import pavilion.plugins.sched.slurm as slurm


class SlurmMPIVars(slurm.SlurmVars):
    @dfr_var_method
    def test_cmd(self):
        """Overrides test_cmd in SlurmVars to use mpirun instead of srun"""
        return 'mpirun'


class SlurmMPI(slurm.Slurm):

    VAR_CLASS = SlurmMPIVars

    def __init__(self):
        SchedulerPlugin.__init__(
            self,
            'slurm_mpi',
            'Schedules tests via Slurm but runs them using mpirun',
            priority=10
        )

