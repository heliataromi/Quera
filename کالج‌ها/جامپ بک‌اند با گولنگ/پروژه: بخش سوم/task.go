package qtodo

import (
    "errors"
    "time"
)

type Task interface {
    DoAction()
    GetAlarmTime() time.Time
    GetAction() func()
    GetName() string
    GetDescription() string
}

type BaseTask struct {
    name        string
    description string
    alarmTime   time.Time
    action      func()
    temp        bool
}

func (b BaseTask) DoAction() {
    b.action()
}

func (b BaseTask) GetAlarmTime() time.Time {
    return b.alarmTime
}

func (b BaseTask) GetAction() func() {
    return b.action
}

func (b BaseTask) GetName() string {
    return b.name
}

func (b BaseTask) GetDescription() string {
    return b.description
}

func NewTask(action func(), alarmTime time.Time, name string, description string) (*BaseTask, error) {
    if action == nil {
        return nil, errors.New("invalid action")
    }

    if name == "" {
        return nil, errors.New("invalid name")
    }

    if description == "" {
        return nil, errors.New("invalid description")
    }

    if alarmTime.IsZero() || alarmTime.Before(time.Now()) {
        return nil, errors.New("invalid alarm time")
    }

    newTask := BaseTask{
        name:        name,
        description: description,
        alarmTime:   alarmTime,
        action:      action,
    }

    return &newTask, nil
}
