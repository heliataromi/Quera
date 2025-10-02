package qtodo

import "errors"

type Database interface {
    GetTaskList() []Task
    GetTask(string) (Task, error)
    SaveTask(Task) error
    DelTask(string) error
}

type BaseDatabase struct {
    tasks map[string]Task
}

func (b BaseDatabase) GetTaskList() []Task {
    if b.tasks == nil {
        return []Task{}
    }

    slice := make([]Task, 0, len(b.tasks))
    for _, task := range b.tasks {
        slice = append(slice, task)
    }
    return slice
}

func (b BaseDatabase) GetTask(s string) (Task, error) {
    task, ok := b.tasks[s]
    if !ok {
        return nil, errors.New("task not found")
    }

    return task, nil
}

func (b BaseDatabase) SaveTask(task Task) error {
    _, err := b.GetTask(task.GetName())
    if err == nil {
        return errors.New("task already exists")
    }

    b.tasks[task.GetName()] = task
    return nil
}

func (b BaseDatabase) DelTask(s string) error {
    _, err := b.GetTask(s)
    if err != nil {
        return errors.New("task not found")
    }

    delete(b.tasks, s)
    return nil
}

func NewDatabase() *BaseDatabase {
    newDatabase := BaseDatabase{tasks: make(map[string]Task)}
    return &newDatabase
}
