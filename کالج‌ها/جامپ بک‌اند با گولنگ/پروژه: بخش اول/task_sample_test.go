package qtodo_test

import (
	"testing"
	"time"

	"qtodo"

	"github.com/stretchr/testify/assert"
)

const (
	safeMargin   = 100 * time.Millisecond
	requestTime  = time.Second
	responseTime = time.Second + (time.Millisecond * 100)
)

func TestTaskCreation(t *testing.T) {
	name, description, alarmTime, action := "walk", "walk somewhere", time.Now().Add(requestTime), func() {}
	newTask, err := qtodo.NewTask(action, alarmTime, name, description)
	assert.Nil(t, err)

	assert.NotNil(t, newTask)
}

func TestTaskNameAndDescription(t *testing.T) {
	name, description, alarmTime, action := "walk", "walk somewhere", time.Now().Add(requestTime), func() {}
	newTask, err := qtodo.NewTask(action, alarmTime, name, description)
	assert.Nil(t, err)

	assert := assert.New(t)
	assert.Equal("walk", newTask.GetName())
	assert.Equal("walk somewhere", newTask.GetDescription())
}
