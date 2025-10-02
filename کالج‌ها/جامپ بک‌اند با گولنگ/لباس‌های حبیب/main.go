package main

import (
    "bufio"
    "fmt"
    "os"
    "strings"
)

type seasonalClothing struct {
    additional []string
    possible   []string
}

func mapCopy(original map[string]string) map[string]string {
    newMap := make(map[string]string)

    for k, v := range original {
        newMap[k] = v
    }

    return newMap
}

func main() {
    //DEFAULT := []string{"SHIRT", "PANTS"}
    //SPRING := seasonalClothing{possible: []string{"COAT", "CAP"}}
    //SUMMER := seasonalClothing{additional: []string{"CAP"}, possible: []string{}}
    //FALL := seasonalClothing{possible: []string{"COAT", "CAP"}}
    //WINTER := seasonalClothing{possible: []string{"COAT", "JACKET"}}

    cloths := make(map[string][]string)

    scanner := bufio.NewScanner(os.Stdin)

    for i := 0; i < 5; i++ {
        scanner.Scan()
        line := scanner.Text()
        parts := strings.SplitN(line, ":", 2)

        cloth := strings.TrimSpace(parts[0])
        colorStr := strings.TrimSpace(parts[1])
        colors := strings.Fields(colorStr)

        cloths[cloth] = colors
    }

    scanner.Scan()
    season := scanner.Text()

    selectedCloths := make([]map[string]string, 0)

    for _, shirtColor := range cloths["SHIRT"] {
        for _, pantsColor := range cloths["PANTS"] {
            choice := map[string]string{"SHIRT": shirtColor, "PANTS": pantsColor}

            switch season {
            case "SPRING":
                selectedCloths = append(selectedCloths, mapCopy(choice))

                optionalChoice := mapCopy(choice)
                for _, coatColor := range cloths["COAT"] {
                    optionalChoice["COAT"] = coatColor
                    selectedCloths = append(selectedCloths, mapCopy(optionalChoice))
                }

                optionalChoice = mapCopy(choice)
                for _, capColor := range cloths["CAP"] {
                    optionalChoice["CAP"] = capColor
                    selectedCloths = append(selectedCloths, mapCopy(optionalChoice))
                }

                optionalChoice = mapCopy(choice)
                for _, coatColor := range cloths["COAT"] {
                    for _, capColor := range cloths["CAP"] {
                        optionalChoice["COAT"] = coatColor
                        optionalChoice["CAP"] = capColor
                        selectedCloths = append(selectedCloths, mapCopy(optionalChoice))
                    }
                }

            case "SUMMER":
                for _, capColor := range cloths["CAP"] {
                    choice["CAP"] = capColor
                    selectedCloths = append(selectedCloths, mapCopy(choice))
                }

            case "FALL":
                selectedCloths = append(selectedCloths, mapCopy(choice))

                optionalChoice := mapCopy(choice)
                for _, coatColor := range cloths["COAT"] {
                    if coatColor != "yellow" && coatColor != "orange" {
                        optionalChoice["COAT"] = coatColor
                        selectedCloths = append(selectedCloths, mapCopy(optionalChoice))
                    }
                }

                optionalChoice = mapCopy(choice)
                for _, capColor := range cloths["CAP"] {
                    optionalChoice["CAP"] = capColor
                    selectedCloths = append(selectedCloths, mapCopy(optionalChoice))
                }

                optionalChoice = mapCopy(choice)
                for _, coatColor := range cloths["COAT"] {
                    for _, capColor := range cloths["CAP"] {
                        if coatColor != "yellow" && coatColor != "orange" {
                            optionalChoice["COAT"] = coatColor
                            optionalChoice["CAP"] = capColor
                            selectedCloths = append(selectedCloths, mapCopy(optionalChoice))
                        }
                    }
                }

            case "WINTER":
                optionalChoice := mapCopy(choice)
                for _, coatColor := range cloths["COAT"] {
                    optionalChoice["COAT"] = coatColor
                    selectedCloths = append(selectedCloths, mapCopy(optionalChoice))
                }

                optionalChoice = mapCopy(choice)
                for _, jacketColor := range cloths["JACKET"] {
                    optionalChoice["JACKET"] = jacketColor
                    selectedCloths = append(selectedCloths, mapCopy(optionalChoice))
                }
            }
        }

    }

    for _, selectedCloth := range selectedCloths {
        output := make([]string, 0)

        if coat, exists := selectedCloth["COAT"]; exists {
            output = append(output, "COAT: "+coat)
        }
        if shirt, exists := selectedCloth["SHIRT"]; exists {
            output = append(output, "SHIRT: "+shirt)
        }
        if pant, exists := selectedCloth["PANTS"]; exists {
            output = append(output, "PANTS: "+pant)
        }
        if cap, exists := selectedCloth["CAP"]; exists {
            output = append(output, "CAP: "+cap)
        }
        if jacket, exists := selectedCloth["JACKET"]; exists {
            output = append(output, "JACKET: "+jacket)
        }

        fmt.Println(strings.Join(output, " "))
    }
}
