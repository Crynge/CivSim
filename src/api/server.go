// CivSim Go API — High-performance simulation backend
package main

import (
    "encoding/json"
    "fmt"
    "net/http"
)

type Agent struct {
    ID      string  `json:"id"`
    Name    string  `json:"name"`
    Role    string  `json:"role"`
    Health  float64 `json:"health"`
    Energy  float64 `json:"energy"`
}

type SimulationStatus struct {
    Running bool  `json:"running"`
    Tick    int   `json:"tick"`
    Agents  int   `json:"agents"`
}

var status = SimulationStatus{Running: false, Tick: 0, Agents: 100}

func handleStatus(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(status)
}

func handleAgents(w http.ResponseWriter, r *http.Request) {
    agents := make([]Agent, status.Agents)
    for i := 0; i < status.Agents; i++ {
        roles := []string{"settler", "trader", "builder", "farmer"}
        agents[i] = Agent{
            ID: fmt.Sprintf("agent-%d", i),
            Name: fmt.Sprintf("Citizen %d", i),
            Role: roles[i%4],
            Health: 80.0,
            Energy: 60.0,
        }
    }
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(map[string]interface{}{"agents": agents, "total": len(agents)})
}

func main() {
    http.HandleFunc("/api/v1/simulation/status", handleStatus)
    http.HandleFunc("/api/v1/agents", handleAgents)
    fmt.Println("CivSim Go API on :9090")
    http.ListenAndServe(":9090", nil)
}
