package main

import (
	"errors"
	"fmt"
	"strconv"
	"strings"
	"sync"
)

type Player struct {
	name       string
	currentMap *Map
	messages   chan string
	mutex      sync.Mutex
}

type Map struct {
	id       int
	players  []*Player
	messages chan []string
	mutex    sync.Mutex
}

type Game struct {
	players []*Player
	maps    []*Map
	mutex   sync.Mutex
}

func NewGame(mapIds []int) (*Game, error) {
	game := &Game{
		players: make([]*Player, 0),
		maps:    make([]*Map, 0),
	}

	seenIds := make(map[int]bool)
	for _, id := range mapIds {
		if id <= 0 {
			return nil, errors.New("map id must be positive")
		}
		if seenIds[id] {
			return nil, errors.New("duplicate map id provided")
		}
		seenIds[id] = true

		newMap := &Map{
			id:       id,
			players:  make([]*Player, 0),
			messages: make(chan []string, 100),
		}
		game.maps = append(game.maps, newMap)

		go newMap.FanOutMessages()
	}
	return game, nil
}

func (g *Game) ConnectPlayer(name string) error {
	g.mutex.Lock()
	defer g.mutex.Unlock()

	for _, p := range g.players {
		if strings.EqualFold(p.name, name) {
			return errors.New("player with this name already connected")
		}
	}

	player := &Player{
		name:     name,
		messages: make(chan string, 10),
	}

	g.players = append(g.players, player)
	return nil
}

func (g *Game) SwitchPlayerMap(name string, mapId int) error {
	player, err := g.GetPlayer(name)
	if err != nil {
		return err
	}

	newMap, err := g.GetMap(mapId)
	if err != nil {
		return err
	}

	player.mutex.Lock()
	oldMap := player.currentMap
	player.mutex.Unlock()

	if oldMap != nil && oldMap.id == newMap.id {
		return errors.New(player.GetName() + " is already in this map")
	}

	if oldMap != nil {
		oldMap.mutex.Lock()
		foundIndex := -1
		for i, p := range oldMap.players {
			if p == player {
				foundIndex = i
				break
			}
		}
		if foundIndex != -1 {
			oldMap.players[foundIndex] = oldMap.players[len(oldMap.players)-1]
			oldMap.players = oldMap.players[:len(oldMap.players)-1]
		}
		oldMap.mutex.Unlock()
	}

	newMap.mutex.Lock()
	newMap.players = append(newMap.players, player)
	newMap.mutex.Unlock()

	player.mutex.Lock()
	player.currentMap = newMap
	player.mutex.Unlock()

	return nil
}

func (g *Game) GetPlayer(name string) (*Player, error) {
	g.mutex.Lock()
	defer g.mutex.Unlock()

	for _, player := range g.players {
		if strings.EqualFold(player.GetName(), name) {
			return player, nil
		}
	}

	return nil, errors.New(name + " not found in the game")
}

func (g *Game) GetMap(mapId int) (*Map, error) {
	g.mutex.Lock()
	defer g.mutex.Unlock()

	for _, regionMap := range g.maps {
		if regionMap.id == mapId {
			return regionMap, nil
		}
	}

	return nil, errors.New("map with id: " + strconv.Itoa(mapId) + " not found in the game")
}

func (m *Map) FanOutMessages() {
	for msg := range m.messages {

		senderName := msg[0]
		text := msg[1]
		fullMessage := fmt.Sprintf("%s says: %s", senderName, text)

		m.mutex.Lock()
		for _, player := range m.players {
			if player.GetName() != senderName {

				select {
				case player.messages <- fullMessage:
				default:
				}
			}
		}
		m.mutex.Unlock()
	}
}

func (p *Player) GetChannel() <-chan string {
	return p.messages
}

func (p *Player) SendMessage(msg string) error {
	p.mutex.Lock()
	defer p.mutex.Unlock()

	if p.currentMap == nil {
		return errors.New("player has no map")
	}

	message := []string{p.GetName(), msg}
	p.currentMap.messages <- message

	return nil
}

func (p *Player) GetName() string {
	if p.name == "" {
		return ""
	}

	lowerName := strings.ToLower(p.name)
	return strings.ToUpper(string(lowerName[0])) + lowerName[1:]
}
