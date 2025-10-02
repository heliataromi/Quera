package qtodo

import (
    "errors"
    "time"
)

type App interface {
    StartTask(string) error
    StopTask(string)
    AddTask(string, string, time.Time, func(), bool) error
    DelTask(string) error
    GetTaskList() []Task
    GetActiveTaskList() []Task
    GetTask(string) (Task, error)
}
type BaseApp struct {
    database       Database
    activeTaskList map[string]Task
}

func (b BaseApp) StartTask(s string) error {
    task, err := b.database.GetTask(s)
    if err != nil {
        return err
    }

    baseTask, ok := task.(*BaseTask)
    if !ok {
        return errors.New("task is not of expected type *BaseTask")
    }

    baseDatabase, ok := b.database.(*BaseDatabase)
    if !ok {
        return errors.New("database is not of expected type *BaseDatabase")
    }

    b.activeTaskList[s] = task

    go func() {
        time.Sleep(time.Until(task.GetAlarmTime()))
        if _, ok := b.activeTaskList[s]; ok {
            if baseTask.temp == true {
                defer delete(b.activeTaskList, s)
                defer delete(baseDatabase.tasks, s)
            }
            baseTask.DoAction()
        }
    }()
    return nil
}

func (b BaseApp) StopTask(s string) {
    delete(b.activeTaskList, s)
}

func (b BaseApp) AddTask(s string, s2 string, t time.Time, f func(), b2 bool) error {
    newTask, err := NewTask(f, t, s, s2)
    if err != nil {
        return err
    }

    newTask.temp = b2

    return b.database.SaveTask(newTask)
}

func (b BaseApp) DelTask(s string) error {
    return b.database.DelTask(s)
}

func (b BaseApp) GetTaskList() []Task {
    return b.database.GetTaskList()
}

func (b BaseApp) GetActiveTaskList() []Task {
    slice := make([]Task, 0, len(b.activeTaskList))

    for _, task := range b.activeTaskList {
        slice = append(slice, task)
    }

    return slice
}

func (b BaseApp) GetTask(s string) (Task, error) {
    return b.database.GetTask(s)
}

func NewApp(database Database) *BaseApp {
    newApp := BaseApp{database, make(map[string]Task)}
    return &newApp
}
