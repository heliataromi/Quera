package qtodo_test

import (
	"testing"
	"time"

	"qtodo"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

// task

const (
	safeMargin   = 100 * time.Millisecond
	requestTime  = time.Second
	responseTime = time.Second + (time.Millisecond * 100)
)

func TestTaskCreation(t *testing.T) {
	t.Parallel()
	name, description, alarmTime, action := "walk", "walk somewhere", time.Now().Add(requestTime), func() {}
	var newTask qtodo.Task
	newTask, err := qtodo.NewTask(action, alarmTime, name, description)
	assert.Nil(t, err)

	assert.NotNil(t, newTask)
}

func TestTaskNameAndDescription(t *testing.T) {
	t.Parallel()
	name, description, alarmTime, action := "walk", "walk somewhere", time.Now().Add(requestTime), func() {}
	var newTask qtodo.Task
	newTask, err := qtodo.NewTask(action, alarmTime, name, description)
	assert.Nil(t, err)

	assert := assert.New(t)
	assert.Equal("walk", newTask.GetName())
	assert.Equal("walk somewhere", newTask.GetDescription())
}

// repository

func TestDBCreation(t *testing.T) {
	t.Parallel()
	var db qtodo.Database = qtodo.NewDatabase()
	assert.NotNil(t, db)
}

func TestGetTaskList(t *testing.T) {
	t.Parallel()
	var db qtodo.Database = qtodo.NewDatabase()
	assert := assert.New(t)
	name, description, alarmTime, action := "walk", "walk somewhere", time.Now().Add(requestTime), func() {}
	newTask, err := qtodo.NewTask(action, alarmTime, name, description)
	assert.Nil(err)

	name, description, alarmTime, action = "study", "do some studying", time.Now().Add(requestTime*2), func() {}
	newTask2, err := qtodo.NewTask(action, alarmTime, name, description)
	assert.Nil(err)

	err = db.SaveTask(newTask)
	assert.Nil(err)
	err = db.SaveTask(newTask2)
	assert.Nil(err)

	assert.Len(db.GetTaskList(), 2)
}

// app

func TestAppCreation(t *testing.T) {
	t.Parallel()
	var db qtodo.Database = qtodo.NewDatabase()
	var app qtodo.App = qtodo.NewApp(db)
	assert := assert.New(t)
	assert.NotNil(app)

	err := app.AddTask("walk", "walking", time.Now().Add(requestTime), func() {}, false)
	assert.Nil(err)
}

func TestAppGetTaskList(t *testing.T) {
	t.Parallel()
	var db qtodo.Database = qtodo.NewDatabase()
	var app qtodo.App = qtodo.NewApp(db)
	assert := assert.New(t)
	assert.NotNil(app)

	err := app.AddTask("walk", "walking", time.Now().Add(requestTime), func() {}, false)
	assert.Nil(err)

	actual := app.GetTaskList()
	require.Equal(t, 1, len(actual))
	assert.Equal("walk", actual[0].GetName())
}

func TestAppDelTask(t *testing.T) {
	t.Parallel()
	var db qtodo.Database = qtodo.NewDatabase()
	var app qtodo.App = qtodo.NewApp(db)
	assert := assert.New(t)
	assert.NotNil(app)

	err := app.AddTask("walk", "walking", time.Now().Add(requestTime), func() {}, false)
	assert.Nil(err)

	_, err = app.GetTask("walk")
	assert.Nil(err)

	err = app.DelTask("walk")
	assert.Nil(err)

	_, err = app.GetTask("walk")
	assert.Error(err)
}
