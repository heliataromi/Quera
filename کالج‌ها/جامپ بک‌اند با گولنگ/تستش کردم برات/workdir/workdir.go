package workdir

import (
    "io"
    "os"
)

// you can use this library freely: "github.com/otiai10/copy"

type WorkDir struct {
}

func (wd *WorkDir) ListFilesRoot() []string {
    dir, _ := os.Open(".")
    defer dir.Close()

    files, _ := dir.Readdir(-1)
    fileNames := make([]string, len(files))

    for _, file := range files {
        fileNames = append(fileNames, file.Name())
    }

    return fileNames
}

func (wd *WorkDir) ListFilesIn(path string) ([]string, error) {
    dir, err := os.Open(path)
    if err != nil {
        return nil, err
    }

    defer dir.Close()

    files, err := dir.Readdir(-1)
    if err != nil {
        return nil, err
    }

    fileNames := make([]string, len(files))

    for _, file := range files {
        fileNames = append(fileNames, file.Name())
    }

    return fileNames, nil
}

func (wd *WorkDir) CatFile(path string) (string, error) {
    file, err := os.OpenFile(path, os.O_RDONLY, 0)
    if err != nil {
        return "", err
    }

    defer file.Close()

    data, err := io.ReadAll(file)
    if err != nil {
        return "", err
    }

    return string(data), nil
}

func (wd *WorkDir) AppendToFile(path, content string) error {
    file, err := os.OpenFile(path, os.O_APPEND|os.O_WRONLY, 0)
    if err != nil {
        return err
    }

    defer file.Close()

    if _, err := file.WriteString(content); err != nil {
        return err
    }

    return nil
}
