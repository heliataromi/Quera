package commands

import "vc/workdir"

type VC struct {
    status Status
}

type Status struct {
    ModifiedFiles []string
    StagedFiles   []string
}

func (vc *VC) Status() Status {
    return vc.status
}

func Init(wd workdir.WorkDir)
