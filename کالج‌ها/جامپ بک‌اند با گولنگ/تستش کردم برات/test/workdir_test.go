package main

import (
    "testing"

    "github.com/stretchr/testify/assert"
)

func TestAllFiles(t *testing.T) {
    assert.ElementsMatch(t,
        []string{
            "README.md",
            "src/main.go",
            "src/workdir/file1.go",
            "src/workdir/file2.go"},
        wd.ListFilesRoot(),
    )
}

func TestDirFiles(t *testing.T) {
    actual, err := wd.ListFilesIn("src")
    assert.NoError(t, err)
    assert.ElementsMatch(t,
        []string{
            "src/main.go",
            "src/workdir/file1.go",
            "src/workdir/file2.go",
        },
        actual,
    )
}

func TestCat(t *testing.T) {
    actual, err := wd.CatFile("README.md")
    assert.NoError(t, err)
    assert.Equal(t, "### MY GIT IMPL", actual)
}

func TestCatNotFound(t *testing.T) {
    _, err := wd.CatFile("src/non_existing_file")
    assert.Error(t, err)
}

func TestAppend(t *testing.T) {
    wd.AppendToFile("src/main.go", "package main")
    wd.AppendToFile("src/main.go", "\nfunc main(){}\n")
    actual, err := wd.CatFile("src/main.go")
    assert.NoError(t, err)
    assert.Equal(t, "package main\nfunc main(){}\n", actual)
}

func TestAppendNotFound(t *testing.T) {
    err := wd.AppendToFile("src/non_existing_file", "salam")
    assert.Error(t, err)
}

func TestWrite(t *testing.T) {
    wd.CreateFile(".gitignore")
    wd.WriteToFile(".gitignore", "*.out\n*.exe")
    actual, err := wd.CatFile(".gitignore")
    assert.NoError(t, err)
    assert.Equal(t, "*.out\n*.exe", actual)
}

func TestWriteNotFound(t *testing.T) {
    err := wd.WriteToFile("src/non_existing_file", "salam")
    assert.Error(t, err)
}

func TestClone(t *testing.T) {
    clonedWD := wd.Clone()
    clonedWD.AppendToFile("README.md", "junk content")
    clonedWD.CreateFile("LICENSE")

    actual, err := wd.CatFile("README.md")
    assert.NoError(t, err)
    assert.Equal(t, "### MY GIT IMPL", actual)
    assert.NotContains(t, wd.ListFilesRoot(), "LICENSE")
    assert.Contains(t, clonedWD.ListFilesRoot(), "LICENSE")
}
