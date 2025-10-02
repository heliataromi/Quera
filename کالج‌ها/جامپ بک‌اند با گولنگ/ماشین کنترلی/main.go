package main

import "fmt"

type Car struct {
    speed   int
    battery int
}

func NewCar(speed, battery int) *Car {
    car := Car{speed: speed, battery: battery}
    return &car
}
func GetSpeed(car *Car) int {
    return car.speed
}
func GetBattery(car *Car) int {
    return car.battery
}
func ChargeCar(car *Car, minutes int) {
    chargeDelta := minutes / 2
    car.battery = min(car.battery+chargeDelta, 100)
}
func TryFinish(car *Car, distance int) string {
    chargeDelta := distance / 2
    charge := car.battery - chargeDelta
    car.battery = max(charge, 0)

    if charge >= 0 {
        return fmt.Sprintf("%.2f", float32(distance)/float32(car.speed))
    } else {
        return ""
    }
}
