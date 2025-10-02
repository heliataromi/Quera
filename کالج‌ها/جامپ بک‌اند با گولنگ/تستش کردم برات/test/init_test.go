package main

import (
	"os"
	"testing"
	"vc/commands"
	workdir "vc/workdir"
)

var wd *workdir.WorkDir

var vc *commands.VC

func TestMain(m *testing.M) {
	Setup()
	os.Exit(m.Run())
}

func Setup() {
	wd = workdir.InitEmptyWorkDir()

	err := wd.CreateFile("README.md")
	if err != nil {
		panic(err)
	}
	err = wd.CreateDir("src")
	if err != nil {
		panic(err)
	}
	err = wd.CreateFile("src/main.go")
	if err != nil {
		panic(err)
	}

	err = wd.CreateDir("src/workdir")
	if err != nil {
		panic(err)
	}
	err = wd.CreateFile("src/workdir/file1.go")
	if err != nil {
		panic(err)
	}
	err = wd.CreateFile("src/workdir/file2.go")
	if err != nil {
		panic(err)
	}

	err = wd.WriteToFile("README.md", "### MY GIT IMPL")
	if err != nil {
		panic(err)
	}

	vc = commands.Init(wd.Clone())
}
