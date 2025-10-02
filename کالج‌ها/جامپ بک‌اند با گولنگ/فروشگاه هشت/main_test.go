package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestAddProduct1(t *testing.T) {
	s := NewStore()
	err := s.AddProduct("apple", 20000, 10)
	assert.Nil(t, err)
	c, err2 := s.GetProductCount("apple")
	assert.Nil(t, err2)
	assert.Equal(t, 10, c)
	p, err3 := s.GetProductPrice("apple")
	assert.Nil(t, err3)
	assert.Equal(t, 20000.0, p)

	err = s.AddProduct("sHampoo", 100000, 20)
	assert.Nil(t, err)
	c, err2 = s.GetProductCount("SHAMPOO")
	assert.Nil(t, err2)
	assert.Equal(t, 20, c)
	p, err3 = s.GetProductPrice("Shampoo")
	assert.Nil(t, err3)
	assert.Equal(t, 100000.0, p)

	err = s.AddProduct("honey", 300000, 15)
	assert.Nil(t, err)
	c, err2 = s.GetProductCount("Honey")
	assert.Nil(t, err2)
	assert.Equal(t, 15, c)
	p, err3 = s.GetProductPrice("HoNeY")
	assert.Nil(t, err3)
	assert.Equal(t, 300000.0, p)
}

func TestAddProduct2(t *testing.T) {
	s := NewStore()
	err := s.AddProduct("apple", 20000, 10)
	assert.Nil(t, err)
	c, err2 := s.GetProductCount("apple")
	assert.Nil(t, err2)
	assert.Equal(t, 10, c)
	p, err3 := s.GetProductPrice("apple")
	assert.Nil(t, err3)
	assert.Equal(t, 20000.0, p)

	err = s.AddProduct("apple", 30000, 30)
	assert.NotNil(t, err)
	assert.Equal(t, "apple already exists", err.Error())
	c, err2 = s.GetProductCount("apple")
	assert.NoError(t, err2)
	assert.Equal(t, 10, c)
	p, err3 = s.GetProductPrice("apple")
	assert.NoError(t, err3)
	assert.Equal(t, 20000.0, p)

	err = s.AddProduct("AppLe", 40000, 40)
	assert.NotNil(t, err)
	assert.Equal(t, "AppLe already exists", err.Error())
	c, err2 = s.GetProductCount("applE")
	assert.NoError(t, err2)
	assert.Equal(t, 10, c)
	p, err3 = s.GetProductPrice("apPle")
	assert.NoError(t, err3)
	assert.Equal(t, 20000.0, p)
}

func TestAddProduct3(t *testing.T) {
	s := NewStore()
	err := s.AddProduct("apple", 0, 10)
	assert.NotNil(t, err)
	assert.Equal(t, "price should be positive", err.Error())
	c, err2 := s.GetProductCount("apple")
	assert.NotNil(t, err2)
	assert.Equal(t, 0, c)
	assert.Equal(t, "invalid product name", err2.Error())
	p, err3 := s.GetProductPrice("apple")
	assert.NotNil(t, err3)
	assert.Equal(t, 0.0, p)
	assert.Equal(t, "invalid product name", err3.Error())

	err = s.AddProduct("apple", -10, 10)
	assert.NotNil(t, err)
	assert.Equal(t, "price should be positive", err.Error())
	c, err2 = s.GetProductCount("apple")
	assert.NotNil(t, err2)
	assert.Equal(t, 0, c)
	assert.Equal(t, "invalid product name", err2.Error())
	p, err3 = s.GetProductPrice("apple")
	assert.NotNil(t, err3)
	assert.Equal(t, 0.0, p)
	assert.Equal(t, "invalid product name", err3.Error())
}

func TestAddProduct4(t *testing.T) {
	s := NewStore()
	err := s.AddProduct("apple", 10, 0)
	assert.Equal(t, "count should be positive", err.Error())
	assert.NotNil(t, err)
	c, err2 := s.GetProductCount("apple")
	assert.NotNil(t, err2)
	assert.Equal(t, 0, c)
	assert.Equal(t, "invalid product name", err2.Error())
	p, err3 := s.GetProductPrice("apple")
	assert.NotNil(t, err3)
	assert.Equal(t, 0.0, p)
	assert.Equal(t, "invalid product name", err3.Error())

	err = s.AddProduct("apple", 10, -10)
	assert.Equal(t, "count should be positive", err.Error())
	assert.NotNil(t, err)
	c, err2 = s.GetProductCount("apple")
	assert.NotNil(t, err2)
	assert.Equal(t, 0, c)
	assert.Equal(t, "invalid product name", err2.Error())
	p, err3 = s.GetProductPrice("apple")
	assert.NotNil(t, err3)
	assert.Equal(t, 0.0, p)
	assert.Equal(t, "invalid product name", err3.Error())

	err = s.AddProduct("apple", -10, -10)
	assert.Equal(t, "price should be positive", err.Error())
	assert.NotNil(t, err)
	c, err2 = s.GetProductCount("apple")
	assert.NotNil(t, err2)
	assert.Equal(t, 0, c)
	assert.Equal(t, "invalid product name", err2.Error())
	p, err3 = s.GetProductPrice("apple")
	assert.NotNil(t, err3)
	assert.Equal(t, 0.0, p)
	assert.Equal(t, "invalid product name", err3.Error())
}

func TestOrder1(t *testing.T) {
	s := NewStore()
	s.AddProduct("apple", 20000, 10)
	err := s.Order("apple", 0)
	assert.NotNil(t, err)
	assert.Equal(t, "count should be positive", err.Error())
	err = s.Order("apple", -10)
	assert.NotNil(t, err)
	assert.Equal(t, "count should be positive", err.Error())
}
func TestOrder2(t *testing.T) {
	s := NewStore()
	err := s.Order("apppppple", 10)
	assert.NotNil(t, err)
	assert.Equal(t, "invalid product name", err.Error())
	s.AddProduct("apple", 20000, 10)
	err = s.Order("apppppple", 10)
	assert.NotNil(t, err)
	assert.Equal(t, "invalid product name", err.Error())
}

func TestOrder3(t *testing.T) {
	s := NewStore()
	s.AddProduct("apple", 20000, 2)
	s.AddProduct("tomato", 27000, 15)
	err := s.Order("tomato", 100)
	c, _ := s.GetProductCount("tomato")
	assert.Equal(t, 15, c)
	assert.NotNil(t, err)
	assert.Equal(t, "not enough tomato in the store. there are 15 left", err.Error())
	err = s.Order("apple", 20)
	c, _ = s.GetProductCount("apple")
	assert.Equal(t, 2, c)
	assert.NotNil(t, err)
	assert.Equal(t, "not enough apple in the store. there are 2 left", err.Error())
}

func TestOrder4(t *testing.T) {
	s := NewStore()
	s.AddProduct("apple", 20000, 2)
	s.AddProduct("tomato", 27000, 15)
	err := s.Order("apple", 1)
	assert.Nil(t, err)
	c, _ := s.GetProductCount("apple")
	assert.Equal(t, 1, c)
	err = s.Order("tomato", 8)
	assert.Nil(t, err)
	c, _ = s.GetProductCount("tomato")
	assert.Equal(t, 7, c)
}

func TestOrder5(t *testing.T) {
	s := NewStore()
	s.AddProduct("tomato", 27000, 15)
	err := s.Order("tomato", 5)
	assert.Nil(t, err)
	c, _ := s.GetProductCount("tomato")
	assert.Equal(t, 10, c)
	err = s.Order("tomato", 10)
	assert.Nil(t, err)
	c, _ = s.GetProductCount("tomato")
	assert.Equal(t, 0, c)
	err = s.Order("tomato", 3)
	assert.NotNil(t, err)
	assert.Equal(t, "there is no tomato in the store", err.Error())
	c, _ = s.GetProductCount("tomato")
	assert.Equal(t, 0, c)
}

func TestProductsList1(t *testing.T) {
	s := NewStore()
	arr, err := s.ProductsList()
	assert.NotNil(t, err)
	assert.Nil(t, arr)
	assert.Equal(t, "store is empty", err.Error())
}

func TestProductsList2(t *testing.T) {
	s := NewStore()
	s.AddProduct("apple", 20000, 2)
	s.AddProduct("tomato", 27000, 15)
	s.Order("apple", 2)
	s.Order("tomato", 15)
	arr, err := s.ProductsList()
	assert.NotNil(t, err)
	assert.Nil(t, arr)
	assert.Equal(t, "store is empty", err.Error())
}

func TestProductsList3(t *testing.T) {
	s := NewStore()
	s.AddProduct("tomato", 27000, 15)
	s.AddProduct("apple", 20000, 2)
	s.AddProduct("mango", 70000, 5)
	arr, err := s.ProductsList()
	assert.Nil(t, err)
	assert.EqualValues(t, []string{"apple", "mango", "tomato"}, arr)
}

func TestProductsList4(t *testing.T) {
	s := NewStore()
	s.AddProduct("tomato", 27000, 15)
	s.AddProduct("apple", 20000, 2)
	s.AddProduct("mango", 70000, 5)
	s.Order("mango", 5)
	arr, err := s.ProductsList()
	assert.Nil(t, err)
	assert.EqualValues(t, []string{"apple", "tomato"}, arr)
}
