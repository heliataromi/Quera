package main

import (
    "errors"
    "fmt"
    "sort"
    "strings"
)

type Store struct {
    products []*Product
}

type Product struct {
    name  string
    count int
    price float64
}

func NewStore() *Store {
    newStore := &Store{}
    return newStore
}

func (s *Store) AddProduct(name string, price float64, count int) error {
    if price <= 0 {
        return errors.New("price should be positive")
    }
    if count <= 0 {
        return errors.New("count should be positive")
    }

    for _, product := range s.products {
        if strings.EqualFold(product.name, name) {
            return fmt.Errorf("%s already exists", name)
        }
    }

    newProduct := &Product{name: name, price: price, count: count}
    s.products = append(s.products, newProduct)
    return nil
}

func (s *Store) GetProductCount(name string) (int, error) {
    for _, product := range s.products {
        if strings.EqualFold(product.name, name) {
            return product.count, nil
        }
    }

    return 0, errors.New("invalid product name")
}

func (s *Store) GetProductPrice(name string) (float64, error) {
    for _, product := range s.products {
        if strings.EqualFold(product.name, name) {
            return product.price, nil
        }
    }

    return 0, errors.New("invalid product name")
}

func (s *Store) Order(name string, count int) error {
    if count <= 0 {
        return errors.New("count should be positive")
    }

    for _, product := range s.products {
        if strings.EqualFold(product.name, name) {
            if product.count == 0 {
                return fmt.Errorf("there is no %s in the store", name)
            }

            if count > product.count {
                return fmt.Errorf("not enough %s in the store. there are %d left", name, product.count)
            }

            product.count -= count
            return nil
        }
    }

    return errors.New("invalid product name")
}

func (s *Store) ProductsList() ([]string, error) {
    if len(s.products) == 0 {
        return nil, errors.New("store is empty")
    }

    availableProducts := make([]string, 0)

    for _, product := range s.products {
        if product.count != 0 {
            availableProducts = append(availableProducts, strings.ToLower(product.name))
        }
    }

    if len(availableProducts) != 0 {
        sort.Strings(availableProducts)
        return availableProducts, nil
    }

    return nil, errors.New("store is empty")
}
