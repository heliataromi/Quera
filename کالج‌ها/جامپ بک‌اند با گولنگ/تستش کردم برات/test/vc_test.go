package main

import (
	"testing"
	"vc/commands"
	"vc/workdir"

	"github.com/stretchr/testify/assert"
)

func TestInit(t *testing.T) {
	assert.NotNil(t, vc)
}

func TestStatusUnmodifiedAtFirst(t *testing.T) {
	status := vc.Status()
	assert.Len(t, status.ModifiedFiles, 0)
	assert.Len(t, status.StagedFiles, 0)
}
func TestStatusModifiedAtFirst(t *testing.T) {
	status := vc.Status()
	assert.Len(t, status.ModifiedFiles, 0)
	assert.Len(t, status.StagedFiles, 0)
	// there is no commit yet
}

func TestStatusModified(t *testing.T) {
	vc = commands.Init(wd.Clone())
	vc.AddAll()
	vc.Commit("initial commit")

	vc.GetWorkDir().AppendToFile("README.md", "\nhello world")

	status := vc.Status()
	assert.ElementsMatch(t, []string{"README.md"}, status.ModifiedFiles)
	assert.Len(t, status.StagedFiles, 0)
}

func TestStatusStaged(t *testing.T) {
	vc = commands.Init(wd.Clone())
	vc.AddAll()
	vc.Commit("initial commit")

	vc.GetWorkDir().AppendToFile("README.md", "\nhello world")
	vc.Add("README.md")

	status := vc.Status()
	assert.Len(t, status.ModifiedFiles, 0)
	assert.ElementsMatch(t, []string{"README.md"}, status.StagedFiles)
}

func TestStatusMixed1(t *testing.T) {
	vc = commands.Init(wd.Clone())
	vc.AddAll()
	vc.Commit("initial commit")

	vc.GetWorkDir().CreateFile(".gitignore")
	vc.GetWorkDir().WriteToFile(".gitignore", "*.class")

	vc.GetWorkDir().AppendToFile("README.md", "\nhello world")
	vc.Add("README.md")

	status := vc.Status()
	assert.ElementsMatch(t, []string{".gitignore"}, status.ModifiedFiles)
	assert.ElementsMatch(t, []string{"README.md"}, status.StagedFiles)
}

func TestStatusMixed2(t *testing.T) {
	vc = commands.Init(wd.Clone())
	vc.AddAll()
	vc.Commit("initial commit")

	vc.GetWorkDir().CreateFile(".gitignore")
	vc.GetWorkDir().WriteToFile(".gitignore", "*.class")

	vc.GetWorkDir().AppendToFile("README.md", "\nhello world")
	vc.Add("README.md")

	vc.GetWorkDir().AppendToFile("README.md", "\nit's time to goodbye")

	status := vc.Status()
	assert.ElementsMatch(t, []string{".gitignore", "README.md"}, status.ModifiedFiles)
	assert.ElementsMatch(t, []string{"README.md"}, status.StagedFiles)
}

func TestLog1(t *testing.T) {
	vc = commands.Init(wd.Clone())
	vc.AddAll()
	vc.Commit("commit1")
	vc.Commit("commit2")
	vc.Commit("commit3")
	vc.Commit("commit4")

	assert.Equal(t,
		[]string{"commit4", "commit3", "commit2", "commit1"}, // in reverse order
		vc.Log(),
	)
}

func TestLog2(t *testing.T) {
	vc = commands.Init(wd.Clone())
	assert.Equal(t,
		[]string{},
		vc.Log(),
	)
}

func addCommits(wd *workdir.WorkDir) *commands.VC {
	vc = commands.Init(wd.Clone())
	vc.AddAll()
	vc.Commit("initial commit")

	vc.GetWorkDir().AppendToFile("src/main.go", "func main(){}")
	vc.AddAll()
	vc.Commit("feat(main)")

	vc.GetWorkDir().AppendToFile("src/main.go", "\n// modification1\n")
	vc.GetWorkDir().AppendToFile("src/workdir/file1.go", "\n// another modification1\n")
	vc.GetWorkDir().AppendToFile("src/workdir/file2.go", "\n// yet another modification1\n")
	vc.Add("src/main.go", "src/workdir/file1.go")
	vc.Add("src/main.go", "src/workdir/file2.go")
	vc.Commit("modifications 1")

	vc.GetWorkDir().AppendToFile("src/main.go", "\n// modification2\n")
	vc.GetWorkDir().AppendToFile("src/workdir/file1.go", "\n// another modification2\n")
	vc.GetWorkDir().AppendToFile("src/workdir/file2.go", "\n// yet another modification2\n")
	vc.Add("src/main.go", "src/workdir/file1.go", "src/workdir/file2.go")
	vc.Commit("modifications 2")

	return vc
}

func TestCheckout1(t *testing.T) {
	vc := addCommits(wd.Clone())
	{
		wdC, err := vc.Checkout("~1")
		assert.NoError(t, err)
		content, err := wdC.CatFile("src/main.go")
		assert.NoError(t, err)
		assert.Contains(t, content, "func main(){}")
		assert.Contains(t, content, "modification1")
		assert.NotContains(t, content, "modification2")
	}

	{
		wdC, err := vc.Checkout("~2")
		assert.NoError(t, err)
		content, err := wdC.CatFile("src/main.go")
		assert.NoError(t, err)
		assert.Contains(t, content, "func main(){}")
		assert.NotContains(t, content, "modification1")
		assert.NotContains(t, content, "modification2")
	}
	{
		wdC, err := vc.Checkout("~3")
		assert.NoError(t, err)
		content, err := wdC.CatFile("src/main.go")
		assert.NoError(t, err)
		assert.NotContains(t, content, "func main(){}")
		assert.NotContains(t, content, "modification1")
		assert.NotContains(t, content, "modification2")
	}
}
func TestCheckout2(t *testing.T) {
	vc := addCommits(wd.Clone())
	{
		wdC, err := vc.Checkout("^")
		assert.NoError(t, err)
		content, err := wdC.CatFile("src/main.go")
		assert.NoError(t, err)
		assert.Contains(t, content, "func main(){}")
		assert.Contains(t, content, "modification1")
		assert.NotContains(t, content, "modification2")
	}

	{
		wdC, err := vc.Checkout("^^")
		assert.NoError(t, err)
		content, err := wdC.CatFile("src/main.go")
		assert.NoError(t, err)
		assert.Contains(t, content, "func main(){}")
		assert.NotContains(t, content, "modification1")
		assert.NotContains(t, content, "modification2")
	}
	{
		wdC, err := vc.Checkout("^^^")
		assert.NoError(t, err)
		content, err := wdC.CatFile("src/main.go")
		assert.NoError(t, err)
		assert.NotContains(t, content, "func main(){}")
		assert.NotContains(t, content, "modification1")
		assert.NotContains(t, content, "modification2")
	}
}
