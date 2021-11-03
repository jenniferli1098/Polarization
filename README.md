# Polarization

## main.py

Configure the following variables
| Variable Name | Definition | Dimension |
| ------------- | ---------- | ---- |
| a_candidates | the identity affiliations of the candidates | m |
| p_candidates | the probability of the candidate shifting the state to the right | m |
| a_voters     | the identity affilication of the voters | n |
| r_voters     | the true rewards that each voter gains towards each candidate | n x m |
| states       | states that the system will have (in range [0,1]) | |

## model.py

The following customizations are possible:

```
model.set_state(1)                     # initial state (first state by default)
model.set_voting_rule("plurality")     # plurality(default)
model.set_type("mallows")              # deterministic (default) or mallows
```

## Run Simulation

Run:
```
python main.py
```

