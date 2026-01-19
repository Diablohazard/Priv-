# Exo_1

## Class

```mermaid
classDiagram
    class Robot {
        +str marque
        +bool state_OK
        +int nb_alarme
        +list<int> pos_Tool
        +GetStatus()
        +MoveHome()
        +MovePick()
        +MovePlace()
        +RaiseDefault()
        +ClearDefault()
}
```

marque = FANUC
