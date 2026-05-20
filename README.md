# ICS381-PA4 — Adversarial Search (Minimax + Alpha-Beta)

Programming assignment 4 for **ICS 381 – Introduction to Artificial Intelligence** at KFUPM (Term 222). Implements adversarial search for two-player zero-sum games — applied to **chess** via `python-chess`.

> Auto-grader score: **100%**.

## What's inside

- `games.py` / `games.ipynb` — `minimax`, `alpha_beta_search`, and heuristic-bounded `h_minimax`. Includes a chess heuristic (`heuristic_chess`) that handles terminal states (win / draw / loss) and material evaluation for non-terminals.
- `refoutput_test_alpha_beta.txt`, `refoutput_test_h_minimax.txt`, `refoutput_test_profiling.txt` — reference outputs used by the grader.
- `ai_env.yml` — conda environment used in the course (includes `python-chess`).

## Run

```bash
conda env create -f ai_env.yml
conda activate ai_env
python games.py
```

---

*Archived: course artifact, kept for reference.*
