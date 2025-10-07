package main

import (
	"encoding/json"
	"errors"
	"fmt"
	"net/http"
	"slices"
	"strconv"
	"strings"
)

type Book struct {
	Title    string `json:"title"`
	Author   string `json:"author"`
	Borrowed bool   `json:"borrowed"`
}

type Server struct {
	host  string
	port  int
	books []*Book
}

func NewBook(title string, author string) *Book {
	newBook := Book{title, author, false}
	return &newBook
}

func NewServer(port string) *Server {
	portInt, err := strconv.Atoi(port)
	if err != nil {
		panic(err)
	}

	newServer := Server{
		"localhost",
		portInt,
		[]*Book{},
	}
	return &newServer
}

func (s *Server) Start() {
	http.HandleFunc("/book", s.book)
	err := http.ListenAndServe(fmt.Sprintf("%s:%d", s.host, s.port), nil)
	if err != nil {
		fmt.Println("Error:", err)
	}
}

func (s *Server) book(w http.ResponseWriter, r *http.Request) {
	switch r.Method {
	case http.MethodGet:
		w.Header().Set("Content-Type", "application/json")

		title := r.URL.Query().Get("title")
		author := r.URL.Query().Get("author")

		if title == "" || author == "" {
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(struct {
				Result string `json:"result"`
				Error  string `json:"error"`
			}{
				"",
				"title or author cannot be empty",
			})
			return
		}

		book, err := findBook(s, title, author)
		if err != nil {
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(struct {
				Result string `json:"result"`
				Error  string `json:"error"`
			}{
				"",
				err.Error(),
			})
			return
		}

		if book.isBorrowed() {
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(struct {
				Result string `json:"result"`
				Error  string `json:"error"`
			}{
				"",
				"this book is borrowed",
			})
			return
		}

		w.WriteHeader(http.StatusOK)
		json.NewEncoder(w).Encode(struct {
			Title  string `json:"title"`
			Author string `json:"author"`
		}{
			strings.ToLower(book.Title),
			strings.ToLower(book.Author),
		})
		return

	case http.MethodPost:
		w.Header().Set("Content-Type", "application/x-www-form-urlencoded")

		if err := r.ParseForm(); err != nil {
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(struct {
				Result string `json:"result"`
				Error  string `json:"error"`
			}{
				"",
				err.Error(),
			})
			return
		}

		title := r.PostFormValue("title")
		author := r.PostFormValue("author")

		if title == "" || author == "" {
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(struct {
				Result string `json:"result"`
				Error  string `json:"error"`
			}{
				"",
				"title or author cannot be empty",
			})
			return
		}

		if _, err := findBook(s, title, author); err == nil {
			w.WriteHeader(http.StatusOK)
			json.NewEncoder(w).Encode(struct {
				Result string `json:"result"`
				Error  string `json:"error"`
			}{
				"this book is already in the library",
				"",
			})
			return
		}

		newBook := Book{
			Title:  title,
			Author: author,
		}
		s.books = append(s.books, &newBook)

		w.WriteHeader(http.StatusOK)
		json.NewEncoder(w).Encode(struct {
			Result string `json:"result"`
			Error  string `json:"error"`
		}{
			fmt.Sprintf("added book %s by %s", strings.ToLower(title), strings.ToLower(author)),
			"",
		})
		return

	case http.MethodPut:
		w.Header().Set("Content-Type", "application/json")

		title := r.URL.Query().Get("title")
		author := r.URL.Query().Get("author")

		if title == "" || author == "" {
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(struct {
				Result string `json:"result"`
				Error  string `json:"error"`
			}{
				"",
				"title or author cannot be empty",
			})
			return
		}

		var req struct {
			Borrow bool `json:"borrow"`
		}

		err := json.NewDecoder(r.Body).Decode(&req)
		if err != nil {
			http.Error(w, err.Error(), http.StatusBadRequest)
			json.NewEncoder(w).Encode(struct {
				Result string `json:"result"`
				Error  string `json:"error"`
			}{
				"",
				"borrow value cannot be empty",
			})
			return
		}

		book, err := findBook(s, title, author)
		if err != nil {
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(struct {
				Result string `json:"result"`
				Error  string `json:"error"`
			}{
				"",
				"this book does not exist",
			})
			return
		}

		if req.Borrow {
			if book.isBorrowed() {
				w.WriteHeader(http.StatusBadRequest)
				json.NewEncoder(w).Encode(struct {
					Result string `json:"result"`
					Error  string `json:"error"`
				}{
					"",
					"this book is already borrowed",
				})
				return
			}

			book.Borrowed = true

			w.WriteHeader(http.StatusOK)
			json.NewEncoder(w).Encode(struct {
				Result string `json:"result"`
				Error  string `json:"error"`
			}{
				"you have borrowed this book successfully",
				"",
			})
			return
		}

		if !req.Borrow {
			if !book.isBorrowed() {
				w.WriteHeader(http.StatusBadRequest)
				json.NewEncoder(w).Encode(struct {
					Result string `json:"result"`
					Error  string `json:"error"`
				}{
					"",
					"this book is already in the library",
				})
				return
			}

			book.Borrowed = false

			w.WriteHeader(http.StatusOK)
			json.NewEncoder(w).Encode(struct {
				Result string `json:"result"`
				Error  string `json:"error"`
			}{
				"you have borrowed this book successfully",
				"",
			})
			return
		}
	case http.MethodDelete:
		w.Header().Set("Content-Type", "application/json")

		title := r.URL.Query().Get("title")
		author := r.URL.Query().Get("author")

		if title == "" || author == "" {
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(struct {
				Result string `json:"result"`
				Error  string `json:"error"`
			}{
				"",
				"title or author cannot be empty",
			})
			return
		}

		book, err := findBook(s, title, author)
		if err != nil {
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(struct {
				Result string `json:"result"`
				Error  string `json:"error"`
			}{
				"",
				"this book does not exist",
			})
			return
		}

		for i, listedBook := range s.books {
			if listedBook == book {
				s.books = slices.Delete(s.books, i, i+1)
				break
			}
		}

		w.WriteHeader(http.StatusOK)
		json.NewEncoder(w).Encode(struct {
			Result string `json:"result"`
			Error  string `json:"error"`
		}{
			"successfully deleted",
			"",
		})
		return
	}

}

func findBook(s *Server, title string, author string) (*Book, error) {
	for _, book := range s.books {
		if strings.ToLower(book.Title) == strings.ToLower(title) &&
			strings.ToLower(book.Author) == strings.ToLower(author) {
			return book, nil
		}
	}
	return &Book{}, errors.New("this book does not exist")
}

func (book *Book) isBorrowed() bool {
	return book.Borrowed
}
