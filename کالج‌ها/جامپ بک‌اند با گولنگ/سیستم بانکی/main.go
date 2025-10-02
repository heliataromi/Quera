package main

type SavingsAccount struct {
	balance int
}

func (s *SavingsAccount) MonthlyInterest() int {
	if s.CheckBalance() == 0 {
		return 0
	}

	return (s.CheckBalance() * 5 / 100) / 12
}

func (s *SavingsAccount) Transfer(receiver Account, amount int) string {
	switch receiver.(type) {
	case *SavingsAccount:
	case *CheckingAccount:
	case *InvestmentAccount:
	default:
		return "Invalid receiver account"
	}

	if amount <= 0 {
		return "Amount cannot be negative"
	}

	if amount > s.CheckBalance() {
		return "Account balance is not enough"
	}

	s.Withdraw(amount)
	receiver.Deposit(amount)

	return "Success"
}

func (s *SavingsAccount) Deposit(amount int) string {
	if amount <= 0 {
		return "Amount cannot be negative"
	}

	s.balance += amount

	return "Success"
}

func (s *SavingsAccount) Withdraw(amount int) string {
	if amount <= 0 {
		return "Amount cannot be negative"
	}

	if amount > s.CheckBalance() {
		return "Account balance is not enough"
	}

	s.balance -= amount

	return "Success"
}

func (s *SavingsAccount) CheckBalance() int {
	return s.balance
}

type CheckingAccount struct {
	balance int
}

func (c *CheckingAccount) MonthlyInterest() int {
	if c.CheckBalance() == 0 {
		return 0
	}

	return (c.CheckBalance() * 1 / 100) / 12
}

func (c *CheckingAccount) Transfer(receiver Account, amount int) string {
	switch receiver.(type) {
	case *SavingsAccount:
	case *CheckingAccount:
	case *InvestmentAccount:
	default:
		return "Invalid receiver account"
	}

	if amount <= 0 {
		return "Amount cannot be negative"
	}

	if amount > c.CheckBalance() {
		return "Account balance is not enough"
	}

	c.Withdraw(amount)
	receiver.Deposit(amount)

	return "Success"
}

func (c *CheckingAccount) Deposit(amount int) string {
	if amount <= 0 {
		return "Amount cannot be negative"
	}

	c.balance += amount

	return "Success"
}

func (c *CheckingAccount) Withdraw(amount int) string {
	if amount <= 0 {
		return "Amount cannot be negative"
	}

	if amount > c.CheckBalance() {
		return "Account balance is not enough"
	}

	c.balance -= amount

	return "Success"
}

func (c *CheckingAccount) CheckBalance() int {
	return c.balance
}

type InvestmentAccount struct {
	balance int
}

func (i *InvestmentAccount) MonthlyInterest() int {
	if i.CheckBalance() == 0 {
		return 0
	}

	return (i.CheckBalance() * 2 / 100) / 12
}

func (i *InvestmentAccount) Transfer(receiver Account, amount int) string {
	switch receiver.(type) {
	case *SavingsAccount:
	case *CheckingAccount:
	case *InvestmentAccount:
	default:
		return "Invalid receiver account"
	}

	if amount <= 0 {
		return "Amount cannot be negative"
	}

	if amount > i.CheckBalance() {
		return "Account balance is not enough"
	}

	i.Withdraw(amount)
	receiver.Deposit(amount)

	return "Success"
}

func (i *InvestmentAccount) Deposit(amount int) string {
	if amount <= 0 {
		return "Amount cannot be negative"
	}

	i.balance += amount

	return "Success"
}

func (i *InvestmentAccount) Withdraw(amount int) string {
	if amount <= 0 {
		return "Amount cannot be negative"
	}

	if amount > i.CheckBalance() {
		return "Account balance is not enough"
	}

	i.balance -= amount

	return "Success"
}

func (i *InvestmentAccount) CheckBalance() int {
	return i.balance
}

func NewSavingsAccount() *SavingsAccount {
	return &SavingsAccount{}
}

func NewCheckingAccount() *CheckingAccount {
	return &CheckingAccount{}
}

func NewInvestmentAccount() *InvestmentAccount {
	return &InvestmentAccount{}
}
